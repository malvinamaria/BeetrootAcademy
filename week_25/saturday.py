#task 1

import random

randomlist = []

for i in range(0, 10):
    random_generator = random.randint(1, 100)
    randomlist.append(random_generator)
    print(randomlist)
    
print(randomlist)
print(max(randomlist))
-------------------------------------------------------------------------------------------------------------------------------------------------------------
#task 2

import random

randomlist_1 = []

for i in range(0, 10):
    random_generator = random.randint(1, 10)
    randomlist_1.append(random_generator)
    
    
print(randomlist_1)

randomlist_2 = []

for i in range(0, 10):
    random_generator = random.randint(1, 10)
    randomlist_2.append(random_generator)
  
    
print(randomlist_2)


# remove duplicates from list
randomlist_1.extend(randomlist_2)
randomlist_1 = list(dict.fromkeys(randomlist_1)) 
print(randomlist_1)

#dict.fromkeys(randomlist_1)
# Create a dictionary, using the List items as keys. This will automatically remove any duplicates because dictionaries cannot have duplicate keys.

#randomlist_1 = list
#Then, convert the dictionary back into a list:
-------------------------------------------------------------------------------------------------------------------------------------------------------------
#task 3

list_of_num_1 = [i for i in range(100) if i % 7 ==0]
#print(list_of_num_1)
list_of_num_2 = [i for i in range(100) if i % 5 != 0]

#print(list_of_num_2)

list_of_num_1.extend(list_of_num_2)
print(list_of_num_1)
