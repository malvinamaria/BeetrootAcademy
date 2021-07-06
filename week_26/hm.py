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

