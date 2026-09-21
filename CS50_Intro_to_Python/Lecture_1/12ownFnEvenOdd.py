# ==================================
# 🏫 HARVARD UNIVERSITY : LECTURE 1
# ==================================

# ---------------------------------------------------------
# 12. OWN PARITY FUNCTION
# ---------------------------------------------------------
print("-"*60)
print("12. OWN PARITY FUNCTION")
print("-"*60)
print()

def main():
    x = int(input("What's x? "))
    print()
    print(f"Value of x : {x}")
    print()

    if is_even(x):
        print("Even")
    else:
        print("Odd")
    print()


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


main()