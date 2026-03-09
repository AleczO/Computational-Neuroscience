import numpy as np
import matplotlib.pyplot as plt
import mne

raw_file = mne.io.read_raw_bdf(r"EEG\EEGs Data\illusory-face-eeg\sub-01_task-faceobj_eeg.bdf")

raw_file.plot(block=True)

#print(raw_file.info)
#print(raw_file.ch_names)

#raw_file.crop(tmin=64.0, tmax=68.0)

#data, times = raw_file.get_data(return_times=True)

#data = data * 1e6



##plt.plot(times, data[0])
#Aplt.show()

"""



def display_epochs():
    events = mne.find_events(raw_file, stim_channel="Status")
    epochs = mne.Epochs(raw_file, events, tmin=-0.005, tmax=0.115)

    epochs.plot(n_epochs=10, events=True, block=True)


def display_raw():
    raw_file.compute_psd(fmax=50).plot(picks="data", exclude="bads", amplitude=False)
    raw_file.plot(block=True)
    


# display_epochs()

display_raw()
"""
