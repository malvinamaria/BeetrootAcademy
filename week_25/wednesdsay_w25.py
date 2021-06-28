#task 1
import random
guessing_input = input("Guess a number between 1 and 10 and press enter:")
random_number_generator = (random.uniform(1, 10))
if random_number_generator == guessing_input:
    print("Correct guess")
elif guessing_input != random_number_generator:
    print(f"Inorecct guess, the correct number was:", random_number_generator)

 #task 2

name = input(f"What is your name?: ")
age = input("What is your age?:")
age = int(age)

print(f"Hello, {name}, on your next birthday you'll be, {age + 1} years old.")

#task 3

import random

def get_random_string(length):
    string = "tennessee"
    result = ''.join(random.choice(string) for i in range(length))
    print("Random string is:", result)


get_random_string(9)
get_random_string(9)
get_random_string(9)
get_random_string(9)
get_random_string(9)

#task 4

task_1 = 4 + 2  
task_2 = 3 * 6 - 7 + 2                
task_3 = 6 * 2 + (5 - 3) * 3 - 8      
task_4 = (3 + 4) + 7 * 2 - 1 - 9       
task_5 = 5 - 2 + 4 * (8 - (5 + 1)) + 9   
task_6 = (8 - 1 + 3) * 6 - ((3 + 7) * 2)

print(task_1, task_2, task_3, task_4, task_5, task_6)
a = input("Give me the asswer to following expression: 4 + 2 = ")
if a == task_1:
    print("Coorect, you're ready for next mathematical expression")
elif a != 6:
    print("Game over, it seems that you don't know basic arithemtics.")
