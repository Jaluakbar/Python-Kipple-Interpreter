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
            "z" : [0],
            "@" : [0]
        }

def get_last_value(stack : program_stack, stackname : str)->int:
    if len(stack.data[stackname]) == 0:
        return 0
    return int(stack.data[stackname][-1])

def pop_last_value(stack : program_stack, stackname : str)->int:
    if len(stack.data[stackname]) == 0:
        return 0
    return int(stack.data[stackname].pop())

def add_value_stack(stack : program_stack, stackname : str, value : int):
    if (stackname == "@"):
        print(value)
        value = ord(str(value))
        print(value)
    if len(stack.data[stackname]) == 0:
        stack.data[stackname].append(value)
    else:
        stack.data[stackname][-1] += value

def multiple_chr_ascii(stack : program_stack, stackname : str, value : str):
    if len(value) == 0:
        return

    character = ord(value[0])
    stack.data[stackname].append(character)

    multiple_chr_ascii(stack, stackname, value[1:])


def append_value_stack(stack : program_stack, stackname : str, value : int):
    if (stackname == "@"):
        multiple_chr_ascii(stack, stackname, str(value))
    else:
        stack.data[stackname].append(value)

def sub_value_stack(stack : program_stack, stackname : str, value : int):
    if len(stack.data[stackname]) == 0:
        stack.data[stackname].append(0 - value)
    else:
        stack.data[stackname][-1] -= value

def get_token_value(stack : program_stack, token : Token, other : Token)->int:
    #Prevent assigning to self 
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
