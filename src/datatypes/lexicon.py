from dataclasses import dataclass
import multiprocessing
from typing import Any, Optional
from enum import Enum


class NoteOrder(dict[str, int]):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.update({
            "C": 0,
            "C#": 1,
            "D": 2,
            "D#": 3,
            "E": 4,
            "F": 5,
            "F#": 6,
            "G": 7,
            "G#": 8,
            "A": 9,
            "A#": 10,
            "B": 11
        })

@dataclass
class Note:
    name: str
    octave: int
    freq: float

    def __gt__(self, other):
        if self.octave > other.octave:
            return True
        elif self.octave == other.octave:
            return NoteOrder()[self.name] > NoteOrder()[other.name]
    
    def __eq__(self, other):
        return self.octave == other.octave and self.name == other.name
    
    def __ge__(self, other):
        return self > other or self == other
    
    def __hash__(self) -> int:
        return hash((self.name, self.octave))
    
    def __str__(self) -> str:
        return f"{self.name}{self.octave}"
    
    def __repr__(self) -> str:
        return f"{self.name}{self.octave}"
        

@dataclass
class AudioData:
    volume: float
    note: Note

    # def __str__(self):
    #     return f"Volume: {self.volume}, Note: {self.note.name}{self.note.octave}: {self.note.freq}Hz"

    def __repr__(self) -> str:
        return f"{self.note.name}{self.note.octave}"
    
    def __str__(self) -> str:
        return f"{self.note.name}{self.note.octave}"
    
    def __gt__(self, other):
        return self.note > other.note

    def __eq__(self, other):
        if not isinstance(other, AudioData):
            return False
        return self.note == other.note

class WordToPitch(dict[Note, str]):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class PitchToWord(dict[str, Note]):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class Openers(WordToPitch):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.update(
            WordToPitch({
                Note("C", 3, 130.81): "Whazzgood",
                Note("D", 3, 146.83): "Hol’up",
                Note("E", 3, 164.81): "Yo",
                Note("F", 3, 174.61): "Nah-fam",
                Note("G", 3, 185): "Straight-up",
                Note("A", 3, 220): "Real talk",
                Note("B", 3, 246.93): "Wagwan",
                Note("C", 2, 261.63): "We out here",
                Note("D", 2, 293.66): "Slime"
            })
        )



class Subjects(WordToPitch):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.update(
            WordToPitch({
                Note("C", 3, 130.81): "Fam",
                Note("D", 3, 146.83): "Big Man",
                Note("E", 3, 164.81): "Mandem",
                Note("F", 3, 174.61): "Bredrin",
                Note("G", 3, 185): "Plug",
                Note("A", 3, 220): "Ting",
                Note("B", 3, 246.93): "Galdem",
                Note("C", 2, 261.63): "Ends",
                Note("D", 2, 293.66): "Whip",
                Note("E", 2, 329.63): "Cheese",
                Note("F", 2, 349.23): "Drip",
                Note("G", 2, 369.99): "Water",
                Note("A", 2, 440): "Brains",
                Note("B", 2, 493.88): "We"
            })
        )

class Verbs(WordToPitch):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.update(
            WordToPitch({
                Note("C", 2, 261.63): "Run",
                Note("D", 2, 293.66): "Skrrt",
                Note("E", 2, 329.63): "Swerve",
                Note("F", 2, 349.23): "Run up",
                Note("G", 2, 369.99): "Chop",
                Note("A", 2, 440): "Mash up",
                Note("B", 2, 493.88): "Could",
                Note("C", 3, 130.81): "Link",
                Note("D", 3, 146.83): "Holla",
                Note("E", 3, 164.81): "Whippin",
                Note("F", 3, 174.61): "Chirpin’",
                Note("G", 3, 185): "Flexin’",
                Note("A", 3, 220): "Catch-a-vibe",
                Note("B", 3, 246.93): "Settle",
            })
        )

class Objects(WordToPitch):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.update(
            WordToPitch({
                Note("C", 3, 130.81): "Gwop",
                Note("D", 3, 146.83): "Piff",
                Note("E", 3, 164.81): "Block",
                Note("F", 3, 174.61): "6ix",
                Note("G", 3, 185): "Food",
                Note("A", 3, 220): "Yute",
                Note("B", 3, 246.93): "Slime",
                Note("C", 2, 261.63): "Cheese",
                Note("D", 2, 293.66): "Whip",
                Note("E", 2, 329.63): "G",
                Note("F", 2, 349.23): "Ends",
                Note("G", 2, 369.99): "Ting",
                Note("A", 2, 440): "Drip",
                Note("B", 2, 493.88): "Watah"
            })
        )

