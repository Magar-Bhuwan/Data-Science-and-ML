# ============================================================
# Loops - Problem: Combination Sum
# Topics: itertools.combinations, finding subset that matches sum
# ============================================================
from itertools import combinations

sum_value = 12
listing = [5, 4, 11, 9, 3]
result = None

for r in range(1, len(listing) + 1):
    for combo in combinations(listing, r):
        if sum(combo) == sum_value:
            result = list(combo)
            break
    if result:
        break

print("Combination that sums to", sum_value, ":", result)
