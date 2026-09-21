# ==================================
# 🏫 HARVARD UNIVERSITY : LECTURE 1
# ==================================

# ---------------------------------------------------------
# 14. MOST PYTHONIC (DIRECT RETURN)
# ---------------------------------------------------------
print("-"*60)
print("14. MOST PYTHONIC (DIRECT RETURN)")
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
    return n % 2 == 0


main()