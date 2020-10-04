import re

# Print all the text lines with the “blockID” values that 
# start with the letter “i” or “g”, and end with digits
print("*** part 1 ***")
with open("blocklist.xml", "r") as f:
    for line in f.readlines():
        pattern = "blockID=\"[ig]\\d+\""
        if re.search(pattern, line):
            print(line, end='')

# Print all the text lines where 
# the “id” values are email addresses.
print("*** part 2 ***")
with open("blocklist.xml", "r") as f:
    for line in f.readlines():
        pattern = "id=\"[0-9a-zA-Z]+@[0-9a-zA-Z]+\\.[0-9a-zA-Z]+"
        if re.search(pattern, line):
            print(line, end='')