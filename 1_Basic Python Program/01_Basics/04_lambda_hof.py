# ============================================================
# Chapter 1 - Lambda & Higher-Order Functions (map, filter)
# Topics: Lambda syntax, map(), filter(), built-in HOF
# ============================================================

# ── Lambda Basics ───────────────────────────────────────────
result  = lambda x, y: x + y
square  = lambda x: x * x
cube    = lambda x: x ** 3
even_odd = lambda x: 'even' if x % 2 == 0 else 'odd'
greater  = lambda a, b: a if a > b else b
greatest = lambda a, b, c: a if (a > b and a > c) else (b if (b > a and b > c) else c)

# print(result(10, 20))
# print(square(10))
# print(cube(10))
# print(even_odd(10))
# print(greater(10, 20))
# print(greatest(100, 20, 30))

# ── map() ───────────────────────────────────────────────────
listing = [1, 2, 3, 4, 5]
cubed_list = list(map(lambda x: x ** 3, listing))
# print(cubed_list)

names = ['Ram', 'Shyam', 'Gopal', 'Sita']
name_lengths = list(map(lambda x: len(x), names))
# print(name_lengths)

celsius = [34, 67, 89, 50]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
# print(fahrenheit)

# ── filter() ────────────────────────────────────────────────
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# print(even_numbers)
