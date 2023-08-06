from functools import partial
from glob import glob
from os import path

import numpy as np
import pandas as pd
from joblib import Parallel, delayed

from .averaging import compute_grands, compute_grands_df
from .io import (convert_participant_input, files_from_dir, save_config,
                 save_df, save_evokeds)
from .participant import participant_pipeline
from .perm import compute_perm, compute_perm_tfr


def group_pipeline(
    vhdr_files,
    log_files,
    output_dir,
    clean_dir=None,
    epochs_dir=None,
    report_dir=None,
    to_df=True,
    downsample_sfreq=None,
    veog_channels='auto',
    heog_channels='auto',
    montage='easycap-M1',
    bad_channels=None,
    ocular_correction='auto',
    highpass_freq=0.1,
    lowpass_freq=40.,
    triggers=None,
    triggers_column=None,
    epochs_tmin=-0.5,
    epochs_tmax=1.5,
    baseline_tmin=-0.2,
    baseline_tmax=0.0,
    skip_log_rows=None,
    skip_log_conditions=None,
    reject_peak_to_peak=200.,
    components={'name': [], 'tmin': [], 'tmax': [], 'roi': []},
    average_by=None,
    perform_tfr=False,
    tfr_subtract_evoked=False,
    tfr_freqs=np.linspace(4., 40., num=37),
    tfr_cycles=np.linspace(2., 20., num=37),
    tfr_baseline_tmin=-0.45,
    tfr_baseline_tmax=-0.05,
    tfr_baseline_mode='percent',
    tfr_components={
        'name': [], 'tmin': [], 'tmax': [], 'fmin': [], 'fmax': [], 'roi': []},
    perm_contrasts=[],
    perm_tmin=0.,
    perm_tmax=1.,
    perm_channels=None,
    perm_fmin=None,
    perm_fmax=None,
    n_jobs=1
):
    """Processes EEG data for all participants of an experiment.

    For each participant, the raw data is read and cleaned using standard steps
    (downsampling, bad channel interpolation, ocular correction, frequency
    domain filtering). Epochs are created around the `triggers`. Bad epochs are
    removed based on peak-to-peak amplitude. Single trial mean ERP amplitudes
    for ERP `components` of interest are computed and matched to the single
    trial behavioral data from the `log_files`.

    Optionally, this last step is repeated on a time-frequency representation
    (TFR) of the data obtained via Morlet wavelet convolution.

    The result is a single trial data frame which can be used for fitting
    linear mixed-effects models on the mean ERP amplitudes (and power).

    Additionally, by-participant condition averages (`evokeds`) for the ERPs
    (and power) are computed to facilitate plotting. Optionally, these can also
    be tested for condition differences in an exploratory fashion using
    cluster-based permutation tests.

    For details about the pipeline, see Frömer et al. (2018)[1].

    Parameters & returns
    --------------------
    See the README[2] in the GitHub repository for the pipeline.

    Notes
    -----
    [1] https://doi.org/10.3389/fnins.2018.00048
    [2] https://github.com/alexenge/hu-neuro-pipeline/blob/dev/README.md
    """

    # Convert input types
    tfr_freqs = list(tfr_freqs)
    tfr_cycles = list(tfr_cycles)

    # Backup input arguments for re-use
    config = locals().copy()

    # Create partial function with arguments shared across participants
    partial_pipeline = partial(
        participant_pipeline,
        skip_log_conditions=skip_log_conditions,
        downsample_sfreq=downsample_sfreq,
        veog_channels=veog_channels,
        heog_channels=heog_channels,
        montage=montage,
        highpass_freq=highpass_freq,
        lowpass_freq=lowpass_freq,
        triggers=triggers,
        triggers_column=triggers_column,
        epochs_tmin=epochs_tmin,
        epochs_tmax=epochs_tmax,
        baseline_tmin=baseline_tmin,
        baseline_tmax=baseline_tmax,
        reject_peak_to_peak=reject_peak_to_peak,
        components=components,
        average_by=average_by,
        perform_tfr=perform_tfr,
        tfr_subtract_evoked=tfr_subtract_evoked,
        tfr_freqs=tfr_freqs,
        tfr_cycles=tfr_cycles,
        tfr_baseline_tmin=tfr_baseline_tmin,
        tfr_baseline_tmax=tfr_baseline_tmax,
        tfr_baseline_mode=tfr_baseline_mode,
        tfr_components=tfr_components,
        clean_dir=clean_dir,
        epochs_dir=epochs_dir,
        chanlocs_dir=output_dir,
        report_dir=report_dir,
        to_df=to_df)

    # Get input file paths if directories were provided
    if isinstance(vhdr_files, str):
        vhdr_files = files_from_dir(vhdr_files, extensions=['vhdr'])
    if isinstance(log_files, str):
        log_files = files_from_dir(log_files, extensions=['csv', 'tsv', 'txt'])

    # Prepare ocular correction method
    if not isinstance(ocular_correction, list):
        if ocular_correction is None or ocular_correction == 'auto':
            ocular_correction = [ocular_correction] * len(vhdr_files)
        elif path.isdir(ocular_correction):
            ocular_correction = files_from_dir(
                ocular_correction, extensions=['matrix'])

    # Extract participant IDs from filenames
    participant_ids = [path.basename(f).split('.')[0] for f in vhdr_files]

    # Construct lists of bad_channels and skip_log_rows per participant
    bad_channels = convert_participant_input(bad_channels, participant_ids)
    skip_log_rows = convert_participant_input(skip_log_rows, participant_ids)

    # Combine participant-specific inputs
    participant_args = zip(vhdr_files, log_files, ocular_correction,
                           bad_channels, skip_log_rows)

    # Do processing in parallel
    n_jobs = int(n_jobs)
    res = Parallel(n_jobs)(
        delayed(partial_pipeline)(*args) for args in participant_args)

    # Sort outputs into seperate lists
    print(f'\n\n=== PROCESSING GROUP LEVEL ===')
    trials, evokeds, evokeds_dfs, configs = list(map(list, zip(*res)))[0:4]

    # Combine trials and save
    trials = pd.concat(trials, ignore_index=True)
    save_df(trials, output_dir, suffix='trials')

    # Combine evokeds_dfs and save
    evokeds_df = pd.concat(evokeds_dfs, ignore_index=True)
    save_df(evokeds_df, output_dir, suffix='ave')

    # Compute grand averaged ERPs and save
    grands = compute_grands(evokeds)
    grands_df = compute_grands_df(evokeds_df)
    save_evokeds(
        grands, grands_df, output_dir, participant_id='grand', to_df=to_df)

    # Update config with participant-specific inputs...
    config['vhdr_files'] = vhdr_files
    config['ocular_correction'] = ocular_correction
    config['bad_channels'] = bad_channels
    config['skip_log_rows'] = skip_log_rows

    # ... and outputs that might have been created along the way
    config['log_files'] = []
    config['rejected_epochs'] = {}
    for pid, pconfig in zip(participant_ids, configs):
        config['log_files'].append(pconfig['log_file'])
        config['rejected_epochs'][pid] = pconfig['rejected_epochs']
        if pconfig['bad_channels'] == 'auto':
            config.setdefault('auto_bad_channels', {}).update(
                {pid: pconfig['auto_bad_channels']})
        if pconfig['ocular_correction'] == 'auto':
            config.setdefault('auto_bad_icas', {}).update(
                {pid: pconfig['auto_bad_icas']})

    # Save config
    save_config(config, output_dir)

    # Define standard returns
    returns = [trials, evokeds_df, config]

    # Cluster based permutation tests for ERPs
    if perm_contrasts != []:
        cluster_df = compute_perm(evokeds, perm_contrasts, perm_tmin,
                                  perm_tmax, perm_channels, n_jobs)
        save_df(cluster_df, output_dir, suffix='clusters')
        returns.append(cluster_df)

    # Combine time-frequency results
    if perform_tfr:

        # Sort outputs into seperate lists
        tfr_evokeds, tfr_evokeds_dfs = list(map(list, zip(*res)))[4:6]

        # Combine evokeds_df for power and save
        tfr_evokeds_df = pd.concat(tfr_evokeds_dfs, ignore_index=True)
        save_df(tfr_evokeds_df, output_dir,
                suffix='tfr_ave')
        returns.append(tfr_evokeds_df)

        # Compute grand averaged power and save
        tfr_grands = compute_grands(tfr_evokeds)
        tfr_grands_df = compute_grands_df(tfr_evokeds_df)
        save_evokeds(tfr_grands, tfr_grands_df, output_dir,
                     participant_id='tfr_grand', to_df=to_df)

        # Cluster based permutation tests for TFR
        if perm_contrasts != []:
            tfr_cluster_df = compute_perm_tfr(
                tfr_evokeds, perm_contrasts, perm_tmin, perm_tmax,
                perm_channels, perm_fmin, perm_fmax, n_jobs)
            save_df(tfr_cluster_df, output_dir, suffix='tfr_clusters')
            returns.append(tfr_cluster_df)

    return returns
