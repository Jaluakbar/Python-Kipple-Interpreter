from tokens import *
from tokenizer import *
from stack import *

def operator(tokens : List[Token]):
    index = list(i for i, x in enumerate(tokens) if isinstance(x, Op_Token))

    if len(index) == 0:
        return
    
    head = index[:1][0]
    tail = index[1:]

    print("head", head)

    if isinstance(tokens[head], Plus_Op):
        lhs = tokens[head-1].value
        rhs = int(tokens[head+1].value)

        Stack_Holder.data[lhs][-1] += rhs

    elif isinstance(tokens[head], Minus_Op):
        lhs = tokens[head-1].value
        rhs = int(tokens[head+1].value)

        Stack_Holder.data[lhs][-1] -= rhs
    
    elif isinstance(tokens[head], Assign_Left):
        lhs = tokens[head-1].value
        rhs = tokens[head+1].value

        Stack_Holder.data[lhs].append(rhs)

    elif isinstance(tokens[head], Assign_Right):
        lhs = tokens[head-1].value
        rhs = tokens[head+1].value

        Stack_Holder.data[rhs].append(lhs)
    
    elif isinstance(tokens[head], Question):
        lhs = tokens[head-1].value

        if Stack_Holder.data[lhs][-1] == 0:
            Stack_Holder.data[lhs].clear()
