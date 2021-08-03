lst = []
lst_vowels = []
vowels = ['a', 'e', 'i', 'o', 'u']

get_in = str(input("Enter a string:"))
[lst.append(i) for i in get_in]
[lst_vowels.append(i.upper()) for i in lst for x in vowels if x.lower() == i.lower()]

print(f"chars are {lst}")
print(f"The entered string is {get_in} and the result to convert a vowels to uppercase is \n {lst_vowels}")
