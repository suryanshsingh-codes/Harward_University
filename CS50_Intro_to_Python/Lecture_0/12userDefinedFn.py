# ==================================
# 🏫HARWARD UNIVERSITY : LECTURE 0
# ==================================


# ===================================================================
# 12. DEF : CREATING OUR OWN FUNCTION
# ===================================================================
print("="*64)
print("DEF : CREATING OUR OWN FUNCTION")
print("="*64)
print()

# --------------------------------------------------
# Step 1 : simple function, no parameter
# --------------------------------------------------
def hello():
    print("hello")

name = input("What's your name? ")
hello()
print(name)

print()

# --------------------------------------------------
# Step 2 : function with parameter
# --------------------------------------------------
def hello(to):
    print("hello,", to)

name = input("What's your name? ")
hello(name)

print()

# --------------------------------------------------
# Step 3 : function with default value
# --------------------------------------------------
def hello(to="world"):
    print("hello,", to)

name = input("What's your name? ")
hello(name)
hello()          
# uses default "world"

print()