import argparse
import sys
import re
from pathlib import Path

parser = argparse.ArgumentParser(description= "a tool for finding files")

parser.add_argument("pattern", type=str, help="Pattern")
parser.add_argument("file", type=str, help="File path")
args = parser.parse_args()
path = Path(args.file)
target = args.pattern
pattern = rf"^{re.escape(target)}"
binary_files = r'\.(jpeg|jpg|png|gif|pdf|zip|tar|gz|rar|exe|dll|so|mp3|mp4)$'
if args.file is None or args.pattern is None:
    print("File path was not inputted")
    sys.exit()
if re.match(binary_files, args.file):
    print("cant open a binary file")
    sys.exit()


def read_words_lazy(file_path):
    global binary_files
    if re.match(binary_files, file_path):
        print(f"skipped: {file_path} ")
        return
    with open(file_path, 'r', encoding='utf-8') as file:
        line_Number = 0
        for line in file:
            line_Number += 1
            for word in line.split():
                yield line_Number, word


if not path.is_dir():
    for line_Number,word in read_words_lazy(args.file):
        
        output = re.search(pattern, word, re.IGNORECASE)
        if output == None:
            continue
        else:
            print(f"{output}:{line_Number}: {word}")
else:
    def grep(path):
        for file in path.iterdir():
            if not file.is_dir():
                for line_Number,word in read_words_lazy(file):
                    output = re.search(pattern, word, re.IGNORECASE)
                    if output == None:
                        continue
                    else:
                      print(f"{output}:{line_Number}: {word}")
            else:
                grep(file)
    grep(path)
        