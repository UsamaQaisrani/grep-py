import sys
from read.reader import Reader
from search.searcher import Searcher
from lexer import Lexer

def main():
    if len(sys.argv) < 1:
        print("Usage: grepy <pattern|sentence> <file>")

    assert len(sys.argv) == 3, print("Missing Arguments")

    pattern = sys.argv[1]
    file_path = sys.argv[2]

    reader = Reader()
    lines = reader.read_line_by_line(file_path)

    lexer = Lexer(pattern)
    tokens = lexer.tokenize()

    searcher = Searcher(tokens)
    for line in lines:
        if searcher.match(line):
            print(line)

if __name__ == "__main__":
    main()
