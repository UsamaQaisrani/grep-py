import sys
from read.reader import Reader

def main():
    if len(sys.argv) < 1:
        print("Usage: grepy <pattern|sentence> <file>")

    assert len(sys.argv) == 3, print("Missing Arguments")

    pattern = sys.argv[1]
    file_path = sys.argv[2]

    reader = Reader()
    reader.read_line_by_line(file_path)

if __name__ == "__main__":
    main()
