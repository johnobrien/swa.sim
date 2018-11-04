#! /usr/bin/python3

class Die:
    def __init__(self, color):
        self.color = color

    def roll(self):
        pass


class Squadron:
    """The parent class for all squadrons."""
    name = None

    def roll(self):
        pass


class Wing:
    """A group of one or two squadrons."""
    pass
