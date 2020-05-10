import math
import random
import time

# Character class to inherit from
class PC_character(object):

    def __init__(self, name, MAX_hp, base_speed, priority="Normal", mindset_multiplier=1.0, move=''):
     self.MAX_hp = MAX_hp
     self.base_hp = MAX_hp
     self.base_speed = base_speed
     self.priority = priority
     self.mindset_multiplier = mindset_multiplier
     self.name = name
     self.gold = gold
     self.health_potion = health_potion

     self.move_pool = {}

    def __repr__(self):
        return "{self.name} - {self.base_hp} / {self.MAX_hp} HP, {self.mindset_multiplier} mindset, {self.base_speed} speed".format(self=self)
# Movement class to inherit from
class Move(object):

    def __init__(self, description="", self_damage=0, damage=0, mindset_multiplier=1.0, opponent_mindset_multiplier=1.0, speed_boost=0, opponent_speed_boost=0, priority="Normal"):
        self.__doc__ = description
        self.self_damage = self_damage
        self.damage = damage
        self.mindset_multiplier = mindset_multiplier
        self.opponent_mindset_multiplier = opponent_mindset_multiplier
        self.speed_boost = speed_boost
        self.opponent_speed_boost = opponent_speed_boost
        self.priority = priority
        self.health_potion = health_potion
        self.gold = gold



    def __call__(self, attacker=None, opponent=None):
        if attacker is not None:
            attacker.priority = self.priority
            attacker.mindset_multiplier *= self.mindset_multiplier
            attacker.base_speed += self.speed_boost
            attacker.base_hp -= math.floor(self.self_damage *
                                           attacker.mindset_multiplier)
            attacker.base_hp = min(max(attacker.base_hp, 0), attacker.MAX_hp)

        if opponent is not None:
            opponent.mindset_multiplier *= self.opponent_mindset_multiplier
            opponent.base_speed += self.speed_boost
            opponent.base_hp -= math.floor(self.damage *
                                           attacker.mindset_multiplier)
            opponent.base_hp = min(max(opponent.base_hp, 0), opponent.MAX_hp)

# Classes
class Necromancer(PC_character):

    def __init__(self):
        PC_character.__init__(self, "Necromancer", 250, 75)
        self.move_pool = {"1": Move(" Chill Touch - A normal speed spell. A ghostly hand reaches out and touches the enemy!",
                                     damage=40),
                           "2": Move(" Vampiric Touch - A Normal speed spell. Absorbs 30 HP to the user.",
                                     damage=-30),
                           "3": Move(" Animate Dead - Raises a nearby corpse to fight for you!",
                                     mindset_multiplier=1.35)}# I need to find a way to add an Undead to team.

class Knight(PC_character):

    def __init__(self):
        PC_character.__init__(self, "Knight", 250, 75)
        self.move_pool = {"1": Move(" Thrust - A fast, light attack. Does 30 Basic Damage to Opponent",
                                    damage=30, priority="Fast"),
                          "2": Move(" Massive Swing - A Slow, strong attack. Does 65 Base Damage to Opponent and 30 Base Damage to User",
                                    self_damage=30, damage=65, priority="Slow"),
                          "3": Move(" Pray to the Light - Normal speed. Improves the Mindset of the User ( x 1.25 )",
                                    mindset_multiplier=1.25)}

class Undead(PC_character):

    def __init__(self):
        PC_character.__init__(self, "Undead", 250, 75)
        self.move_pool = {"1": Move(" Claw - A light attack. Does 10 Basic Damage to Opponent",
                                    damage=10),
                          "2": Move(" Bite - A light attack. Does 10 Basic Damage to Opponent",
                                    damage=10),
                          "3": Move(" Unholy Moan - An unnerving action, causes a bit of fear",
                                    mindset_multiplier=-1.25)}# Might have an issue with negative motifyer

class Villager(PC_character):

    def __init__(self):
        PC_character.__init__(self, "Villager", 250, 75)
        self.move_pool = {"1": Move(" Basic Attack - An untrained attack. Does 5 Basic Damage to Opponent",
                                    damage=5),
                          "2": Move(" Cries of Fear - Cries out for help. Has a chance to call for help.",
                                    mindset_multiplier=0.25)}# I need to find a way to summon a knight

# Combat System

class Combat(system):

    def __init__(self):
        PC_character
        


# Game yes/no or move inputs
yes_no = ["yes", "no"]
directions = ["left", "right", "forward", "backwards"]
# Introduction
name = input("What is your name, adventurer?\n")
print("Greetings, " + name + ". Let's start you on your journey!")
print("You find yourself on the edge of a dark forest.")
print("Before you lies the body of a villager, you feel power swelling in your hands, but a pulling darkness within.")

#Start of game
response = ""
while response not in yes_no:
    response = input("Will you raise the villager?\nyes/no\n")
    if response == "yes":
        print("Dark power surges from your hands as the villager moans and shuffles to his feet!\n")
        print("The undead villager awaits your commands!\n")
    elif response == "no":
        print("The body lays still and quiet. You let out a sigh of relief as the sun peers through the trees overhead.")
        quit()
    else:
        print("Reply yes or no!\n")

# Next part
response = ""
while response not in directions:
    print("To your left, you see more forest.")
    print("To your right, you see the shocked face of another villager!")
    print("In front of you stands your undead minion, awaiting your commands...")
    print("Behind you stands a large oak!")
    response = input("What direction will you move?\nleft/right/forward/backward\n")
    if response == "left":
        print("You turn and run deeper into the forest!\n")
        break
    elif response == "right":
        print("You turn and approach the villager with a look of pure ice\n")
        print("The villager looks back into your eyes with complete fear.")

        while response not in yes_no:
            response = input("Will you attack?\nyes/no")
            if response == "yes":
                print("You march forward, undead following closely... The villager screams as a knight emerges.\n")
                break
            elif response == "no":
                print("Before you get a chance to run, the villager screams, and her knight escort emerges from the brush!\n")
                break
            else:
                print("I didn't understand that.\n")
        # Start combat!
    elif response == "forward":
        print("You look at the creature and command it to devour the villager!\n")
        break
    elif response == "backward":
        print("You cannot scale the great tree!\n")
        response = ""
        break
    else:
        print("I didn't understand that.\n")

# Next part

print("You find yourself wondering, what's next?")