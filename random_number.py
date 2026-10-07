import random
number = random.randint(1, 1000)
attempts = 0
while True:
    input_number =input("Guess a number between 1 and 1000: ")
    input_number = int(input_number)
    attempts += 1
    if input_number== number:
        print("Yes!congetulations! You did it  https://www.pinterest.com/pin/cat-you-got-this-cute-gif-769130442624233686/")
        break
    if input_number < number:
        print("too low! try again. ")
    if input_number > number:
        print("too high! try again. ")
print("you tried",attempts,"times to find correct number")