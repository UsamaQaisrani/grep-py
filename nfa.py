from lexer import TokenType

class NFAState:
    def __init__(self, transitions=None, is_accepting=False) -> None:
        if transitions is None:
            self.transitions = {}
        else:
            self.transitions = transitions
            
        self.is_accepting = is_accepting

class NFAFragment:
    def __init__(self, start_state, end_state) -> None:
        self.start_state = start_state
        self.end_state = end_state

class NFA:
    def __init__(self, ast_root) -> None:
        self.ast_root = ast_root
        self.EPSILON = "__EPSILON__"
        self.ANY_CHAR = "__ANY_CHAR__"

    def build_nfa(self):
        pattern_frag = self.build_fragment(self.ast_root)
        
        start_state = NFAState()
        start_state.transitions[self.EPSILON] = [pattern_frag.start_state, start_state]
        start_state.transitions[self.ANY_CHAR] = [start_state] 
        end_state = NFAState(is_accepting=True) 
        pattern_frag.end_state.transitions[self.EPSILON] = [end_state]
        end_state.transitions[self.ANY_CHAR] = [end_state]
        return start_state

    def build_fragment(self, node):
        if node.token.token_type == TokenType.LITERAL:
            start_state = NFAState()
            end_state = NFAState()
            char = node.token.token_value
            start_state.transitions[char] = [end_state]
            return NFAFragment(start_state, end_state)

        elif node.token.token_type == TokenType.CONCAT:
            frag_A = self.build_fragment(node.children[0])
            frag_B = self.build_fragment(node.children[1])
            frag_A.end_state.transitions[self.EPSILON] = [frag_B.start_state]
            return NFAFragment(frag_A.start_state, frag_B.end_state)

        elif node.token.token_type == TokenType.UNION:
            frag_A = self.build_fragment(node.children[0])
            frag_B = self.build_fragment(node.children[1])
            start_state = NFAState()
            end_state = NFAState()
            start_state.transitions[self.EPSILON] = [frag_A.start_state, frag_B.start_state]
            frag_A.end_state.transitions[self.EPSILON] = [end_state]
            frag_B.end_state.transitions[self.EPSILON] = [end_state]
            return NFAFragment(start_state, end_state)

        elif node.token.token_type == TokenType.QUANTIFIER:
            frag_A = self.build_fragment(node.children[0])
            start_state = NFAState()
            end_state = NFAState()
            frag_A.end_state.transitions[self.EPSILON] = [frag_A.start_state, end_state]
            start_state.transitions[self.EPSILON] = [frag_A.start_state, end_state]
            return NFAFragment(start_state, end_state)

        elif node.token.token_type == TokenType.ONEORMORE:
            frag_A = self.build_fragment(node.children[0])
            start_state = NFAState()
            end_state = NFAState()
            frag_A.end_state.transitions[self.EPSILON] = [frag_A.start_state, end_state]
            start_state.transitions[self.EPSILON] = [frag_A.start_state]
            return NFAFragment(start_state, end_state)

        elif node.token.token_type == TokenType.OPTIONAL:
            frag_A = self.build_fragment(node.children[0])
            start_state = NFAState()
            end_state = NFAState()
            frag_A.end_state.transitions[self.EPSILON] = [end_state]
            start_state.transitions[self.EPSILON] = [frag_A.start_state, end_state]
            return NFAFragment(start_state, end_state)
        
        else:
            raise ValueError(f"Unknown AST node type: {node.token.token_type}")


