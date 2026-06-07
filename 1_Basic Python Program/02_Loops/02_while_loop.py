# ============================================================
# Loops - While Loop
# Topics: basic while loop, while True, number guessing game
# ============================================================

# ── Basic While Loop ────────────────────────────────────────
number = 0
while number < 10:
    print(number)
    number += 1

# ── While True: Sum Input ───────────────────────────────────
# while True:
#     number1 = int(input("Enter a number: "))
#     number2 = int(input("Enter a number: "))
#     print(number1 + number2)

# ── Number Guessing Game ─────────────────────────────────────
stored_num = 10
print("\n-- Guess the Number Game (1 to 10) --")
while True:
    number1 = int(input("Enter a number between 1 to 10: "))
    if number1 == stored_num:
        print("Number found!")
        break
    elif number1 < stored_num:
        print("Too low, try again.")
    else:
        print("Too high, try again.")
