# hello world

print("hello world")

count_numbers = [1, 2, 3, 4, 5, 6]
fruits = ["apples", "pineaple", "mango", "orange"]
animals = ["cats", "dogs", "zebras", "unicorns"]

#prints exact
print(fruits)

#prints only values no commas and []
print(*fruits)

print(*fruits, sep = "\n")
# does not work without *

#can we have some examples with end ???
print(fruits, end = "aaa")
