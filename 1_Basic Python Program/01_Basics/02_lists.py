# ============================================================
# Chapter 1 - Lists
# Topics: List creation, append, insert, pop, sort,
#         reverse, remove — from sample.py
# ============================================================

# --- String input methods (from earlier practice) ---
# name = str(input("Enter your name and address: "))
# print("Length:", len(name))
# print(name.upper())
# print(name.capitalize())
# print(name.count("a"))
# print(name.find("ram"))
# print(name.endswith("lal"))

# --- List Operations ---
lists = ["Ram", "Shyam", "Cat", 5, 7, 30.2, "Hello"]
print("Original list:", lists)

lists.append("Yaman Gautam")
print("After append:", lists)

lists.insert(4, "Apple")
print("After insert:", lists)

lists.pop(3)
print("After pop:", lists)

l1 = [5, 2, 7, 0, 10, 50, 23, 67]
l1.sort()
print("After sort:", l1)

l1.reverse()
print("After reverse:", l1)

l1.remove(50)
print("After remove:", l1)
