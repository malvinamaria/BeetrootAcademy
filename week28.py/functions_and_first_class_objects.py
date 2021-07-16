# TASK ONE

def function():
    x = 1
    y = 2
    z = 5
    str1 = "something"
print("Detect number of local variables declared in a function:")

print(function.__code__.co_nlocals)
print(function.__code__)  # code object function at 0x10b1d5660


# TASK TWO
def adding(z):
    return z * 7

def sub(f):
    def result_fun(z):
        return f(f(z))
    return result_fun

final_result = sub(adding)
print(final_result(10))  # ans = 490   70*(10*7)


# TASK 3

nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]

def callbackFunc1(nums):
    return [num ** 2 for num in nums]
    print("This is a callback function one.")

def callbackFunc2(self):
    return [num for num in nums if num > 0]
    print("This is a callback function two.")

def choose_func(nums: list, callback1, callback2):
    return nums1 and nums2

print(choose_func(nums1, callbackFunc1, callbackFunc2))
