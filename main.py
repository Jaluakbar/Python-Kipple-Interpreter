from tokens import *
from tokenizer import *
from stack import *
from interpreter import *

chars = get_str_from_file("text.txt")
tokens = (convert_str(chars))

print(tokens)

operator(tokens)

print(Stack_Holder.data)