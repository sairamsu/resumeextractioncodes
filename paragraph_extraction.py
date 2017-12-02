#import os

with open("se.txt", encoding='latin-1')as infile,open("fgh11.txt",'w', encoding='latin-1')as outfile:
    copy = False
    for line in infile:
        if line.strip() == "Summary":
            copy = True
        elif line.strip() == "Technical Skills":
            copy = False
        elif copy:
            outfile.write(line)
        fh = open("fgh11.txt",'r')
        contents = fh.read()
        len(contents)
