from enum import Enum


class Literal:
    def __init__(self, character) -> None:
        self.character = character

class Token(Enum):
    START_ANCHOR = "^"
    ANY_CHAR = "."
    END_ANCHOR = "$"
    LITERAL = Literal("")

    def __new__(cls, value):
        obj = object.__new__(cls)
        obj._value_ = value
        return obj  

class Parser:
    def __init__(self) -> None:
        pass

    def parse_pattern(self, pattern) -> list[Token]:
        tokens = []
        for char in pattern:
            match char:
                case Token.START_ANCHOR.value:
                    tokens.append(Token.START_ANCHOR)
                case Token.END_ANCHOR.value:
                    tokens.append(Token.END_ANCHOR)
                case _:
                    token = Token.LITERAL.value.character = char
                    tokens.append(token)
        return []

