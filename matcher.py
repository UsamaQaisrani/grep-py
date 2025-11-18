class Matcher:
    def __init__(self, start_state, epsilon="__EPSILON__", any_char="__ANY_CHAR__") -> None:
        self.start_state = start_state
        self.EPSILON = epsilon
        self.ANY_CHAR = any_char

    def get_closure_set(self, states):
        to_visit = list(states)
        visited = set(states)

        while to_visit:
            curr_state = to_visit.pop()
            if self.EPSILON in curr_state.transitions:
                for next_state in curr_state.transitions[self.EPSILON]:
                    if next_state not in visited:
                        visited.add(next_state)
                        to_visit.append(next_state)

        return visited

    def match(self, text: str) -> bool:
            current_states = self.get_closure_set({self.start_state})

            for char in text:
                next_states = set()
                for state in current_states:
                    if char in state.transitions:
                        next_states.update(state.transitions[char])
                    if self.ANY_CHAR in state.transitions:
                        next_states.update(state.transitions[self.ANY_CHAR])
                if not next_states:
                    return False

                current_states = self.get_closure_set(next_states)

            for state in current_states:
                if state.is_accepting:
                    return True
                    
            return False
