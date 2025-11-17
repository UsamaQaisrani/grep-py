from lexer import TokenType


class NFAState:
    def __init__(self, transitions={}, is_accepting=False) -> None:
        self.transitions = transitions
        self.is_accepting = is_accepting

class NFAFragment:
    def __init__(self, start_state, end_state) -> None:
        self.start_state = start_state
        self.end_state = end_state

class NFA:

    def build_fragment(self, node):
        if node.token.token_type == TokenType.LITERAL:
            start_state = NFAState()
            end_state = NFAState()
            start_state.transitions[node.token.token_value] = [end_state]
            return NFAFragment(start_state, end_state)

        if node.token_type == TokenType.CONCAT:
            frag_A = self.build_fragment(node.children[0])
            frag_B = self.build_fragment(node.children[1])
            frag_A.end_state.transitions["EPSILON"] = [frag_B.start_state] 
            return NFAFragment(frag_A.start_state, frag_B.end_state)

