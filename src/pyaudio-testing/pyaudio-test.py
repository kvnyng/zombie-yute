import pyaudio
import numpy as np
import matplotlib.pyplot as plt

# Parameters for the audio recording
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
VOLUME_THRESHOLD = 100000

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
frames = []

while True:
    for _ in range(0, int(RATE / CHUNK)):
        data = stream.read(CHUNK)
        frames.append(np.frombuffer(data, dtype=np.int16))

    print("Recording finished.")

    audio_data = np.hstack(frames)
    volume = np.linalg.norm(audio_data)

    if volume > VOLUME_THRESHOLD:
        print("Sound detected.")
    else:
        print("No sound detected.")
        continue

    fft_result = np.fft.fft(audio_data)
    frequencies = np.fft.fftfreq(len(fft_result), 1.0 / RATE)

    # Only take the positive part of the spectrum
    positive_freqs = frequencies[:len(frequencies)//2]
    positive_fft = np.abs(fft_result[:len(fft_result)//2])

    positive_freqs_sorted = np.argsort(positive_fft)

    for i in range(1, 4):
        print("The ", i, "th loudest frequency is: ", positive_freqs[positive_freqs_sorted[-i]], "Hz")
    print("\n")
    frames=[]