class Closers(WordToPitch):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.update(
            WordToPitch({
                Note("C", 3, 130.81): "Deadass",
                Note("D", 3, 146.83): "No cap",
                Note("E", 3, 164.81): "Facts",
                Note("F", 3, 174.61): "Bless up",
                Note("G", 3, 185): "Boom",
                Note("A", 3, 220): "Safe",
                Note("B", 3, 246.93): "Trust",
                Note("C", 2, 261.63): "On god",
                Note("D", 2, 293.66): "Say less",
                Note("E", 2, 329.63): "You dun know",
                Note("F", 2, 349.23): "Clapped",
                Note("G", 2, 369.99): "On job",
                Note("A", 2, 440): "Bless up",
                Note("B", 2, 493.88): "Safe"
            })
        )

@dataclass
class Grammar(Enum):
    Opener = 0
    Subject = 1
    Verb = 2
    Object = 3
    Closer = 4

    def __hash__(self) -> int:
        return hash(self.value)
    
class intToGrammar(dict[int, Grammar]):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.update({
            0: Grammar.Opener,
            1: Grammar.Subject,
            2: Grammar.Verb,
            3: Grammar.Object,
            4: Grammar.Closer
        })

class OpenersReverse(PitchToWord):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.update(
            PitchToWord({
                "whazzgood": "data/C3.mp3",
                "hol’up": "data/D3.mp3",
                "yo": "data/E3.mp3",
                "nah-fam": "data/F3.mp3",
                "straight-up": "data/G3.mp3",
                "real talk": "data/A3.mp3",
                "wagwan": "data/B3.mp3",
                "we out here": "data/C4.mp3",
                "slime": "data/D4.mp3"
            })
        )

class SubjectsReverse(PitchToWord):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.update(
            PitchToWord({
                "fam": "data/C3.mp3",
                "big Man": "data/D3.mp3",
                "mandem": "data/E3.mp3",
                "bredrin": "data/F3.mp3",
                "plug": "data/G3.mp3",
                "ting": "data/A3.mp3",
                "galdem": "data/B3.mp3",
                "ends": "data/C4.mp3",
                "whip": "data/D4.mp3",
                "cheese": "data/E4.mp3",
                "drip": "data/F4.mp3",
                "water": "data/G4.mp3",
                "brains": "data/A4.mp3",
                "we": "data/B4.mp3"
            })
        )
# Look for sytax errors in the following code
class VerbsReverse(PitchToWord):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.update(
            PitchToWord({
                "link": "data/C3.mp3",
                "holla": "data/D3.mp3",
                "whippin": "data/E3.mp3",
                "chirpin’": "data/F3.mp3",
                "flexin’": "data/G3.mp3",
                "catch-a-vibe": "data/A3.mp3",
                "settle": "data/B3.mp3",
                "run": "data/C4.mp3",
                "skrrt": "data/D4.mp3",
                "swerve": "data/E4.mp3",
                "run up": "data/F4.mp3",
                "chop": "data/G4.mp3",
                "mash up": "data/A4.mp3",
                "could": "data/B4.mp3"
            })
        )

class ObjectsReverse(PitchToWord):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.update(
            PitchToWord({
                "gwop": "data/C3.mp3",
                "piff": "data/D3.mp3",
                "block": "data/E3.mp3",
                "six": "data/F3.mp3",
                "food": "data/G3.mp3",
                "yute": "data/A3.mp3",
                "slime": "data/B3.mp3",
                "cheese": "data/C4.mp3",
                "whip": "data/D4.mp3",
                "g": "data/E4.mp3",
                "ends": "data/F4.mp3",
                "ting": "data/G4.mp3",
                "drip": "data/A4.mp3",
                "watah": "data/B4.mp3"
            })
        )
        
class ClosersReverse(PitchToWord):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.update(
            PitchToWord({
            "deadass": "data/C3.mp3",
            "no cap": "data/D3.mp3",
            "facts": "data/E3.mp3",
            "bless up": "data/F3.mp3",
            "boom": "data/G3.mp3",
            "safe": "data/A3.mp3",
            "trust": "data/B3.mp3",
            "on god": "data/C4.mp3",
            "say less": "data/D4.mp3",
            "you dun know": "data/E4.mp3",
            "clapped": "data/F4.mp3",
            "on job": "data/G4.mp3",
            "bless up": "data/A4.mp3",
            "safe": "data/B4.mp3"
            })
        )

class Lexicon(dict[Grammar, WordToPitch]):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.update({
            Grammar.Opener: Openers(),
            Grammar.Subject: Subjects(),
            Grammar.Verb: Verbs(),
            Grammar.Object: Objects(),
            Grammar.Closer: Closers()
        })

# class SentenceQueue(multiprocessing.Queue):
#     def __init__(self, maxsize: int = 0, *, ctx: Any = ...) -> None:
#         super().__init__(maxsize, ctx=ctx)

#     def __str__(self) -> str:
#         return " ".join([str(item) for item in list(self.queue)])

    