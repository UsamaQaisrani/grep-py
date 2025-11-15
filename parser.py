from lexer import *
class Parser:
    def __init__(self, lexer) -> None:
        self.lexer = lexer
        self.curr_token = None
        self.peek_token = None
        self.next_token()
        self.next_token()

    def next_token(self):
        self.curr_token = self.peek_token
        self.peek_token = self.lexer.get_token()

    def start(self):
        while not self.check_token(TokenType.NEWLINE):
            self.next_token()

    def check_token(self, token_type):
        return token_type == self.curr_token.token_type

    def check_peek(self, kind):
        return kind == self.peek_token.token_type
