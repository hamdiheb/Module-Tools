import cowsay
import argparse

parser = argparse.ArgumentParser(description="Cow CLI")

parser.add_argument("-a","--animal")
parser.add_argument("text", nargs="+")
args = parser.parse_args()

animal = args.animal
message = " ".join(args.text)

if(animal):
    print(cowsay.get_output_string(animal, message))
else:
    print(cowsay.cow(message))
