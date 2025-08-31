import matplotlib.pyplot as plt
import numpy as np
import mne


raw_file = mne.io.read_raw_fif(r"MEG\MEGs Data\the-spatiotemporal-neural-dynamics-of-object-recognition-for-natural-images-and-line-drawings\sub-01_ses-01_task-main_run-01_meg.fif")

raw_file.plot(duration=5, block=True)

raw_file.compute_psd(fmax=50).plot(picks="data", exclude="bads", amplitude=False)