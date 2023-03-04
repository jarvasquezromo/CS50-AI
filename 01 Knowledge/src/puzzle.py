from logic import *

people = ["Gilderoy", "Pomona", "Minerva", "Horace"]
houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

symbols = []

knowledge = And()

# Make a symbol for each option
for person in people:
    for house in houses:
        symbols.append(Symbol(f"{person}{house}"))

# Each person belongs to a house.
for person in people:
    knowledge.add(Or(
        Symbol(f"{person}Gryffindor"),
        Symbol(f"{person}Hufflepuff"),
        Symbol(f"{person}Ravenclaw"),
        Symbol(f"{person}Slytherin")
    ))
# Al parecer no es necesario agregar los simbolos ya creados porque como 
# se instancian de la misma fora, entonces son iguales

# Only one house per person.
for person in people:
    for h1 in houses:
        for h2 in houses:
            if h1 != h2:
                knowledge.add(
                    Implication(Symbol(f"{person}{h1}"), Not(Symbol(f"{person}{h2}")))
                )

# Only one person per house.
for house in houses:
    for p1 in people:
        for p2 in people:
            if p1 != p2:
                knowledge.add(
                    Implication(Symbol(f"{p1}{house}"), Not(Symbol(f"{p2}{house}")))
                )

# print (knowledge.formula ())

# We like to add new information
# Gilderoy on gryffindor or ravenclaw
knowledge.add(
    Or(Symbol("GilderoyGryffindor"), Symbol("GilderoyRavenclaw"))
)

# Pomona not in slytherin
knowledge.add(
    Not(Symbol("PomonaSlytherin"))
)

# Minerva on gryffindor
knowledge.add(
    Symbol("MinervaGryffindor")
)

for symbol in symbols:
    if model_check(knowledge, symbol):
        print(symbol)
