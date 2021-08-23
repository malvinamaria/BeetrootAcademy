#TASK 1

some_list = ['malwina', 'maria', 'polak']

class Stack:
    def __init__(self):
        self._items = some_list

    def __repr__(self):
        representation = "<Stack>\n"
        for ind, item in enumerate(reversed(self._items), 1):  #because of 1 the index on print starts with 1 insteadf of 0
            representation += f"{ind}: {str(item)}"
        return representation


if __name__ == "__main__":
    s = Stack()

    print(s)

# OUTPUT <Stack>
# 1: polak2: maria3: malwina


----------------------------------------------------------------------------------------------------------------------------
# task 2

open_parenthesis = ['(', '{', '[']
closed_parenthesis = [')', '}', ']']


def check_balance(str):
    stack = []
    for parenthesis in str:
        if parenthesis in open_parenthesis:
            stack.append(parenthesis)
        elif parenthesis in closed_parenthesis:
            matching = closed_parenthesis.index(parenthesis)
            if (len(stack) > 0) and (open_parenthesis[matching] == stack[len(stack) -1]):
                stack.pop()
            else:
                return "Unbalanced"
    if len(stack) == 0:
        return "Balanced"
    else:
        return "Unbalanced"


some_string = "{[]{()}}"
print(some_string, "-", check_balance(some_string))

some_string = "[{}{})(]"
print(some_string, "-", check_balance(some_string))

some_string = "{[]{()}}))))((())((((("
print(some_string, "-", check_balance(some_string))

some_string = "[{)()()()()()()"
print(some_string, "-", check_balance(some_string))
