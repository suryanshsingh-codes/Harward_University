# ==================================
# 🏫 HARVARD UNIVERSITY : LECTURE 1
# ==================================

# ---------------------------------------------------------
# 9. CHAINED COMPARISON (PYTHONIC)
# ---------------------------------------------------------
print("-"*60)
print("9. CHAINED COMPARISON (PYTHONIC)")
print("-"*60)
print()

score = int(input("Score: "))
print()

print(f"Value of score : {score}")
print()

if 90 <= score <= 100:
    print("Grade: A")
elif 80 <= score < 90:
    print("Grade: B")
elif 70 <= score < 80:
    print("Grade: C")
elif 60 <= score < 70:
    print("Grade: D")
else:
    print("Grade: F")
print()