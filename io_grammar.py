import argparse
import os
from opcode import opname

parser = argparse.ArgumentParser(description="Process some integers.")
parser.add_argument("-n", help="Name of the person")
parser.add_argument("-a", "--age", type=int, help="Age of the person")
args = parser.parse_args()

print(f"Hello {args.n}, welcome to the calculator!")

print("################# file ################")

file_name= "./text_w.txt"

fw = open(file_name, mode="w", encoding="UTF-8")
fw.write("中华人民共和国万岁！\n")
fw.write("Hello world!\n")
fw.close()

# read 1
with open(file_name, mode="r", encoding="UTF-8") as f:
    content = f.read()
print(content)

# read 2
file_handler = open(file_name, mode="r", encoding="UTF-8")
content = file_handler.read()
print(content)
file_handler.close()

# delete file
os.remove(file_name)



