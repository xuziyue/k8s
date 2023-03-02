import numpy as np
from scipy.signal import find_peaks

# Generate a signal with a period of 50 samples
N = 1000
t = np.arange(N)
period = 120
signal = np.sin(2 * np.pi * t / period)

# Compute the FFT of the signal
fft_signal = np.fft.rfft(signal)

# # Find the peak in the magnitude of the FFT
# peaks, _ = find_peaks(np.abs(fft_signal))

idx = np.abs(fft_signal).argmax()

# Calculate the frequency at the peak location
freqs = np.fft.rfftfreq(N)
freq_at_peak = freqs[idx]

# Calculate the period from the frequency at the peak location
calculated_period = 1 / freq_at_peak

print(f"Calculated period: {calculated_period}")
