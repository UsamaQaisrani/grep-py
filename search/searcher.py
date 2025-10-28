from parse.parser import Token, TokenType
from dataclasses import dataclass

@dataclass
class Searcher:
    tokens: list[Token]
    def search_sentence(self, pattern, input):
        return pattern in input

    def match(self, line):
        check = False
        match self.tokens[0].type:
            case TokenType.START_ANCHOR:
                pattern = "".join(token.value for token in self.tokens[1:])
                check = pattern == line[0:len(pattern)]

        if tokens[-1].type == TokenType.END_ANCHOR:
            if line
