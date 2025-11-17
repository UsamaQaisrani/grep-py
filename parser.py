from lexer import * 

class ASTNode:
    def __init__(self, token=None, children=[]) -> None:
        self.token = token
        self.children = list(children)

    def pop_child(self):
        if len(self.children) < 1:
            return None
        popped_child = self.children.pop()
        return popped_child

    def add_child(self, child):
        self.children.append(child)

    def child_count(self):
        return len(self.children)

    def __repr__(self):
        
        if not self.children:
            return f"ASTNode({self.token.token_type}, val='{self.token.value}')"
        return f"ASTNode({self.token.token_type}, children={self.children})"

class Parser:
    def __init__(self, lexer) -> None:
        self.lexer = lexer
        self.curr_token = None
        self.peek_token = None
        self.root_node = None 
        self.next_token()
        self.next_token()

        self.precedence = {
            TokenType.UNION: 1,
            TokenType.CONCAT: 2,
            TokenType.GROUP_START: 0 
        }

    def next_token(self):
        self.curr_token = self.peek_token
        self.peek_token = self.lexer.get_token()
    
    def apply_op(self, operator_stack, operand_stack):
        if len(operand_stack) < 2:
            self.abort("Not enough operands for binary operation.")
        if len(operator_stack) < 1:
            self.abort("Missing operator for apply_op.")
        
        op_token = operator_stack.pop()
        rhs_node = operand_stack.pop()
        lhs_node = operand_stack.pop()
        new_node = ASTNode(op_token, children=[lhs_node, rhs_node])
        operand_stack.append(new_node)
    
    def apply_postfix_op(self, operand_stack, op_token):
        if len(operand_stack) < 1:
            self.abort(f"Not enough operands for postfix operator {op_token.token_type}.")
        operand_node = operand_stack.pop()
        new_node = ASTNode(op_token, children=[operand_node])
        operand_stack.append(new_node)

    def start(self):
        operator_stack = []
        operand_stack = []
        
        while not self.check_token(TokenType.NEWLINE):
            if self.curr_token.token_type == TokenType.LITERAL:
                node = ASTNode(self.curr_token)
                operand_stack.append(node)
            
            elif self.curr_token.token_type == TokenType.GROUP_START:
                operator_stack.append(self.curr_token)

            elif self.curr_token.token_type == TokenType.GROUP_END:
                while operator_stack and operator_stack[-1].token_type != TokenType.GROUP_START:
                    self.apply_op(operator_stack, operand_stack)
                if not operator_stack or operator_stack[-1].token_type != TokenType.GROUP_START:
                    self.abort("Mismatched parentheses: No matching '('.")
                operator_stack.pop()
            
            elif self.curr_token.token_type == TokenType.UNION or self.curr_token.token_type == TokenType.CONCAT:
                current_op_precedence = self.precedence[self.curr_token.token_type]
                while (operator_stack and
                       operator_stack[-1].token_type != TokenType.GROUP_START and
                       self.precedence.get(operator_stack[-1].token_type, 0) >= current_op_precedence):
                    self.apply_op(operator_stack, operand_stack)
                operator_stack.append(self.curr_token)

            elif self.curr_token.token_type == TokenType.ONEORMORE: 
                self.apply_postfix_op(operand_stack, self.curr_token)

            elif self.curr_token.token_type == TokenType.QUANTIFIER: 
                self.apply_postfix_op(operand_stack, self.curr_token)

            elif self.curr_token.token_type == TokenType.OPTIONAL: 
                self.apply_postfix_op(operand_stack, self.curr_token)
            
            else:
                self.abort(f"Unhandled token type: {self.curr_token.token_type}")

            self.next_token()
        
        while operator_stack:
            if operator_stack[-1].token_type == TokenType.GROUP_START:
                self.abort("Mismatched parentheses: Extra '('.")
            self.apply_op(operator_stack, operand_stack)
        
        if len(operand_stack) != 1:
            self.abort("Invalid expression. Final operand stack must have exactly one AST.")
            
        self.root_node = operand_stack.pop()
        return self.root_node

    def abort(self, message="Parsing error."):
        raise Exception(message)

    def check_token(self, token_type):
        return token_type == self.curr_token.token_type

    def check_peek(self, kind):
        return kind == self.peek_token.token_type
