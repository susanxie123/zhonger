import os
import sys
import re

indent = "    "
printRe = '说：“(.*)”'


def compile(sourcefile, pyfile):
    indentNum = 0
    for line in sourcefile:
        line = line.lstrip()
        line = line.rstrip()
        sentences = line.split('。')
        sentences = list(filter(None, sentences))
        if len(sentences) == 0:
            continue
        for sentence in sentences:
            if sentence[0] == '这':
                # This is a comment
                continue
            if sentence[0:2] == "今天":
                # This is for pydoc
                continue
            if sentence[0:3] == "现在，":
                # This is the start of main
                pyfile.write("if __name__ == '__main__':\n")
                indentNum += 1
                pyfile.write(indentNum * indent + translate(sentence[3:]) + '\n')
            if sentence[0:2] == "好了":
                indentNum -= 1
                if sentence[2] == '，':
                    if sentence[3:5] == '再见':
                          return 0

def translate(sentence):
    result = ''
    if re.match(printRe, sentence):
        result += "print('" + re.match(printRe, sentence).group(1) + "')"
    return result


def main(argv):
    if len(argv) < 2:
        print("Compiler Error: must supply a sourcefile")
        sys.exit(1)
    filename = argv[1]
    if filename[-2:] != '.中':
        print("Compiler Error: incorrect source file format, must be '.中'")
    sourcefile = open(filename, 'r')
    pyfile = open(filename[:-2] + '.py', 'w')
    compile(sourcefile, pyfile)
    
if __name__ == '__main__':
    main(sys.argv)
