# ============================================================
# Loops - For Loop
# Topics: break, continue, searching in list, voter age check
# ============================================================

# ── Break: Search in List ───────────────────────────────────
a = [2, 3, 1, 5, 9, 8]
search_num = 1
for element in a:
    if element == search_num:
        print("Element found")
        break

# ── Continue: Voter ID Generation ──────────────────────────
voters_age = [18, 19, 20, 21, 22, 23, 24]
for age in voters_age:
    if age >= 18:
        print("Voter ID is being generated")
        continue
    print("Not a voter")
    remaining_age = 18 - age
    print(f'{remaining_age} years remaining')
