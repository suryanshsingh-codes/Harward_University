# ==================================
# 🏫HARWARD UNIVERSITY : LECTURE 0
# ==================================


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
