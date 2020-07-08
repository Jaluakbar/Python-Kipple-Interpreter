class Token():
    def __init__(self, value : str):
        self.value = value

    def __str__(self):
        return '{type}({value})'.format(
            type=repr(self.__class__.__name__),
            value=repr(self.value)
        )

    def __repr__(self):
        return self.__str__()

class Op_Token(Token):
    def __init__(self, value):
        super().__init__(value)

class Normal_Stack(Token):
    def __init__(self, value):
        super().__init__(value)

class Input_Stack(Token):
    def __init__(self, value):
        super().__init__(value)

class Output_Stack(Token):
    def __init__(self, value):
        super().__init__(value)

class Ascii_Stack(Token):
    def __init__(self, value):
        super().__init__(value)

class Assign_Left(Op_Token):
    def __init__(self, value):
        super().__init__(value)

class Assign_Right(Op_Token):
    def __init__(self, value):
        super().__init__(value)

class Plus_Op(Op_Token):
    def __init__(self, value):
        super().__init__(value)

class Minus_Op(Op_Token):
    def __init__(self, value):
        super().__init__(value)

class Question(Op_Token):
    def __init__(self, value):
        super().__init__(value)

class Quard_Open(Token):
    def __init__(self, value):
        super().__init__(value)

class Quard_Close(Token):
    def __init__(self, value):
        super().__init__(value)

class Integer(Token):
    def __init__(self, value):
        super().__init__(value)

class Space(Token):
    def __init__(self, value):
        super().__init__(value)

class Error(Token):
    def __init__(self, value):
        super().__init__(value)

class End(Token):
    def __init__(self, value):
        super().__init__(value)