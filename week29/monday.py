# TASK 1 Write a decorator that prints a function with arguments passed to it.
# NOTE! It should print the function, not the result of its execution!

def logger(func):
    pass
    print("Just passing here...")


x = 4
y = 5

@logger
def add(x, y):
    return x + y
    print("nothing will be printed")

@logger
def square_all(*args):
    return [arg ** 2 for arg in args]
    print("same here, nothing will be preinted")


# TASK 2 Write a decorator that takes a list of stop words and replaces them with * inside the decorated function


from functools import reduce


def stop_word(give_me_stop_words: list):
    def decorator_wrapper(callback):
        def wrap(*args):
            result = callback(*args)
            return reduce(lambda string, give_me_stop_words: string.replace(give_me_stop_words, '*'), give_me_stop_words, result)
        return wrap
    return decorator_wrapper
    
    
@stop_word(['is', 'here'])
def test_func():
    return "What is happening here?"
print(test_func())


# TASK 3 Write a decorator `arg_rules` that validates arguments passed to the function.



def arg_rules(type_: type, max_length: int, contains: list):
    def decorator_wrapper(callback):
        def wrap(name):
            if len(name) > max_length:
                print("max lengt excideed!")
                return False
            elif not all(symbol in name for symbol in contains):
                print("not all symbols contained")
                return False
            else:
                return callback(name)
        return wrap
    return decorator_wrapper
    

@arg_rules(type_=str, max_length=15, contains=['bbb', '@'])
def create_slogan(name: str) -> str:
    return 

print(create_slogan('bbb @x'))
print(create_slogan('gefv xxx @ ccd.o'))
