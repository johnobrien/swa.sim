#! /usr/bin/python3

"""Provides classes and methods to simulate squadron battles in Star Wars Armada.

Each squadron will have hull and be able to roll for attack.
"""

from random import choice


# Die faces if undefined are blank
class Face:
    def __init__(self, color, hits=0, crits=0, accuracies=0):
        self.color = color
        self.hits = hits
        self.crits = crits
        self.accuracies = accuracies

    def __repr__(self):
        return f'color={self.color}, hits={self.hits}, crits={self.crits}, accuracies={self.accuracies}'


red = (Face("red", hits=1),
       Face("red", hits=1),
       Face("red", crits=1),
       Face("red", crits=1),
       Face("red", accuracies=1),
       Face("red", hits=2),
       Face("red", hits=1),
       Face("red", crits=1),
       Face("red"),
       Face("red"))
blue = (Face("blue", hits=1),
        Face("blue", hits=1),
        Face("blue", hits=1),
        Face("blue", hits=1),
        Face("blue", crits=1),
        Face("blue", crits=1),
        Face("blue", accuracies=1),
        Face("blue", accuracies=1))
black = (Face("black", hits=1),
         Face("black", hits=1),
         Face("black", hits=1),
         Face("black", hits=1),
         Face("black", hits=1, crits=1),
         Face("black", hits=1, crits=1),
         Face("black"),
         Face("black"))

faces = {"red": red,
         "blue": blue,
         "black": black}


# After creating a Die with d1 = Die("red", red), d1.roll will return a Face

class Die:
    """A single attack die"""
    def __init__(self, color, die_faces):
        self.color = color
        self.faces = die_faces

    @property
    def roll(self):
        return choice(self.faces)


class Squadron:
    """The parent class for all squadrons."""
    def __init__(self, model, hull, dice_colors):
        self.kind = model
        self.hull = hull
        self.dice = []
        for die_color in dice_colors:
            self.dice.append(Die(die_color, faces[die_color]))

    @property
    def roll(self, dice=None):
        # Roll all the die and return the result
        attack = []
        # Can pass in dice to roll. Default is to roll all dice.
        if dice is None:
            dice = self.dice
        for die in dice:
            result = die.roll
            attack.append(result)
        return attack

    def defend(self, attack):
        # Given at attack from an enemy wing, the squadron defends itself, or takes damage.
        pass

class TieFighter(Squadron):
    """Tie fighter squadron, implementing Swarm. For now, until I can figure out how to
    have the definition of the 'worst' die vary by the opponent, I will just re-roll the
    first result that did not result in a hit."""
    def __init__(self):
        super(TieFighter, self).__init__(model="TIE Fighter Squadron", hull=3, dice_colors=["blue", "blue", "blue"])

    def roll(self, dice=None, wing=None):
        # Use the parent method to start.
        attack = super().roll
        if len(wing) > 1:
            # The enemy is engaged by two fighters, so we can use swarm.
            for i, result in enumerate(attack):
                if result.hits is 0:
                    # re-roll this, then stop
                    new_color = result.color
                    del attack[i]
                    new_die = Die(new_color, faces[new_color])
                    attack.insert(i, new_die.roll)
                    break
        return attack

class Xwing(Squadron):
    """X-wings have escort. I will need to figure how to model that."""
    def __init__(self):
        super(Xwing, self).__init__(model="X-wing Squadron   ", hull=5, dice_colors=["blue", "blue", "blue", "blue"])

    def roll(self, dice=None, wing=None):
        attack = super().roll
        return attack


class Wing:
    """A wing is composed of one or more squadrons."""
    def __init__(self, squadrons):
        self.squadrons = squadrons

    def attack(enemy_wing):
        """Given an enemy wing, selects a squadron to attack in the enemy wing."""
        targets = sorted(enemy_wing, key=lambda x: x.hull, reverse=True)


if __name__ == "__main__":
    t1 = TieFighter()
    t2 = TieFighter()
    imperial_wing = [t1, t2]
    print(t1.roll(wing=imperial_wing))
    print(t2.roll(wing=imperial_wing))

    x1 = Xwing()
    rebel_wing = [x1]
    print(x1.roll(wing=rebel_wing))
