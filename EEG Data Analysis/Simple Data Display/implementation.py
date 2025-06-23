import numpy as np
import mne


file = mne.io.read_raw_eeglab("EEG Data Analysis/Simple Data Display/002.set") 

file.plot(start=0, duration=5, block=True)
