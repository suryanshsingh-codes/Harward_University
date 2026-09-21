# ==================================
# 🏫 HARVARD UNIVERSITY : LECTURE 1
# ==================================

# ---------------------------------------------------------
# 4. ELSE (CATCH-ALL)
# ---------------------------------------------------------
print("-"*60)
print("4. ELSE (CATCH-ALL)")
print("-"*60)
print()

x = int(input("What's x? "))
y = int(input("What's y? "))
print()

print(f"Value of x : {x}")
print(f"Value of y : {y}")
print()

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")
print()