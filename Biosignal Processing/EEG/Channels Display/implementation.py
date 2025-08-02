import mne

file = mne.io.read_raw_edf(r"../EEGs Data/4/S1.edf")

print(file.info)

file.compute_psd(fmax=50).plot(picks="data", exclude="bads", amplitude=False)
file.plot(block=True)
