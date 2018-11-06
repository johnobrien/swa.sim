#! /usr/bin/python3

"""Provides classes and methods to simulate squadron battles in Star Wars Armada.

Each squadron will have hull and be able to roll for attack.
"""

from random import choice


# Die faces if undefined are blank
class Face:
    def __init__(self, hits=0, crits=0, accuracies=0):
        self.hits = hits
        self.crits = crits
        self.accuracies = accuracies

    def __repr__(self):
        return f'hits={self.hits}, crits={self.crits}, accuracies={self.accuracies}'


red = (Face(hits=1),
       Face(hits=1),
       Face(crits=1),
       Face(crits=1),
       Face(accuracies=1),
       Face(hits=2),
       Face(hits=1),
       Face(crits=1),
       Face(),
       Face())
blue = (Face(hits=1),
        Face(hits=1),
        Face(hits=1),
        Face(hits=1),
        Face(crits=1),
        Face(crits=1),
        Face(accuracies=1),
        Face(accuracies=1))
black = (Face(hits=1),
         Face(hits=1),
         Face(hits=1),
         Face(hits=1),
         Face(hits=1, crits=1),
         Face(hits=1, crits=1),
         Face(),
         Face())


# After creating a Die with d1 = Die("red", red), d1.roll will return a Face
class Die:
    """A single attack die"""
    def __init__(self, color, faces):
        self.color = color
        self.faces = faces

    @property
    def roll(self):
        return choice(self.faces)


class Squadron:
    """The parent class for all squadrons."""
    def __init__(self, model, dice):
        self.kind = model
        self.dice = dice

    def roll(self):
        # Roll all the die and return the result
        pass


class Wing:
    """A group of one or two squadrons."""
    def __init__(self):
        pass


if __name__ == "__main__":
    t1 = Squadron(model="TIE", dice=["blue", "blue", "blue", "blue"])
    t1.roll()
