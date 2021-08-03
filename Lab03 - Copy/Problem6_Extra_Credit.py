from functools import reduce

items = []
get_in = int(input("Enter an integer:"))
[items.append(i) for i in range(1, get_in + 1)]
squared = list(map(lambda x: x ** 2, items))
product = reduce((lambda x, y: x + y), squared)

print(f"The sum of the square of {items} is {product}")
