import numpy as np


answer = np.random.randint(1, 11)
number = int(input("Guess A Number between 1 and 10: "))
if number <= 0:
    print("Invalid Number Closing Program")
    exit(0)
if number > 10:
    print("Invalid Number Closing Program")
    exit(0)
if number == answer:
    print("Correct Number!!!")
else:
    print("Sorry You lost the number was")
    print(answer)
