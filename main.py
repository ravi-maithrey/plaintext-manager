import argparse
from tokenize import String

parser = argparse.ArgumentParser(description="TODO list manager")
parser.add_argument("todo", "-t", "--todo", metavar="todo: ", type=String, help="Write an item to add to your TODO list")
input = parser.parse_args()

