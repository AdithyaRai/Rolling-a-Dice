import random


while True:
    user = input("Want to Roll a Dice? (y/n): ").lower()
    if user == 'y':
       dice = random.randint(1,6)
       print(f'{dice}')

    elif user == 'n':
        print("Thank you!")
        break
    else:
        print("Invalid Input!")
    