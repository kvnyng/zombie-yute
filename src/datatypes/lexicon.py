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
                "Whazzgood": Note("C", 3, 130.81),
                "Hol’up": Note("D", 3, 146.83),
                "Yo": Note("E", 3, 164.81),
                "Nah-fam": Note("F", 3, 174.61),
                "Straight-up": Note("G", 3, 185),
                "Real talk": Note("A", 3, 220),
                "Wagwan": Note("B", 3, 246.93),
                "We out here": Note("C", 4, 261.63),
                "Slime": Note("D", 4, 293.66)
            })
        )

class SubjectsReverse(PitchToWord):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.update(
            PitchToWord({
                "Fam": Note("C", 3, 130.81),
                "Big Man": Note("D", 3, 146.83),
                "Mandem": Note("E", 3, 164.81),
                "Bredrin": Note("F", 3, 174.61),
                "Plug": Note("G", 3, 185),
                "Ting": Note("A", 3, 220),
                "Galdem": Note("B", 3, 246.93),
                "Ends": Note("C", 4, 261.63),
                "Whip": Note("D", 4, 293.66),
                "Cheese": Note("E", 4, 329.63),
                "Drip": Note("F", 4, 349.23),
                "Water": Note("G", 4, 369.99),
                "Brains": Note("A", 4, 440),
                "We": Note("B", 4, 493.88)
            })
        )

class VerbsReverse(PitchToWord):
    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.update(
            PitchToWord({
                "Link": Note("C", 3, 130.81),
                "Holla": Note("D", 3, 146.83),
                "Whippin": Note("E", 3, 164.81),
                "Chirpin’": Note("F", 3, 174.61),
                "Flexin’": Note("G", 3, 185),
                "Catch-a-vibe": Note("A", 3, 220),
                "Settle": Note("B", 3, 246.93),
                "Run": Note("C", 4, 261.63),
                "Skrrt": Note("D", 4, 293.66),
                "Swerve": Note("E", 4, 329.63),
                "Run up": Note("F", 4, 349.23),
                "Chop": Note("G", 4, 369.99),
                "Mash up": Note("A", 4, 440),
                "Could": Note("B", 4, 493.88)
            })
        )

class ObjectsReverse(PitchToWord):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.update(
            PitchToWord({
                "Gwop": Note("C", 3, 130.81),
                "Piff": Note("D", 3, 146.83),
                "Block": Note("E", 3, 164.81),
                "6ix": Note("F", 3, 174.61),
                "Food": Note("G", 3, 185),
                "Yute": Note("A", 3, 220),
                "Slime": Note("B", 3, 246.93),
                "Cheese": Note("C", 4, 261.63),
                "Whip": Note("D", 4, 293.66),
                "G": Note("E", 4, 329.63),
                "Ends": Note("F", 4, 349.23),
                "Ting": Note("G", 4, 369.99),
                "Drip": Note("A", 4, 440),
                "Watah": Note("B", 4, 493.88)
            })
        )
        
class ClosersReverse(PitchToWord):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.update(
            PitchToWord({
                "Deadass": Note("C", 3, 130.81),
                "No cap": Note("D", 3, 146.83),
                "Facts": Note("E", 3, 164.81),
                "Bless up": Note("F", 3, 174.61),
                "Boom": Note("G", 3, 185),
                "Safe": Note("A", 3, 220),
                "Trust": Note("B", 3, 246.93),
                "On god": Note("C", 4, 261.63),
                "Say less": Note("D", 4, 293.66),
                "You dun know": Note("E", 4, 329.63),
                "Clapped": Note("F", 4, 349.23),
                "On job": Note("G", 4, 369.99),
                "Bless up": Note("A", 4, 440),
                "Safe": Note("B", 4, 493.88)
            })
        )
