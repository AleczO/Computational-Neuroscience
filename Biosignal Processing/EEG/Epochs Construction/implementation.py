import matplotlib.pyplot as plt
import numpy as np
import mne

raw_file = mne.io.read_raw_bdf(r"../EEGs Data/3/S01.bdf")

print(raw_file.info)
print(raw_file.ch_names)

raw_file.crop(tmin=64.0, tmax=68.0)

def display_epochs():
    events = mne.find_events(raw_file, stim_channel="Status")
    epochs = mne.Epochs(raw_file, events, tmin=-0.005, tmax=0.115)

    epochs.plot(n_epochs=10, events=True, block=True)


def display_raw():
    raw_file.plot(block=True)


display_epochs()

