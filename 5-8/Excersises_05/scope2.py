## Scope Excersise 3 - Write a function to search for an even number in a list of numbers...

numbers = [1, 3, 5, 7, 8, 9]

def has_even_number(numbers):
    for number in numbers:
        if number % 2 == 0:
            return True
    return False

result = has_even_number(numbers)
print(result) 