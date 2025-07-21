import numpy as np
import mne


file = mne.io.read_raw_edf("EEG Data Analysis/Simple Channels Display/P1.edf") 

print(file.info)

file.compute_psd(fmax=50).plot(picks="data", exclude="bads", amplitude=False)
file.plot(duration=1, block=True)
