# ==================================
# 🏫HARWARD UNIVERSITY : LECTURE 0
# ==================================


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