import matplotlib.pyplot as plt
import numpy as np
import mne


raw_file = mne.io.read_raw_fif("MEG Data Analysis\\MEGs Data\\1\\sub-01_ses-01_task-main_run-01_meg.fif")

raw_file.plot(duration=5, n_channels=1, block=True)

raw_file.compute_psd(fmax=50).plot(picks="data", exclude="bads", amplitude=False)