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

class Assign_Left(Token):
    def __init__(self, value):
        super().__init__(value)

class Assign_Right(Token):
    def __init__(self, value):
        super().__init__(value)

class Plus(Token):
    def __init__(self, value):
        super().__init__(value)

class Minus(Token):
    def __init__(self, value):
        super().__init__(value)

class Question(Token):
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