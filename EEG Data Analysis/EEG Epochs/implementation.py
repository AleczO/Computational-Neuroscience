import matplotlib.pyplot as plt
import numpy as np
import mne

raw_file = mne.io.read_raw_bdf("EEG Data Analysis\EEG Epochs\sub-01.bdf")

print(raw_file.info)
print(raw_file.ch_names)
print(raw_file.__len__())

raw_file.crop(tmin=64.0,tmax=164.0)

print(raw_file.__len__())



events = mne.find_events(raw_file, stim_channel="Status")
epochs = mne.Epochs(raw_file, events, tmin=-0.01, tmax=0.12)

epochs.plot(n_epochs=10, events=True, block=True)
