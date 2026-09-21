# ==================================
# 🏫 HARVARD UNIVERSITY : LECTURE 1
# ==================================

# ---------------------------------------------------------
# 13. PYTHONIC (TERNARY RETURN)
# ---------------------------------------------------------
print("-"*60)
print("13. PYTHONIC (TERNARY RETURN)")
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
    return True if n % 2 == 0 else False


main()