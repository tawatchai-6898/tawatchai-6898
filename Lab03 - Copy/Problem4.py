vowels = ['a', 'e', 'i', 'o', 'u']

get_in = str(input("Enter a string:"))
lst = list(map(str, get_in))
result = [x.upper() for i in get_in for x in vowels if x.lower() == i.lower()]


print(f"Character in the string are {result}")
print(f"The entered string is {get_in} and the result to convert a vowels to uppercase is \n {result}")