import matplotlib.pyplot as plt
import mne

file = mne.io.read_raw_edf(r"EEG\EEGs Data\mouse-sleep-staging-validation-dataset\sub-001_task-sleep_run-1_eeg.edf")

print(file.info)

file.compute_psd(fmax=50).plot(picks="data", exclude="bads", amplitude=False)
file.plot(block=True)
