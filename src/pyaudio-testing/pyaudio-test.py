import pyaudio
import numpy as np
import torch
from dataclasses import dataclass
# Parameters for the audio recording
from typing import Optional
import math

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
VOLUME_THRESHOLD = 40 # in dB

p = pyaudio.PyAudio()

# Open a stream with the above parameters
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)


@dataclass
class Note:
    name: str
    octave: int

@dataclass
class AudioData:
    volume: float
    note: Note

    def __str__(self):
        return f"Volume: {self.volume}, Note: {self.note.name}{self.note.octave}"

def freq_to_note(freq) -> Note:
    notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

    note_number = 12 * math.log2(freq / 440) + 49  
    note_number = round(note_number)
        
    note_index = (note_number - 1 ) % len(notes)
    note = notes[note_index]
    
    octave = (note_number + 8 ) // len(notes)
    
    if note == 'A#' or note == 'C#' or note == 'D#' or note == 'F#' or note == 'G#':
        note = notes[note_index - 1]
    return Note(note, octave)

def listener() -> Optional[AudioData]:
    frames = []
    for _ in range(0, int(RATE / CHUNK)):
        data = stream.read(CHUNK)
        frames.append(np.frombuffer(data, dtype=np.int16))
    
    audio = np.hstack(frames)
    volume = math.log10(np.linalg.norm(audio)) * 10
    
    fft_result = np.fft.fft(audio)
    frequencies = np.fft.fftfreq(len(fft_result), 1.0 / RATE)

    if not volume > VOLUME_THRESHOLD:
        return None
    
    # Only take the positive part of the spectrum
    positive_freqs = frequencies[:len(frequencies)//2]
    positive_fft = np.abs(fft_result[:len(fft_result)//2])

    positive_freqs_sorted = np.argsort(positive_fft)

    # for i in range(1, 4):
    #     print("The ", i, "th loudest frequency is: ", positive_freqs[positive_freqs_sorted[-i]], "Hz")

    note: Note = freq_to_note(positive_freqs[positive_freqs_sorted[-1]])

    return_data = AudioData(volume, note)

    return return_data
