import random

num_ran = random.randint(1, 10)
print(f"The random number is {num_ran}")
i = 0
while True:
    get_in = int(input("Enter an integer to guess:"))

    i += 1

    if get_in == num_ran:
        print("Congrats that you guess the number correctly")
        break
    elif get_in < num_ran:
        print("Try a higher number")
        print(f"You have {5 - i} guesses remaining")
        if i >= 5:
            break
    elif get_in > num_ran:
        print("Try a lower number")
        print(f"You have {5 - i} guesses remaining")
        if i >= 5:
            break
