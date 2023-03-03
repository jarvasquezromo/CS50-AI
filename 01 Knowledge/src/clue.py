import termcolor

from logic import *

mustard = Symbol("ColMustard")
plum = Symbol("ProfPlum")
scarlet = Symbol("MsScarlet")
characters = [mustard, plum, scarlet]

ballroom = Symbol("ballroom")
kitchen = Symbol("kitchen")
library = Symbol("library")
rooms = [ballroom, kitchen, library]

knife = Symbol("knife")
revolver = Symbol("revolver")
wrench = Symbol("wrench")
weapons = [knife, revolver, wrench]

symbols = characters + rooms + weapons


def check_knowledge(knowledge):
    for symbol in symbols:
        if model_check(knowledge, symbol):
            termcolor.cprint(f"{symbol}: YES", "green")
        elif not model_check(knowledge, Not(symbol)):
            print(f"{symbol}: MAYBE")


# There must be a person, room, and weapon.
knowledge = And(
    Or(mustard, plum, scarlet),         # one of the characters must be the murderer
    Or(ballroom, kitchen, library),
    Or(knife, revolver, wrench)
)

# Initial cards (adding to aditional knowledege)
knowledge.add(And(
    Not(mustard), Not(kitchen), Not(revolver)
))

# A card was be reveld (revelado?) 
# Unknown card
knowledge.add(Or(
    Not(scarlet), Not(library), Not(wrench)
))

# Known cards
knowledge.add(Not(plum))        # I saw the profesor plum
knowledge.add(Not(ballroom))

check_knowledge(knowledge)
