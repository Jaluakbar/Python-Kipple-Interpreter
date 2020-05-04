class Token():
    def __init__(self, value, type):
        self.value = value
        self.type = type

    def __str__(self):
        """String representation of the class instance.

        Examples:
            Token(INTEGER, 3)
            Token(PLUS '+')
        """
        return 'Token({type}, {value})'.format(
            type=self.type,
            value=repr(self.value)
        )

    def __repr__(self):
        return self.__str__()

class Interpreter():
    def __init__(self):
        self.STACK = "STACK"
        self.INPUT_STACK = "INPUT_STACK"
        self.OUTPUT_STACK = "OUTPUT_STACK"
        self.ASCII_STACK = "ASCII_STACK"
        self.ASSIGN_LEFT = "ASSIGN_LEFT"
        self.ASSIGN_RIGHT = "ASSIGN_RIGHT"
        self.PLUS = "PLUS"
        self.MINUS = "MINUS"
        self.QUESTION = "QUESTION"
        self.GUARD_CLOSE = "GUARD_CLOSE"
        self.GUARD_OPEN = "GUARD_OPEN"

        self.syntaxes = {
            "STACK": "abcdefghjklmnpqrstuvwxyz",
            "INPUT_STACK": "i",
            "OUTPUT_STACK": "o",
            "ASCII_STACK_SYNTAX": "@",
            "ASSIGN_LEFT_SYNTAX": ">",
            "ASSIGN_RIGHT_SYNTAX": "<",
            "PLUS": "+",
            "MINUS": "-",
            "QUESTION": "?",
            "GUARD_CLOSE": ")",
            "GUARD_OPEN": "(",
        }

    def get_token(self, character):

        if character is None:
            raise ValueError("None Char")

        elif character in self.syntaxes["STACK"]:
            return Token(character, self.STACK)
        
        elif character in self.syntaxes["INPUT_STACK"]:
            return Token(character, self.INPUT_STACK)
            
        elif character in self.syntaxes["OUTPUT_STACK"]:
            return Token(character, self.OUTPUT_STACK)
        
        elif character in self.syntaxes["ASCII_STACK_SYNTAX"]:
            return Token(character, self.ASCII_STACK)

        elif character in self.syntaxes["ASSIGN_LEFT_SYNTAX"]:
            return Token(character, self.ASSIGN_LEFT)
        
        elif character in self.syntaxes["ASSIGN_RIGHT_SYNTAX"]:
            return Token(character, self.ASSIGN_RIGHT)

        elif character in self.syntaxes["PLUS"]:
            return Token(character, self.PLUS)

        elif character in self.syntaxes["MINUS"]:
            return Token(character, self.MINUS)
        
        elif character in self.syntaxes["QUESTION"]:
            return Token(character, self.QUESTION)

        elif character in self.syntaxes["GUARD_CLOSE"]:
            return Token(character, self.GUARD_CLOSE)
        
        elif character in self.syntaxes["GUARD_OPEN"]:
            return Token(character, self.GUARD_OPEN)

        else:
            raise ValueError("Wrong Syntax")


    def lex(self, characters,index = 0):
        #print(index)
        #print(characters[index])
        #print("===")
        if len(characters) == 0:
            raise ValueError("Command string empty")
            
        elif len(characters)  == (index+1):
            return [self.get_token(characters[index])]

        return [self.get_token(characters[index])] + (self.lex(characters, index + 1))


inter = Interpreter()
crs = "io"
lst = inter.lex(crs)

print(lst)

