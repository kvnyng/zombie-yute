from dataclasses import dataclass
from typing import Optional
from enum import Enum


@dataclass
class Note:
    name: str
    octave: int
    freq: float

class WordToPitch(dict[Note, str]):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class PitchToWord(dict[str, Note]):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
class Lexicon(dict[Grammar, str]):
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
                Note("C", 4, 261.63): "We out here",
                Note("D", 4, 293.66): "Slime"
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
                Note("C", 4, 261.63): "Ends",
                Note("D", 4, 293.66): "Whip",
                Note("E", 4, 329.63): "Cheese",
                Note("F", 4, 349.23): "Drip",
                Note("G", 4, 369.99): "Water",
                Note("A", 4, 440): "Brains",
                Note("B", 4, 493.88): "We"
            })
        )

class Verbs(WordToPitch):
    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.update(
            WordToPitch({
                Note("C", 3, 130.81): "Link",
                Note("D", 3, 146.83): "Holla",
                Note("E", 3, 164.81): "Whippin",
                Note("F", 3, 174.61): "Chirpin’",
                Note("G", 3, 185): "Flexin’",
                Note("A", 3, 220): "Catch-a-vibe",
                Note("B", 3, 246.93): "Settle",
                Note("C", 4, 261.63): "Run",
                Note("D", 4, 293.66): "Skrrt",
                Note("E", 4, 329.63): "Swerve",
                Note("F", 4, 349.23): "Run up",
                Note("G", 4, 369.99): "Chop",
                Note("A", 4, 440): "Mash up",
                Note("B", 4, 493.88): "Could"
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
                Note("C", 4, 261.63): "Cheese",
                Note("D", 4, 293.66): "Whip",
                Note("E", 4, 329.63): "G",
                Note("F", 4, 349.23): "Ends",
                Note("G", 4, 369.99): "Ting",
                Note("A", 4, 440): "Drip",
                Note("B", 4, 493.88): "Watah"
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
                Note("C", 4, 261.63): "On god",
                Note("D", 4, 293.66): "Say less",
                Note("E", 4, 329.63): "You dun know",
                Note("F", 4, 349.23): "Clapped",
                Note("G", 4, 369.99): "On job",
                Note("A", 4, 440): "Bless up",
                Note("B", 4, 493.88): "Safe"
            })
        )

@dataclass
class Grammar(WordToPitch, int):
    Opener: Openers = 0
    Subject: Subjects = 1
    Verb: Verbs = 2
    Object: Objects = 3
    Closer: Closers = 4

class OpenersReverse(PitchToWord):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.update(
            PitchToWord({
                "whazzgood": Note("C", 3, 130.81),
                "hol’up": Note("D", 3, 146.83),
                "yo": Note("E", 3, 164.81),
                "nah-fam": Note("F", 3, 174.61),
                "straight-up": Note("G", 3, 185),
                "real talk": Note("A", 3, 220),
                "wagwan": Note("B", 3, 246.93),
                "we out here": Note("C", 4, 261.63),
                "slime": Note("D", 4, 293.66)
            })
        )

class SubjectsReverse(PitchToWord):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.update(
            PitchToWord({
                "fam": Note("C", 3, 130.81),
                "big Man": Note("D", 3, 146.83),
                "mandem": Note("E", 3, 164.81),
                "bredrin": Note("F", 3, 174.61),
                "plug": Note("G", 3, 185),
                "ting": Note("A", 3, 220),
                "galdem": Note("B", 3, 246.93),
                "ends": Note("C", 4, 261.63),
                "whip": Note("D", 4, 293.66),
                "cheese": Note("E", 4, 329.63),
                "drip": Note("F", 4, 349.23),
                "water": Note("G", 4, 369.99),
                "brains": Note("A", 4, 440),
                "we": Note("B", 4, 493.88)
            })
        )

class VerbsReverse(PitchToWord):
    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.update(
            PitchToWord({
                "link": Note("C", 3, 130.81),
                "holla": Note("D", 3, 146.83),
                "whippin": Note("E", 3, 164.81),
                "chirpin’": Note("F", 3, 174.61),
                "flexin’": Note("G", 3, 185),
                "catch-a-vibe": Note("A", 3, 220),
                "settle": Note("B", 3, 246.93),
                "run": Note("C", 4, 261.63),
                "skrrt": Note("D", 4, 293.66),
                "swerve": Note("E", 4, 329.63),
                "run up": Note("F", 4, 349.23),
                "chop": Note("G", 4, 369.99),
                "mash up": Note("A", 4, 440),
                "could": Note("B", 4, 493.88)
            })
        )

class ObjectsReverse(PitchToWord):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.update(
            PitchToWord({
                "gwop": Note("C", 3, 130.81),
                "piff": Note("D", 3, 146.83),
                "block": Note("E", 3, 164.81),
                "6ix": Note("F", 3, 174.61),
                "food": Note("G", 3, 185),
                "yute": Note("A", 3, 220),
                "slime": Note("B", 3, 246.93),
                "cheese": Note("C", 4, 261.63),
                "whip": Note("D", 4, 293.66),
                "g": Note("E", 4, 329.63),
                "ends": Note("F", 4, 349.23),
                "ting": Note("G", 4, 369.99),
                "drip": Note("A", 4, 440),
                "watah": Note("B", 4, 493.88)
            })
        )
        
class ClosersReverse(PitchToWord):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.update(
            PitchToWord({
                "deadass": Note("C", 3, 130.81),
                "no cap": Note("D", 3, 146.83),
                "facts": Note("E", 3, 164.81),
                "bless up": Note("F", 3, 174.61),
                "boom": Note("G", 3, 185),
                "safe": Note("A", 3, 220),
                "trust": Note("B", 3, 246.93),
                "on god": Note("C", 4, 261.63),
                "say less": Note("D", 4, 293.66),
                "you dun know": Note("E", 4, 329.63),
                "clapped": Note("F", 4, 349.23),
                "on job": Note("G", 4, 369.99),
                "bless up": Note("A", 4, 440),
                "safe": Note("B", 4, 493.88)
            })
        )
