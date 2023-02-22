### Task 1

add15 = lambda x: x + 15

print(add15(1))
print(add15(-2))

### Task 2

isOdd = lambda num: num % 2 != 0
isEven = lambda num: num % 2 == 0
getParity = lambda num, str: True if (str == 'odd' and num % 2 != 0) or (str == 'even' and num % 2 == 0) else False

print("############################################################################")
print(isOdd(2), isEven(2))
print(isOdd(1), isEven(1))
print(getParity(2, 'odd'), getParity(2, 'even'))
print(getParity(1, 'odd'), getParity(1, 'even'))

### Task 3

starts_with_p = lambda str: True if str[0].lower() == 'p' else False 

print("############################################################################")
print(starts_with_p("Python"))
print(starts_with_p("JavaScript"))
print(starts_with_p("pirate"))

### Task 4

numbers = [2, 4, 5, 7, 9, 14]
factor = 2

multiply = map(lambda number: number * factor, numbers)

print("############################################################################")
print(list(multiply))