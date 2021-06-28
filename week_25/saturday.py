#task 1

import random

randomlist = []

for i in range(0, 10):
    random_generator = random.randint(1, 100)
    randomlist.append(random_generator)
    print(randomlist)
    
print(randomlist)
print(max(randomlist))
