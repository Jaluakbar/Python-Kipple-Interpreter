from typing import List
from tokens import *

def get_str_from_file(filename : str)->List[str]:
    f = open(filename, "r")
    all =  " ".join(f.read().split())
    return all

def multiple_digits(code : str)->int:
    if code[0].isdigit() and len(code) == 1:
        return 1
    elif code[0].isdigit():
        return 1 + multiple_digits(code[1:])
    else:
        return 0

def convert_str(code : str)->List[Token]:

    head = code[:1]
    tail = code[1:]

    if(len(tail) == 0):
        if head.isdigit():
            return [Integer(head)]
        elif head in "abcdefghjklmnpqrstuvwxyz@":
            return [Normal_Stack(head)]
        elif head == "i":
            return [Input_Stack(head)]
        elif head == "o":
            return [Output_Stack(head)]
        elif head == "@":
            return [Ascii_Stack(head)]    
        elif head == "(":
            return [Guard_Open(head)]
        elif head == ")":
            return [Guard_Close(head)]
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
        elif head == "?":
            return[Question(head)]
        else:
            return [Error(head)]
    else:
        if head.isdigit():
            used_chrs = multiple_digits(code)

            if len(code[used_chrs:]) == 0:
                return [Integer(code[0:used_chrs])]
            else:
                return [Integer(code[0:used_chrs])] + convert_str(code[used_chrs:])
        elif head in "abcdefghjklmnpqrstuvwxyz@":
            return [Normal_Stack(head)] + convert_str(tail)
        elif head == "i":
            return [Input_Stack(head)] + convert_str(tail)
        elif head == "o":
            return [Output_Stack(head)] + convert_str(tail)
        elif head == "@":
            return [Ascii_Stack(head)] + convert_str(tail)    
        elif head == "(":
            return [Guard_Open(head)] + convert_str(tail)
        elif head == ")":
            return [Guard_Close(head)] + convert_str(tail)
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
        elif head == "?":
            return [Question(head)] + convert_str(tail)
        else:
            return [Error(head)] + convert_str(tail)
