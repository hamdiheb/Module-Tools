import argparse
import os

parser = argparse.ArgumentParser(description="wc CLI")
parser.add_argument("-l", "--lines", action="store_true", help="Count lines")
parser.add_argument("-w", "--words", action="store_true", help="Count words")
parser.add_argument("-c", "--bytes", action="store_true", help="Count bytes")
parser.add_argument("file", nargs="?", help="File to process")

args = parser.parse_args()

if not args.file:
    parser.print_help()
else:
    byte_count = os.path.getsize(args.file)
    with open(args.file, "r") as f:
        content = f.read()
    line_count = content.count("\n")
    word_count = len(content.split())

    if not any([args.lines, args.words, args.bytes]):
        print(f"{line_count} {word_count} {byte_count} {args.file}")
    else:
        results = []
        if args.lines:
            results.append(str(line_count))
        if args.words:
            results.append(str(word_count))
        if args.bytes:
            results.append(str(byte_count))
        print(" ".join(results) + f" {args.file}")