# task 2

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
    
answer = sum(prices[p] * stock[p] for p in prices) 
print(answer)


# task 3 
answer = [i for i in range(1, 11)]
print(answer)
a = [i ** 2 for i in range(1, 11)]
print(a)

square = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
for i, j in enumerate(square):
    square[i] = (i + 1, j)
print(square)
