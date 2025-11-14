from enum import Enum
import sys

class TokenType(Enum):
    START_ANCHOR = "^"
    ANY_CHAR = "."
    END_ANCHOR = "$"
    START_AND_END_ANCHOR = "^$"
    LITERAL = ""
    QUANTIFIER = "*"

class Token:
    def __init__(self, token_type, token_value) -> None:
        self.token_type = token_type
        self.token_value = token_value

class Lexer:
    def __init__(self, source) -> None:
        self.source = source
        self.currChar = ""
        self.currPos = -1
        self.next_char()
        

    def next_char(self):
        self.currPos += 1
        if self.currPos >= len(self.source):
            self.currChar = "\0"
        else:
            self.currChar = self.source[self.currPos]

    def peek(self):
        if self.currPos + 1 >= len(self.source):
            return "\0"
        else:
            return self.source[self.currPos + 1]

    def abort(self, message):
        sys.exit(f"Lexing Error: {message}")

    def get_token(self):
        token = None

        #TODO: Operate on source to create tokens

        self.next_char()
        return token

