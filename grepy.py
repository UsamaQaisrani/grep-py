import sys
from read.reader import Reader
from search.search import search_sentence
from parse.parser import Parser, Token

def main():
    if len(sys.argv) < 1:
        print("Usage: grepy <pattern|sentence> <file>")

    assert len(sys.argv) == 3, print("Missing Arguments")

    pattern = sys.argv[1]
    file_path = sys.argv[2]

    reader = Reader()
    lines = reader.read_line_by_line(file_path)

#    for line in lines:
#        if search_sentence(pattern, line):
#            print(line)
    parser = Parser()
    tokens = parser.parse_pattern(pattern)
    for token in tokens:
        print(token.type, token.value)


if __name__ == "__main__":
    main()
