import numpy as np
import mne


file = mne.io.read_raw_eeglab("EEG Data Analysis/Simple Channels Display/002.set") 

file.compute_psd(fmax=50).plot(picks="data", exclude="bads", amplitude=False)
file.plot(duration=5, block=True)
