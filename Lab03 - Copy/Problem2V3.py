fruits_list = ["Grapefruit", "Longan", "Orange", "Apple", "Cherry"]
print(f"The fruits are {fruits_list}")
print("After converting fruits to uppercase letters, fruits are")

for i in range(len(fruits_list)):
    fruits_list[i] = fruits_list[i].upper()

for index, name in enumerate(fruits_list, 1):
    print(f"{index}. {name}")

fruits_list.sort()
print("After sorting fruits, fruits are")
print(fruits_list)
