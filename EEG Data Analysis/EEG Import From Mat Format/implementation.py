from pymatreader import read_mat
import matplotlib.pyplot as plt
import numpy as np
import mne

raw_file = read_mat("EEG Data Analysis\EEG Import From Mat Format\S0.mat")


print(raw_file['SIGNAL'].shape)


raw_channels = np.transpose(raw_file['SIGNAL'])
raw_channels = raw_channels[2:17, :]

channels_count = raw_channels.shape[0]



info = mne.create_info(ch_names = [f"CH{i + 1}" for i in range(channels_count)], sfreq=512)
raw = mne.io.RawArray(raw_channels, info)

raw.plot(duration=5, block=True)