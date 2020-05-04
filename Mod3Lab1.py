"""
CTEC 121
Caleb Howard
Module 3 Lab 1
<assignment/lab description
"""

""" IPO template
Input(s): list/description
Process: description of what function does
Output: return value and description
"""

def main():
    # literal
    print("\nBoolean literals")
    print(True)
    print(False)
    print(type(True))
    print()

    # relational operators 
    print("Relational operators")
    print("3 < 5", 3 < 5)
    print("3 <= 3", 3 <= 3)
    print("3 == 3", 3 == 3)
    print("3 >= 5", 3 >= 5)
    print("3 != 5", 3 != 5)
    print()

    # using variables
    x = 3
    y = 5
    print("Using Variables")
    print("x:", x, "y:", y)
    print("x < y", x < y)
    print("x != y", x != y)
    print()

    # simple if statements
    print("x:", x, "y:", y)
    if x < y:
        print("x < y")

    if x > y:
        print("x > y")

    print("end simple if example")
    print()

    # if/else statement
    print("if/else statement")
    print("x:", x, "y:", y)
    if x < y:
        print("x < y")
    else:
        print("x >= y")

    x = 6
    print("x:", x, "y:", y)
    if x < y:
        print("x < y")
    else:
        print("x >= y")

    print("end if/else example")
    print()

    # exercise 3-1
    # followed what Professor did since I still struggle with the range stuff
    
    print("Exercise")
    for i in range(1,11):
        if (i % 2) == 0:
            outputString = "even"
        else:
            outputString = "odd"
        print(i, outputString)
    print()

    # alphabetize names
    name = "Caleb"
    firstLetterOfName = "C"

    print("Multi-way if example")
    if firstLetterOfName == "A":
        print(name)
    elif firstLetterOfName == "B":
        print(name)
    elif firstLetterOfName == "C":
        print(name)
    # ...
    elif firstLetterOfName == "Y":
        print(name)
    else:
        print(name)
    print()

main()    