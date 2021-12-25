import random

computer_number = random.randint(0, 20)
count = 0

while True:
    user_number = int(input())
    count = count + 1

    if user_number == computer_number:
        print("eyval, barande shodi")
        print(count)
        break

    elif user_number > computer_number:
        print("boro paeen")

    elif user_number < computer_number:
        print("boro bala")   
