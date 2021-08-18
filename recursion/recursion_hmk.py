#task 1

def to_power(x: int, exp: int) -> int:
    if exp == 0:
        return 1
    elif x == 1:
        return x
    return (x * to_power(x, exp -1))

print(to_power(2,2))

-------------------------------------------------------------------------------------------------
#task 2

# function which return reverse of a string

some_string_to_be_reversed = 'a santa at nasa'


def is_palindrome(looking_str: str, index: int = 0) -> bool:
    if len(looking_str) == 1:
        return looking_str
    return looking_str[-1] + is_palindrome(looking_str[:-1])

ans = is_palindrome(some_string_to_be_reversed)

if ans == True:
    print("Yes," " " + some_string_to_be_reversed + ":" + " " + "is a palindrome string")
else:
    print("No")

-------------------------------------------------------------------------------------------------


#task 3

def mult(a: int, n: int) -> int:
    if a < 0 or n < 0:
        return ValueError
    return (mult(a, n))

print(mult(2, 9))

-------------------------------------------------------------------------------------------------


#Task 4

some_string_to_be_reversed = 'njjjj'


def reverse_two(input_str: str) -> str:
    if len(input_str) == 1:  # base, when to stop
        return input_str
    return input_str[-1] + reverse_two(input_str[:-1])

print(reverse_two(some_string_to_be_reversed))
