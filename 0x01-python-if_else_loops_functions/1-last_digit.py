#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
for i in range(0, len(str(number))):
    if i == (len(str(number))-1):
        if int(str(number)[i]) < 6 and int(str(number)[i]) > 0:
            print(f"Last digit of {number} is {str(number)[i]} and is less than 6 and not 0")
        elif int(str(number)[i]) == 0:
            print(f"Last digit of {number} is {str(number)[i]} and is 0")
        else:
            print(f"Last digit of {number} is {str(number)[i]} and is greater than 5")
