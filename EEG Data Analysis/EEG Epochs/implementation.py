import matplotlib.pyplot as plt
import numpy as np
import mne

raw_file = mne.io.read_raw_bdf("EEG Data Analysis\EEG Epochs\sub-01.bdf")


raw_file.compute_psd(fmax=50).plot(picks="data", exclude="bads", amplitude=False)
raw_file.plot(duration=1, block=True)


