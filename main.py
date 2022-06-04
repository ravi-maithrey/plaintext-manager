import argparse
import uuid

parser = argparse.ArgumentParser(
    description="TODO list manager", prog="plaintext-manager"
)
parser.add_argument(
    "--todo", "-t", type=str, help="Write an item to add to your TODO list",
)
parser.add_argument(
    "--view", "-v", action="store_true", help="View the ",
)

arg = parser.parse_args()
if arg.todo != None and len(arg.todo) != 0:
    full_unique_id = str(uuid.uuid4())
    unique_id = full_unique_id[0:8]
    string_to_write = unique_id + " " + arg.todo + "\n"
    file = open("/home/ravi/Documents/TODO/TODO.txt", "a")
    file.write(string_to_write)
    file.close()

if arg.view != False:
    file = open("/home/ravi/Documents/TODO/TODO.txt", "r")
    for line in file:
        print(line)
