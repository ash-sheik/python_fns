# Python Function and List Exercises

This repository contains a set of Python exercises demonstrating the use of functions, list comprehensions, `eval`, prime number checking, and mapping functions to lists. These exercises are designed for beginners to practice fundamental Python concepts.

## Table of Contents

* [Exercise 1: Custom Function](#exercise-1-custom-function)
* [Exercise 2: Filter Strings by Length](#exercise-2-filter-strings-by-length)
* [Exercise 3: Evaluate Expression](#exercise-3-evaluate-expression)
* [Exercise 4: Prime Numbers](#exercise-4-prime-numbers)
* [Exercise 5: Convert Strings to Uppercase](#exercise-5-convert-strings-to-uppercase)

---

## Exercise 1: Custom Function

A Python function that performs addition or multiplication based on the number of arguments provided.

**Code Example:**

```python
def custom_function(arg1, arg2=10, arg3=None):
    if arg3 is None:
        print(f"The sum is: {arg1 + arg2}")
    else:
        print(f"The product is: {arg1 * arg2 * arg3}")

custom_function(10)
custom_function(5, 3)
custom_function(5, 3, 2)
```

**Output:**

```
The sum is: 20
The sum is: 8
The product is: 30
```

**Concepts Covered:**

* Default arguments
* Conditional logic
* Function calls with different numbers of arguments

---

## Exercise 2: Filter Strings by Length

Filters a list of strings and returns only those with 5 or more characters.

**Code Example:**

```python
def filter_strings(strings):
    return [s for s in strings if len(s) >= 5]

strings = ["honey", "cat", "cherry", "dog", "elephant"]
filtered = filter_strings(strings)
print(filtered)
```

**Output:**

```
['honey', 'cherry', 'elephant']
```

**Concepts Covered:**

* List comprehension
* Conditional filtering

---

## Exercise 3: Evaluate Expression

Evaluates a mathematical expression represented as a string using the `eval()` function.

**Code Example:**

```python
expression = "3 * 5 + 2"
result = eval(expression)
print(f"The result of the expression '{expression}' is: {result}")
```

**Output:**

```
The result of the expression '3 * 5 + 2' is: 17
```

**Concepts Covered:**

* String evaluation
* Arithmetic operations

---

## Exercise 4: Prime Numbers

Filters a list of numbers to find all prime numbers.

**Code Example:**

```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
prime_numbers = list(filter(is_prime, numbers))
print(prime_numbers)
```

**Output:**

```
[2, 3, 5, 7, 11]
```

**Concepts Covered:**

* Prime number checking
* `filter()` function
* Loops and conditionals

---

## Exercise 5: Convert Strings to Uppercase

Converts all strings in a list to uppercase using `map()` and `str.upper`.

**Code Example:**

```python
def to_uppercase(strings):
    return list(map(str.upper, strings))

strings = ["apple", "banana", "cherry"]
uppercase_strings = to_uppercase(strings)
print(uppercase_strings)
```

**Output:**

```
['APPLE', 'BANANA', 'CHERRY']
```

**Concepts Covered:**

* `map()` function
* String methods

---

## How to Run

1. Clone the repository:

```bash
git clone <your-repo-link>
```

2. Navigate to the project directory:

```bash
cd <project-directory>
```

3. Run the Python file:

```bash
python exercises.py
```

---

## Author

ASHIBA B
Beginner Python enthusiast practicing fundamental programming exercises.
