from tokens import *
from tokenizer import *
from stack import *

def loop(tokens : List[Token], stack : program_stack):
    loop_true = get_last_value(stack, tokens[0].value)
    print(loop_true)
    if loop_true == 0:
        print("return?")
        return
    operator(tokens, stack)
    loop(tokens, stack)


def operator(tokens : List[Token], stack : program_stack):
    guard_open_i = [i for i, x in enumerate(tokens) if isinstance(x, Guard_Open)]
    guard_close_i = [i for i, x in enumerate(tokens) if isinstance(x, Guard_Close)]


    if len(guard_open_i) != len(guard_open_i):
        raise Error
    
    if len(guard_open_i) > 0:
        open_index = guard_open_i[0]
        close_index = guard_close_i[-1]

        print("before", tokens[0:open_index])
        #Exeucte things before loop
        operator(tokens[0:open_index], stack)

        #do loop over range
        print("loop", tokens[open_index+1:close_index])
        loop(tokens[open_index+1:close_index], stack)

        #here after
        print("REst", tokens[close_index+1:])
        new_index = [i for i, x in enumerate(tokens[close_index+1:]) if isinstance(x, Op_Token)]
        index = list(map(lambda x: x + close_index+1, new_index))
    else:
        index = [i for i, x in enumerate(tokens) if isinstance(x, Op_Token)]

    if len(index) == 0:
        return

    print(index, "INDEX")

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
