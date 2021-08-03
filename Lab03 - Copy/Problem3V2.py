get_in = str(input("Enter a string:"))
lst = []
vowels = ['a', 'e', 'i', 'o', 'u']
lst_vowels = []
for i in get_in:
    lst.append(i)
for i in lst:
    for x in vowels:
        if x == i:
            lst_vowels.append(i.upper())
print(lst_vowels)
print(lst)
