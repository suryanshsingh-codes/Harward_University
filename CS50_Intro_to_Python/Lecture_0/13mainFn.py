# ==================================
# 🏫HARWARD UNIVERSITY : LECTURE 0
# ==================================

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