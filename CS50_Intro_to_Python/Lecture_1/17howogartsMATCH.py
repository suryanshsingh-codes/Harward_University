# ==================================
# 🏫 HARVARD UNIVERSITY : LECTURE 1
# ==================================

# ---------------------------------------------------------
# 17. HOGWARTS (MATCH / CASE VERSION)
# ---------------------------------------------------------
print("-"*60)
print("17. HOGWARTS (MATCH / CASE VERSION)")
print("-"*60)
print()

name = input("What's your name? ")
print()

print(f"Value of name : {name}")
print()

match name:
    case "Harry":
        print("Gryffindor")
    case "Hermione":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
print()