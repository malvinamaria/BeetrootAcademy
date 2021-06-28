import random
guessing_input = input("Guess a number between 1 and 10 and press enter:")
random_number_generator = (random.uniform(1, 10))
if random_number_generator == guessing_input:
    print("Correct guess")
elif guessing_input != random_number_generator:
    print(f"Inorecct guess, the correct number was:", {random_number_generator})