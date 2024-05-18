import pyaudio
import numpy as np
import matplotlib.pyplot as plt

# Parameters for the audio recording
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024

# Initialize PyAudio
p = pyaudio.PyAudio()

# Open a stream with the above parameters
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("Recording...")

# Record data for a set duration
duration = 5  # seconds
frames = []

for _ in range(0, int(RATE / CHUNK * duration)):
    data = stream.read(CHUNK)
    frames.append(np.frombuffer(data, dtype=np.int16))

print("Recording finished.")

# Stop and close the stream
stream.stop_stream()
stream.close()
p.terminate()

# Convert the list of frames into a NumPy array
audio_data = np.hstack(frames)

# Apply FFT
fft_result = np.fft.fft(audio_data)

# Get the corresponding frequencies
frequencies = np.fft.fftfreq(len(fft_result), 1.0 / RATE)

# Only take the positive part of the spectrum
positive_freqs = frequencies[:len(frequencies)//2]
positive_fft = np.abs(fft_result[:len(fft_result)//2])

# Plot the results
plt.plot(positive_freqs, positive_fft)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.title('Frequency Spectrum')
plt.show()
