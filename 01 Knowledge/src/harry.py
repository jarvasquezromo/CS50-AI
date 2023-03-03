from logic import *

# Propotisional logic
rain = Symbol("rain")               # It is raining
hagrid = Symbol("hagrid")           # Harry visited hagrid
dumbledore = Symbol("dumbledore")   # Harry visited dumbledore

knowledge = And(
    Implication(Not(rain), hagrid), # If it is not raining then harry visited hagrid
    Or(hagrid, dumbledore),         # Harry visited hagrid or dumbledore
    Not(And(hagrid, dumbledore)),   # Harry visited hagrid or dumbledore but not both
    dumbledore                      # We know harry visited dumbledore
)

# For see the formula likewe write on paper
print (knowledge.formula ())

#                | Information than i know
#                |         | the question, that i want to know
print(model_check(knowledge, rain))

# In every world when knowledge is true, rain is true
