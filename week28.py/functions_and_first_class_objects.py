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
