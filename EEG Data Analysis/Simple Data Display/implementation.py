import numpy as np
import mne


file = mne.io.read_raw_eeglab("EEG Data Analysis/Simple Data Display/002.set") 

file.plot(start=0, duration=5, block=True)


'''
file = mne.read_evokeds(
    file, baseline=(None, 0), proj=True, verbose=False
)


for e in file:
    print(f"Condition: {e.comment}, baseline: {e.baseline}")


conds = ("aud/left", "aud/right", "vis/left", "vis/right")
evks = dict(zip(conds, file))

evks["aud/left"].plot(exclude=[])
'''