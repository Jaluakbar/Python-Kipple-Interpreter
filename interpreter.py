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

def find_loop(tokens : List[tuple], open_guards : int = 0, guards : List = None)->List[int]:
    # open_g = filter(lambda x: isinstance(x, Guard_Open), tokens)
    # close_g = filter(lambda x: isinstance(x, Guard_Close), tokens)

    # if len(open_g) != len(close_g):
    #     raise Exception("The parentheses amount dont match")

    if len(tokens) == 0:
        return guards

    head_token = tokens[0][0]
    head_index = tokens[0][1]
    tail_tokens= tokens[1:]

    if isinstance(head_token, Guard):
        if guards is None:
            guards = []
            
        if isinstance(head_token, Guard_Open):
            open_guards += 1
            if open_guards == 1:
                guards.append(head_index)
            return find_loop(tail_tokens, open_guards, guards)

        elif isinstance(head_token, Guard_Close):
            open_guards -= 1
            if open_guards == 0:
                guards.append(head_index)
                return guards
            else:
                return find_loop(tail_tokens, open_guards, guards)

    else:
        return find_loop(tail_tokens, open_guards, guards)



def find_loop_index(tokens : List[Token])->List[int]:
    num_tokens = len(tokens)
    index_tokens = range(0,num_tokens)

    return find_loop(list(zip(tokens, index_tokens)))



def operator(tokens : List[Token], stack : program_stack):
    guard_indexes = find_loop_index(tokens)
    print("guard_indexes", guard_indexes)

    if guard_indexes is not None and len(guard_indexes) ==2 :
        
        open_index = guard_indexes[0]
        close_index = guard_indexes[1]
        print("OPEN / CLOSE", open_index, close_index)

        #Exeucte things before loop
        print("before", tokens[0:open_index])
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

    print("Output : ", stack.data["o"])

# def interpret(tokens : List[Token], stack : program_stack):
#     index = [i for i, x in enumerate(tokens) if isinstance(x, Control)]
    
#     if len(index) == 0:
#         return operator(tokens, stack)
        
#     op_index = index[0]
#     list_tail = tokens[op_index+1:]

#     if isinstance(tokens[op_index], Plus_Op):
