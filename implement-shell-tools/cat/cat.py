import argparse

parser = argparse.ArgumentParser(description="cat Cli")
parser.add_argument("-n","--number")
parser.add_argument("-b","--bytes")
parser.add_argument("text")

args = parser.parse_args()

file_name = args.text
lines = 1

if args.number:
    with open(file_name, "r") as file:
        for line in file:
            lines+=1
    print(lines)
elif args.bytes:
    with open(file_name, "r") as file:
        content = file.read()
        for char in content.split():
            for letter in char:
                print(format(ord(letter), '08b'), end='')
else:
    file = open(file_name)
    print(file.read())