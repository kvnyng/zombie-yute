from enum import Enum
import pyaudio
import numpy as np
import torch
from dataclasses import dataclass
# Parameters for the audio recording
from typing import Optional
import math

from .datatypes.lexicon import *

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
VOLUME_THRESHOLD = 40  # in dB

p = pyaudio.PyAudio()

def stream_callback(in_data, frame_count, time_info, status):
    frames.append(np.frombuffer(in_data, dtype=np.int16))
    return (in_data, pyaudio.paContinue)

# Open a stream with the above parameters
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK,
                stream_callback=stream_callback)

@dataclass
class AudioData:
    volume: float
    note: Note

    def __str__(self):
        return f"Volume: {self.volume}, Note: {self.note.name}{self.note.octave}: {self.note.freq}Hz"

def freq_to_note(freq) -> Note:
    notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

    note_number = 12 * math.log2(freq / 440) + 49  
    note_number = round(note_number)
        
    note_index = (note_number - 1 ) % len(notes)
    note = notes[note_index]
    
    octave = (note_number + 8 ) // len(notes)
    
    if note == 'A#' or note == 'C#' or note == 'D#' or note == 'F#' or note == 'G#':
        note = notes[note_index - 1]
    
    return Note(note, octave, freq)

frames = []

def sound_picker() -> Optional[AudioData]:
    if (len(frames) < RATE/CHUNK):
        return None
    
    audio = np.hstack(frames)
    volume = math.log10(np.linalg.norm(audio)) * 10
    
    fft_result = np.fft.fft(audio)
    frequencies = np.fft.fftfreq(len(fft_result), 1.0 / RATE)
    
    # Only take the positive part of the spectrum
    positive_freqs = frequencies[:len(frequencies)//2]
    positive_fft = np.abs(fft_result[:len(fft_result)//2])

    positive_freqs_sorted = np.argsort(positive_fft)

    # for i in range(1, 4):
    #     print("The ", i, "th loudest frequency is: ", positive_freqs[positive_freqs_sorted[-i]], "Hz")
    
    # Grabbing the fundamental frequency, the lowest note out of the top three loudest frequencies
    loudest_freq = [positive_freqs[positive_freqs_sorted[-i]] for i in range(1, 5)]
    fundemental_freq = min(loudest_freq)


    note: Note = freq_to_note(fundemental_freq)
    
    frames.clear()

    return AudioData(volume, note)

def listener():
    global return_data
    while True:
        return_data = sound_picker()
        if return_data:
            # call to check if audio is triggering
            # then feed into map
            print(return_data)

import multiprocessing

if __name__ == "__main__":
    print("Starting listener")
    listen = multiprocessing.Process(target=listener)
    listen.start()