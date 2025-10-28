import sys

def main():
    if len(sys.argv) < 1:
        print("Usage: grepy <pattern|sentence> <file>")

    assert len(sys.argv) == 3, print("Missing Arguments")

    pattern = sys.argv[1]
    file_path = sys.argv[2]

if __name__ == "__main__":
    main()
