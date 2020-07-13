from tokens import *
from tokenizer import *
from stack import *

def loop(tokens : List[Token], stack : program_stack):
    loop_true = get_last_value(stack, tokens[0].value)
    if loop_true == 0:
        return
    operator(tokens, stack)
    loop(tokens, stack)


def operator(tokens : List[Token], stack : program_stack):
    index = [i for i, x in enumerate(tokens) if isinstance(x, Op_Token)]
    guard_open_i = [i for i, x in enumerate(tokens) if isinstance(x, Guard_Open)]
    guard_close_i = [i for i, x in enumerate(tokens) if isinstance(x, Guard_Close)]


    if len(guard_open_i) != len(guard_open_i):
        raise Error
    
    if len(guard_open_i) > 0:
        open_index = guard_open_i[0]
        close_index = guard_close_i[-1]

        print(tokens[open_index+1:close_index])

        #rhs = get_last_value(stack, tokens[open_index+1])
        loop(tokens[open_index+1:close_index], stack)
    

    if len(index) == 0:
        return
    
    op_index = index[0]
    list_tail = tokens[op_index+1:]

    if isinstance(tokens[op_index], Plus_Op):
        lhs = tokens[op_index-1].value
        rhs = get_token_value(stack, tokens[op_index+1], tokens[op_index-1])

        add_value_stack(stack, lhs, rhs)

        operator(list_tail, stack)

    elif isinstance(tokens[op_index], Minus_Op):
        lhs = tokens[op_index-1].value
        rhs = get_token_value(stack, tokens[op_index+1], tokens[op_index-1])

        sub_value_stack(stack, lhs, rhs)

        operator(list_tail, stack)
    
    elif isinstance(tokens[op_index], Assign_Left):
        lhs = tokens[op_index-1].value
        rhs = get_token_value(stack, tokens[op_index+1], tokens[op_index-1])

        stack.data[lhs].append(rhs)
        operator(list_tail, stack)


    elif isinstance(tokens[op_index], Assign_Right):
        lhs = get_token_value(stack, tokens[op_index-1], tokens[op_index+1])
        rhs = tokens[op_index+1].value

        stack.data[rhs].append(lhs)
        operator(list_tail, stack)

    
    elif isinstance(tokens[op_index], Question):
        lhs = tokens[op_index-1].value

        if stack.data[lhs][-1] == 0:
            stack.data[lhs].clear()
        
        operator(list_tail, stack)

# def interpret(tokens : List[Token], stack : program_stack):
#     index = [i for i, x in enumerate(tokens) if isinstance(x, Control)]
    
#     if len(index) == 0:
#         return operator(tokens, stack)
        
#     op_index = index[0]
#     list_tail = tokens[op_index+1:]

#     if isinstance(tokens[op_index], Plus_Op):
