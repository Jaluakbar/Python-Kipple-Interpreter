from tokens import *
from tokenizer import *

class program_stack:
    def __init__(self):
        self.data = {
            "a" : [0],
            "b" : [0],
            "c" : [0],
            "d" : [0],
            "e" : [0],
            "f" : [0],
            "g" : [0],
            "h" : [0],
            "i" : [0],
            "j" : [0],
            "k" : [0],
            "l" : [0],
            "m" : [0],
            "n" : [0],
            "o" : [0],
            "p" : [0],
            "q" : [0],
            "r" : [0],
            "s" : [0],
            "t" : [0],
            "u" : [0],
            "v" : [0],
            "w" : [0],
            "x" : [0],
            "y" : [0],
            "z" : [0]
        }

def get_last_value(stack : program_stack, stackname : str)->int:
    return int(stack.data[stackname][-1])

def pop_last_value(stack : program_stack, stackname : str)->int:
    value = stack.data[stackname].pop()
    return int(value)

def add_value_stack(stack : program_stack, stackname : str, value : int):
    if len(stack.data[stackname]) == 0:
        print(type(value))
        stack.data[stackname].append(value)
    else:
        stack.data[stackname][-1] += value

def sub_value_stack(stack : program_stack, stackname : str, value : int):
    stack.data[stackname][-1] -= value

def get_token_value(stack : program_stack, token : Token, other : Token)->int:
    if token.value != other.value:
        if isinstance(token, Normal_Stack):
            return pop_last_value(stack, token.value)
        else:
            return int(token.value)
    else:
        if isinstance(token, Normal_Stack):
            return get_last_value(stack, token.value)
        else:
            return int(token.value)




# c.data["a"].append(1)
# c.data["a"].append(2)

# add_value_stack(Stack_Holder, "a", 4)

# sub_value_stack(c, "a", 7)

# pop_last_value(c, "a")

