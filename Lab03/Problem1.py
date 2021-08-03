import random


def status(count):
    print(f"You have {5 - count} guesses remaining")


max = 10
min = 1

num_ran = random.randint(min, max)
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
        status(i)
        if i >= 5:
            break
    elif get_in > num_ran:
        print("Try a lower number")
        status(i)
        if i >= 5:
            break
