# ==================================
# 🏫HARWARD UNIVERSITY : LECTURE 0
# ==================================


# ===================================================================
# 1. HELLO WORLD : The First Program
# ===================================================================
print("="*64)
print("PRINT : HELLO WORLD")
print("="*64)
print()

print("hello, world")    
# print() function takes "hello, world" as argument
print()

# ===================================================================
# 2. INPUT + VARIABLES
# ===================================================================
print("="*64)
print("INPUT + VARIABLES")
print("="*64)
print()

# --------------------------------------------------
# Taking input and storing in a variable
# --------------------------------------------------
name = input("What's your name? ")    
# input() returns a string


# --------------------------------------------------
# Printing using the variable
# --------------------------------------------------
print("hello, name")     
# ❌ this prints literally "hello, name"
print("hello,", name)    
# ✅ this prints "hello, David"

print()


# ===================================================================
# 4. STRING CONCATENATION vs COMMA
# ===================================================================
print("="*64)
print("STRING CONCATENATION vs COMMA")
print("="*64)
print()

name = input("What's your name? ")

# --------------------------------------------------
# Using + ( concatenation )
# --------------------------------------------------
print("hello, " + name)

# --------------------------------------------------
# Using , ( multiple arguments )
# --------------------------------------------------
print("hello,", name)

print()


# ===================================================================
# 5. END PARAMETER
# ===================================================================
print("="*64)
print("END PARAMETER")
print("="*64)
print()

name = input("What's your name? ")

# --------------------------------------------------
# Default : end = "\n" ( new line after print )
# --------------------------------------------------
print("hello,")
print(name)

print()

# --------------------------------------------------
# Override : end = "" ( no new line )
# --------------------------------------------------
print("hello,", end="")
print(name)

print()


# ===================================================================
# 6. QUOTATION MARKS PROBLEM
# ===================================================================
print("="*64)
print("QUOTATION MARKS PROBLEM")
print("="*64)
print()

# --------------------------------------------------
# Wrong way : double quotes inside double quotes
# --------------------------------------------------
# print("hello,"friend"")    # ❌ ERROR

# --------------------------------------------------
# Way 1 : use single quotes
# --------------------------------------------------
print('hello, "friend"')

# --------------------------------------------------
# Way 2 : use backslash escape
# --------------------------------------------------
print("hello, \"friend\"")

print()


# ===================================================================
# 7. F-STRINGS : the elegant way
# ===================================================================
print("="*64)
print("F-STRINGS")
print("="*64)
print()

name = input("What's your name? ")

# f-string : variable directly inside { }
print(f"hello, {name}")

print()


# ===================================================================
# 8. STRING METHODS : strip() + title()
# ===================================================================
print("="*64)
print("STRING METHODS : strip() + title()")
print("="*64)
print()

# --------------------------------------------------
# Step by step
# --------------------------------------------------
name = input("What's your name? ")
name = name.strip()     
# remove whitespace from left and right
name = name.title()     
# capitalize first letter of each word
print(f"hello, {name}")

print()

# --------------------------------------------------
# Chained : strip().title()
# --------------------------------------------------
name = input("What's your name? ").strip().title()
print(f"hello, {name}")

print()


# ===================================================================
# 9. INTEGERS / INT
# ===================================================================
print("="*64)
print("INTEGERS / INT")
print("="*64)
print()

# --------------------------------------------------
# Simple addition
# --------------------------------------------------
x = 1
y = 2
z = x + y
print("z =", z)

print()

# --------------------------------------------------
# Without int() : concatenation happens
# --------------------------------------------------
x = input("What's x? ")
y = input("What's y? ")
z = x + y
print("z =", z)    
# ❌ "12" instead of 3

print()

# --------------------------------------------------
# With int() : casting
# --------------------------------------------------
x = int(input("What's x? "))
y = int(input("What's y? "))
print("x + y =", x + y)

print()


# ===================================================================
# 10. FLOAT BASICS
# ===================================================================
print("="*64)
print("FLOAT BASICS")
print("="*64)
print()

# --------------------------------------------------
# Float input
# --------------------------------------------------
x = float(input("What's x? "))
y = float(input("What's y? "))
print("x + y =", x + y)

print()

# --------------------------------------------------
# round() to nearest integer
# --------------------------------------------------
x = float(input("What's x? "))
y = float(input("What's y? "))
z = round(x + y)
print("rounded z =", z)

print()

# --------------------------------------------------
# round( z , 2 ) : two decimal places
# --------------------------------------------------
x = float(input("What's x? "))
y = float(input("What's y? "))
z = round(x / y, 2)
print("z =", z)

print()

# --------------------------------------------------
# Format with commas : {z:,}
# --------------------------------------------------
x = float(input("What's x? "))
y = float(input("What's y? "))
z = round(x + y)
print(f"{z:,}")

print()

# --------------------------------------------------
# f-string : {z:.2f}
# --------------------------------------------------
x = float(input("What's x? "))
y = float(input("What's y? "))
z = x / y
print(f"{z:.2f}")

print()




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


# ===================================================================
# 13. MAIN FUNCTION
# ===================================================================
print("="*64)
print("MAIN FUNCTION")
print("="*64)
print()

def main():
    # Output using our own function
    name = input("What's your name? ")
    hello(name)

    # Output without passing the expected arguments
    hello()


def hello(to="world"):
    print("hello,", to)


main()    
# ← this line brings the program to life

print()


# ===================================================================
# 14. RETURNING VALUES
# ===================================================================
print("="*64)
print("RETURNING VALUES")
print("="*64)
print()

def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    return n * n      
# return back to main


main()

print()