
# Exercise 7.1: Fourier Transforms

import numpy as np
import matplotlib.pyplot as plt

N = 1000  # Number of samples
n = np.arange(N)  # Sample points

# Generating waves
square_wave = [np.sign(np.sin(x / 106)) for x in n]
sawtooth_wave = n % (N // 10)
modulated_sine_wave = np.sin(np.pi * n / N) * np.sin(20 * np.pi * n / N)

# Computing Fourier coefficients
fourier_coeffs_square = np.fft.fft(square_wave) / N
fourier_coeffs_sawtooth = np.fft.fft(sawtooth_wave) / N
fourier_coeffs_mod_sin = np.fft.fft(modulated_sine_wave) / N
freqs = np.fft.fftfreq(N)

# Plotting in subplots
fig, axs = plt.subplots(1, 3, figsize=(15, 5), tight_layout=True)
plt.suptitle('Fourier Transformations', fontsize=16)

# Plotting square wave
axs[0].plot(n, square_wave)
axs[0].set_title('Square Wave')
axs[0].set_xlabel('Frequency (Hz)')
axs[0].set_ylabel('Amplitude')
axs[0].set_xlim(1, N)

# Plotting sawtooth wave
axs[1].plot(n, sawtooth_wave)
axs[1].set_title('Sawtooth Wave')
axs[1].set_xlabel('Frequency (Hz)')
axs[1].set_ylabel('Amplitude')

# Plotting modulated sine wave
axs[2].plot(n, modulated_sine_wave)
axs[2].set_title('Modulated Sine Wave')
axs[2].set_xlabel('Frequency (Hz)')
axs[2].set_ylabel('Amplitude')

plt.tight_layout()
plt.show()
