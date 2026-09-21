# ==================================
# 🏫 HARVARD UNIVERSITY : LECTURE 1
# ==================================

# ---------------------------------------------------------
# 18. HOGWARTS (MATCH WITH | — BEST)
# ---------------------------------------------------------
print("-"*60)
print("18. HOGWARTS (MATCH WITH | — BEST)")
print("-"*60)
print()

name = input("What's your name? ")
print()

print(f"Value of name : {name}")
print()

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
print()