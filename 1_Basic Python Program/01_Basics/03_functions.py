# ============================================================
# Chapter 1 - Functions
# Topics: Basic functions, *args/**kwargs, nested functions,
#         closures, recursion, decorators (higher-order functions)
# ============================================================

# ── Basic Functions ─────────────────────────────────────────
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def div(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def mult(a, b):
    return a * b

# print(add(5, 6))
# print(sub(7, 3))
# print(div(6, 3))
# print(mult(7, 3))

# ── Find Max of 3 Numbers ───────────────────────────────────
def find_max(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

# print(find_max(5, 6, 7))

# ── **kwargs — Arbitrary Keyword Arguments ──────────────────
def check_key(key, **kwargs):
    check = kwargs.get(key)
    return 'Key exists' if check else 'Key does not exist'

# print(check_key('value', name="nepal", age=20))

def sum_number(**kwargs):
    return sum(kwargs.values())

# print(sum_number(a=15, b=25, c=90, d=30))

# ── Nested Functions ────────────────────────────────────────
def greet(name):
    def get_message():
        print(f"Hello {name}")
    return get_message()

# greet('Nepal')

# ── Closure — Max & Remove ──────────────────────────────────
def max_value():
    nums = [1, 2, 3, 4, 5]
    def remove_func():
        nonlocal nums
        m = max(nums)
        nums.remove(m)
        return m, nums
    return remove_func

# result = max_value()
# val_max, array = result()
# print(val_max, array)
# while len(array) > 0:
#     val_max, array = result()
#     print(val_max, array)

# ── Closure — Discount System ───────────────────────────────
def discount_parent():
    current_discount = 0.1

    def apply_discount(price):
        nonlocal current_discount
        return price * (1 - current_discount)

    def set_discount(discount_rate):
        nonlocal current_discount
        current_discount = discount_rate

    return apply_discount, set_discount

# apply_discount, set_discount = discount_parent()
# print(apply_discount(1000))
# set_discount(0.2)
# print(apply_discount(1000))

# ── Recursion ───────────────────────────────────────────────
def natural_num(n):
    if n == 1:
        return 1
    return n + natural_num(n - 1)

def fact(n):
    if n == 1 or n == 0:
        return 1
    return n * fact(n - 1)

def flatten_list(l, result_list=None):
    if result_list is None:
        result_list = []
    for i in l:
        if isinstance(i, list):
            flatten_list(i, result_list)
        else:
            result_list.append(i)
    return result_list

# example_list = [1, 2, [3, 4, [5, 25], 7], 8, 9, [10]]
# flat = flatten_list(example_list)
# print("Flattened:", flat)
# print("Max:", max(flat))

# ── Decorators (Higher-Order Functions) ─────────────────────
def divider_function(func_add):
    def child_function(a, b):
        if b == 0:
            return "Cannot divide by zero"
        return func_add(a, b)
    return child_function

@divider_function
def divide(a, b):
    return a / b

# print(divide(10, 5))
# print(divide(6, 0))

def age_validate(age_func):
    def child_func(age):
        if age < 18:
            return "You are not eligible for voting."
        return age_func(age)
    return child_func

@age_validate
def vot_age(age):
    return "You are eligible for voting."

# print(vot_age(40))

def is_admin(func):
    def child_function_admin(user):
        if not user.get('role'):
            return 'Role must be provided.'
        if user.get('role') != 'admin':
            return 'You are not authorized to access.'
        return func(user)
    return child_function_admin

@is_admin
def delete_database(user):
    return f"Authorized: {user.get('username')}. Database deleted."

# user = {'username': 'admin', 'password': 'password', 'role': 'admin'}
# print(delete_database(user))
