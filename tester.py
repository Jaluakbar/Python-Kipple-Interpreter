from tokens import *
from tokenizer import *
from stack import *
from interpreter import *

r = get_str_from_file("text.txt")
print (r)

all = []
for i in r:
    all.append(convert_str(i))

print(all)

print(Stack_Holder.data["a"][-1])

operator(all[0])

print(Stack_Holder.data)