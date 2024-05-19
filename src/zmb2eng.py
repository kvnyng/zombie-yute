from enum import Enum
import pyaudio
import numpy as np
import torch
from dataclasses import dataclass
# Parameters for the audio recording
from typing import Optional
import math

from queue import Queue

from .datatypes.lexicon import *

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
VOLUME_THRESHOLD = 50  # in dB

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
    history: list[AudioData] = [None] * 10
    previous: Optional[AudioData] = None
    while True:

        if len(history) > 5:
            history.pop(0)

        current = sound_picker()
        print(history, str(previous), str(current))
        
        # Moves on if current is none
        if not current:
            continue
        
        # Adds none, meaning no noise
        if current.volume < VOLUME_THRESHOLD:
            history.append(None)
            continue
        
        if current == previous:
            continue
        
        history.append(current)
        previous = current

        count = count_obj_instances(history, current)
        if count >= 2:
            print("Triggered")
        
        
def count_obj_instances(queue: list[AudioData], obj: AudioData) -> int:
    count: int = 0
    for item in queue:
        if item == obj:
            count += 1
    return count


import multiprocessing

C = Note("C", 3, 130.81)
D = Note("D", 3, 146.83)

print("Is c greater than D?", C > D)

print(Grammar.Closer.value)

if __name__ == "__main__":
    print("Starting listener")
    listen = multiprocessing.Process(target=listener)
    listen.start()