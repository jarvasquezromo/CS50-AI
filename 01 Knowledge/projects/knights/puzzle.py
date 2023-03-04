from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave." == And(AKnight, AKnave)
knowledge0 = And(
    Or(AKnight, AKnave),            # A it is knight or knave
    Not(And(AKnight, AKnave)),      # but not both

    # For the sentence
    Implication(And(AKnight, AKnave), AKnight),  # if the sentence is true, then is a knight
    Implication(Not(And(AKnight, AKnave)), AKnave) # if the sentence is not true, then is a knave
)

# Puzzle 1
# A says "We are both knaves." == And(AKnave, BKnave)
# B says nothing.
knowledge1 = And(
    # Estructure for A
    Or(AKnight, AKnave),            # A it is knight or knave
    Not(And(AKnight, AKnave)),      # but not both
    # Estructure for B
    Or(BKnight, BKnave),            # B it is knight or knave
    Not(And(BKnight, BKnave)),      # but not both

    # For the sentence
    Implication(And(AKnave, BKnave), AKnight),  # if the sentence is true, then is a knight
    Implication(Not(And(AKnave, BKnave)), AKnave) # if the sentence is not true, then is a knave
)

# Puzzle 2
# A says "We are the same kind." == Or(And(AKnight, BKnight), And(AKnave, BKnave))
sentenceA = Or(And(AKnight, BKnight), And(AKnave, BKnave))
# B says "We are of different kinds." == Or(And(AKnight, BKnave), And(AKnave, BKnight))
sentenceB = Or(And(AKnight, BKnave), And(AKnave, BKnight))
knowledge2 = And(
    # Estructure for A
    Or(AKnight, AKnave),            # A it is knight or knave
    Not(And(AKnight, AKnave)),      # but not both
    # Estructure for B
    Or(BKnight, BKnave),            # B it is knight or knave
    Not(And(BKnight, BKnave)),      # but not both
    
    # For the sentence: A says "We are the same kind."
    Implication(sentenceA, AKnight),  # if the sentence is true, then is a knight
    Implication(Not(sentenceA), AKnave), # if the sentence is not true, then is a knave
    # For the sentence: B says "We are of different kinds."
    Implication(sentenceB, BKnight),  # if the sentence is true, then is a knight
    Implication(Not(sentenceB), BKnave) # if the sentence is not true, then is a knave
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
sentenceA = Or(AKnight, AKnave)
# B says "A said 'I am a knave'."
sentenceB_0 = AKnave
# B says "C is a knave."
sentenceB_1 = CKnave
# C says "A is a knight."
sentenceC = AKnight
knowledge3 = And(
    # Estructure for A
    Or(AKnight, AKnave),            # A it is knight or knave
    Not(And(AKnight, AKnave)),      # but not both
    # Estructure for B
    Or(BKnight, BKnave),            # B it is knight or knave
    Not(And(BKnight, BKnave)),      # but not both
    # Estructure for C
    Or(CKnight, CKnave),            # C it is knight or knave
    Not(And(CKnight, CKnave)),      # but not both

    # For the sentence: "I am a knight." or "I am a knave."
    Implication(sentenceA, AKnight),  # if the sentence is true, then is a knight
    Implication(Not(sentenceA), AKnave), # if the sentence is not true, then is a knave
    # For the sentence: B says "A said 'I am a knave'."
    Implication(sentenceB_0, BKnight),  # if the sentence is true, then is a knight
    Implication(Not(sentenceB_0), BKnave), # if the sentence is not true, then is a knave
    # For the sentence: B says "C is a knave."
    Implication(sentenceB_1, BKnight),  # if the sentence is true, then is a knight
    Implication(Not(sentenceB_1), BKnave), # if the sentence is not true, then is a knave
    # For the sentence: C says "A is a knight."
    Implication(sentenceC, CKnight),  # if the sentence is true, then is a knight
    Implication(Not(sentenceC), CKnave) # if the sentence is not true, then is a knave
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")
                # else: 
                #     print (f"No solution for {symbol}")


if __name__ == "__main__":
    main()
