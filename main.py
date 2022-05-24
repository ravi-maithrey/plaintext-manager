import argparse


parser = argparse.ArgumentParser(description="TODO list manager")
parser.add_argument(
    "todo", metavar="todo: ", type=str, help="Write an item to add to your TODO list",
)
parser.add_argument(
    "view",
    metavar="view todo list, first word is unique identifier",
    help="This takes no arguments, don't give",
)

arg = parser.parse_args()
if len(arg.todo) != 0:
    file = open("/home/ravi/Documents/TODO/TODO.txt", "a")
    file.write(arg.todo)
    file.close()
