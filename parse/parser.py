from enum import Enum
from dataclasses import dataclass

class TokenType(Enum):
    START_ANCHOR = "^"
    ANY_CHAR = "."
    END_ANCHOR = "$"
    LITERAL = ""
    QUANTIFIER = "*"

@dataclass
class Token:
    type: TokenType
    value: str = ""

class Parser:
    def __init__(self) -> None:
        pass

    def parse_pattern(self, pattern) -> list[Token]:
        tokens = []
        for char in pattern:
            match char:
                case TokenType.START_ANCHOR.value:
                    token = Token(TokenType.START_ANCHOR, char)
                    tokens.append(token)
                case TokenType.END_ANCHOR.value:
                    token = Token(TokenType.END_ANCHOR, char)
                    tokens.append(token)
                case TokenType.QUANTIFIER.value:
                    token = Token(TokenType.QUANTIFIER, char)
                    tokens.append(token)
                case _:
                    token = Token(TokenType.LITERAL, char)
                    tokens.append(token)
        return tokens

