#task 1 A:

def oops():
    try:
        [1,2,3][4]
    except IndexError:
        print("Indeed this is Index Error")
        raise
        
print(oops())

# B:
def oops():
    try:
        [1,2,3][4]
    except KeyError:
        print("test")
        raise
    except:
        print("this works?")
        raise
        
print(oops())

#task 2 

a, b = [int(a) for a in input("Input the value of a & b: ").split()]
print(f"The value of a =",a)
print("and the value of b =",b)


try:
    a ** 2 / b
except ZeroDivisionError:
    print("This operationis not allowed")
    raise
else:
    print("This operation is allowed")
    
print(a, b)
