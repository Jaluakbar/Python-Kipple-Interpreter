from tokens import *
from tokenizer import *
from stack import *
from interpreter import *

Stack_Holder = program_stack()

chars = get_str_from_file("text.txt")
tokens = (convert_str(chars))

print(tokens)

operator(tokens, Stack_Holder)

print(Stack_Holder.data)

