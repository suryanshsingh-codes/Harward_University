# ==================================
# 🏫HARWARD UNIVERSITY : LECTURE 0
# ==================================

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