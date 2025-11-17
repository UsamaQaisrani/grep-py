from enum import Enum
import sys

class TokenType(Enum):
    CONCAT = 1
    START_ANCHOR = 2
    END_ANCHOR = 3
    LITERAL = 4
    QUANTIFIER = 5
    UNION = 6
    ONEORMORE = 7
    OPTIONAL = 8
    GROUP_START = 9
    GROUP_END = 10
    NEWLINE = 11
    GROUP = 12


class Token:
    def __init__(self, token_type, token_value) -> None:
        self.token_type = token_type
        self.token_value = token_value

class Lexer:
    def __init__(self, source) -> None:
        self.source = source + "\n"
        self.curr_char = ""
        self.curr_pos = -1
        self.next_char()
        

    def next_char(self):
        self.curr_pos += 1
        if self.curr_pos >= len(self.source):
            self.curr_char = "\0"
        else:
            self.curr_char = self.source[self.curr_pos]

    def peek(self):
        if self.curr_pos + 1 >= len(self.source):
            return "\0"
        else:
            return self.source[self.curr_pos + 1]

    def abort(self, message):
        sys.exit(f"Lexing Error: {message}")

    def get_token(self):
        token = None

        if self.curr_char == ".":
            token = Token(TokenType.CONCAT, self.curr_char)
        elif self.curr_char == "|":
            token = Token(TokenType.UNION, self.curr_char)
        elif self.curr_char == "+":
            token = Token(TokenType.ONEORMORE, self.curr_char)
        elif self.curr_char == "*":
            token = Token(TokenType.QUANTIFIER, self.curr_char)
        elif self.curr_char == "?":
            token = Token(TokenType.OPTIONAL, self.curr_char)
        elif self.curr_char == "(":
            token = Token(TokenType.GROUP_START, self.curr_char)
        elif self.curr_char == ")":
            token = Token(TokenType.GROUP_END, self.curr_char)
        elif self.curr_char == "\n":
            token = Token(TokenType.NEWLINE, self.curr_char)
        else:
            token = Token(TokenType.LITERAL, self.curr_char)

        self.next_char()
        return token

