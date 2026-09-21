# ==================================
# 🏫 HARVARD UNIVERSITY : LECTURE 1
# ==================================

# ---------------------------------------------------------
# 8. AND OPERATOR (GRADE PROGRAM - v1)
# ---------------------------------------------------------
print("-"*60)
print("8. AND OPERATOR (GRADE PROGRAM - v1)")
print("-"*60)
print()

score = int(input("Score: "))
print()

print(f"Value of score : {score}")
print()

if score >= 90 and score <= 100:
    print("Grade: A")
elif score >= 80 and score < 90:
    print("Grade: B")
elif score >= 70 and score < 80:
    print("Grade: C")
elif score >= 60 and score < 70:
    print("Grade: D")
else:
    print("Grade: F")
print()