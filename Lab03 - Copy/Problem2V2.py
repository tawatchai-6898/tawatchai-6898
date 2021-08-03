fruits_list = ["Grapefruit", "Longan", "Orange", "Apple", "Cherry"]
print(f"The fruits are {fruits_list} \nAfter converting fruits to uppercase letters, fruits are")
fruits_list = [i.upper() for i in fruits_list]
[print(f"{val + 1}. {i}") for val, i in enumerate(fruits_list)]
fruits_list.sort()
print(f"After sorting fruits, fruits are \n{fruits_list}")
