import sys
from reader import Reader
from lexer import Lexer
from parser import Parser
from nfa import *
from matcher import *

def main():
    if len(sys.argv) < 1:
        print("Usage: grepy <pattern|sentence> <file>")

    assert len(sys.argv) == 3, print("Missing Arguments")

    pattern = preprocess_input(sys.argv[1])
    file_path = sys.argv[2]

    reader = Reader()
    lines = reader.read_line_by_line(file_path)

    lexer = Lexer(pattern)
    parser = Parser(lexer)
    ast_root = parser.start()
    nfa = NFA(ast_root)
    nfa_start_state = nfa.build_nfa()
    matcher = Matcher(nfa_start_state)

    for line in lines:
        stripped_line = line.strip()
        if matcher.match(stripped_line):
            print(line)

def preprocess_input(input):
    if len(input) < 2:
        return input

    result = []
    special_operators = set("()|*+?")
    quantifiers = set("*+?")

    for i in range(len(input)-1):
        curr_char = input[i]
        next_char = input[i+1]
        result.append(curr_char)

        is_current_literal = curr_char not in special_operators
        is_next_literal = next_char not in special_operators

        concat = False

        if is_current_literal and is_next_literal:
            concat = True
        elif is_current_literal and next_char == "(":
            concat = True
        elif curr_char == ")" and is_next_literal:
            concat = True
        elif curr_char == ")" and next_char == "(":
            concat = True
        elif curr_char in quantifiers and next_char == "(":
            concat = True
        elif curr_char in quantifiers and is_next_literal:
            concat = True
        
        if concat:
            result.append(".")

    result.append(input[-1])

    return "".join(result)



if __name__ == "__main__":
    main()


