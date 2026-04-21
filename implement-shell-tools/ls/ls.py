import argparse
import os

parser = argparse.ArgumentParser(description="ls CLI")
parser.add_argument("-l","--list")
parser.add_argument("text", nargs="?")

args = parser.parse_args()

if args.list:
    if args.text:
       print(os.stat(args.text))
    else:
        print(os.stat())
else:
    if args.text:
        print(os.listdir(args.text))
    else:
        print(os.listdir())