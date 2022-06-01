import argparse
import uuid

parser = argparse.ArgumentParser(description="TODO list manager")
parser.add_argument(
    "--todo",
    "-t",
    nargs="?",
    metavar="todo: ",
    type=str,
    help="Write an item to add to your TODO list",
)
parser.add_argument(
    "--view",
    "-v",
    nargs="?",
    metavar="view: ",
    type=null,
    help="This takes no arguments, don't give",
)

arg = parser.parse_args()
if len(arg.todo) != 0:
    full_unique_id = str(uuid.uuid4())
    unique_id = full_unique_id[0:8]
    string_to_write = unique_id + " " + arg.todo + "\n"
    file = open("/home/ravi/Documents/TODO/TODO.txt", "a")
    file.write(string_to_write)
    file.close()
