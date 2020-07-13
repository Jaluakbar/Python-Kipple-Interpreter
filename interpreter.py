from tokens import *
from tokenizer import *
from stack import *

def operator(tokens : List[Token], stack : program_stack):
    index = [i for i, x in enumerate(tokens) if isinstance(x, Op_Token)]
    print("index", index)

    if len(index) == 0:
        return
    
    op_index = index[0]
    list_tail = tokens[op_index+1:]
    print(op_index)
    print(list_tail)

    print("op_index", op_index)
    print(stack.data)

    if isinstance(tokens[op_index], Plus_Op):
        lhs = tokens[op_index-1].value
        rhs = get_token_value(stack, tokens[op_index+1], tokens[op_index-1])

        print(type(lhs), type(rhs))

        add_value_stack(stack, lhs, rhs)

        operator(list_tail, stack)

    elif isinstance(tokens[op_index], Minus_Op):
        lhs = tokens[op_index-1].value
        rhs = int(tokens[op_index+1].value)

        stack.data[lhs][-1] -= rhs
        operator(list_tail, stack)
    
    elif isinstance(tokens[op_index], Assign_Left):
        lhs = tokens[op_index-1].value
        rhs = int(tokens[op_index+1].value)

        stack.data[lhs].append(rhs)
        operator(list_tail, stack)


    elif isinstance(tokens[op_index], Assign_Right):
        lhs = int(tokens[op_index-1].value)
        rhs = tokens[op_index+1].value

        stack.data[rhs].append(lhs)
        operator(list_tail, stack)

    
    elif isinstance(tokens[op_index], Question):
        lhs = tokens[op_index-1].value

        if stack.data[lhs][-1] == 0:
            stack.data[lhs].clear()
        
        operator(list_tail, stack)

