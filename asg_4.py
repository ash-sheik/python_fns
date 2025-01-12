#exercise 1
def custom_function(arg1, arg2=10, arg3=None):
    if arg3 is None:
        print(f"The sum is: {arg1 + arg2}")
    else:
        print(f"The product is: {arg1 * arg2 * arg3}")

custom_function(10)
custom_function(5, 3)
custom_function(5, 3, 2)

#exercise 2

def filter_strings(strings):
    return [s for s in strings if len(s) >= 5]


strings = ["honey", "cat", "cherry", "dog", "elephant"]
filtered = filter_strings(strings)
print(filtered)

#exercise 3
expression = "3 * 5 + 2"
result = eval(expression)
print(f"The result of the expression '{expression}' is: {result}")

#exercise 4
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

#exercise 5
def to_uppercase(strings):
    return list(map(str.upper, strings))


strings = ["apple", "banana", "cherry"]
uppercase_strings = to_uppercase(strings)
print(uppercase_strings)