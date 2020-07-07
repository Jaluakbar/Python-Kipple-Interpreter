from typing import List
from tokens import *

def get_str_from_file(filename : str)->str:
    f = open(filename, "r")
    return " ".join(f.read().split())

def multiple_digits(code : str)->int:
    if code[0].isdigit():
        return 1 + multiple_digits(code[1:])
    else:
        return 0

def convert_str(code : str)->List[Token]:
    head = code[:1]
    tail = code[1:]

    if(len(tail) == 1):
        if head.isdigit():
            return [Integer(head)]
        elif head in "abcdefghjklmnpqrstuvwxyz":
            return [Normal_Stack(head)]
        elif head == "i":
            return [Input_Stack(head)]
        elif head == "o":
            return [Output_Stack(head)]
        elif head == "@":
            return [Ascii_Stack(head)]    
        elif head == "(":
            return [Quard_Open(head)]
        elif head == ")":
            return [Quard_Close(head)]
        elif head == "+":
            return [Plus_Op(head)]
        elif head == "-":
            return [Minus_Op(head)]
        elif head == ">":
            return [Assign_Right(head)]
        elif head == "<":
            return [Assign_Left(head)]
        elif head == " ":
            return [Space(head)]
        else:
            return [Error(head)]

    else:
        if head.isdigit():
            used_chrs = multiple_digits(code)
            return [Integer(code[0:used_chrs])] + convert_str(code[used_chrs:])
        elif head in "abcdefghjklmnpqrstuvwxyz":
            return [Normal_Stack(head)] + convert_str(tail)
        elif head == "i":
            return [Input_Stack(head)] + convert_str(tail)
        elif head == "o":
            return [Output_Stack(head)] + convert_str(tail)
        elif head == "@":
            return [Ascii_Stack(head)] + convert_str(tail)    
        elif head == "(":
            return [Quard_Open(head)] + convert_str(tail)
        elif head == ")":
            return [Quard_Close(head)] + convert_str(tail)
        elif head == "+":
            return [Plus_Op(head)] + convert_str(tail)
        elif head == "-":
            return [Minus_Op(head)] + convert_str(tail)
        elif head == ">":
            return [Assign_Right(head)] + convert_str(tail)
        elif head == "<":
            return [Assign_Left(head)] + convert_str(tail)
        elif head == " ":
            return [Space(head)] + convert_str(tail)
        else:
            return [Error(head)] + convert_str(tail)


# r = get_str_from_file("text.txt")
# print (r)
# lst = convert_str(r)

# print(lst)
