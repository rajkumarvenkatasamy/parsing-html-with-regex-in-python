import re


matched = re.compile('<title>').search
with open("simple.html", "r") as input_file:
    for line in input_file:
        if matched(line):
            print(line.replace("<title>", "").replace("</title>", ""))
