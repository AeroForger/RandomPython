import argparse
from collections import Counter


parser = argparse.ArgumentParser(description= "a tool for text")

parser.add_argument("file", type=str, help="file path")

args = parser.parse_args()

words = []
chars = 0
lines = 1
skip_chars = [" ", "\n", ".", ",", "!", "?", ";", ":", "'", '"', "(", ")", "[", "]", "{", "}", "-", "_", "/", "\\"]

with open(args.file, "r") as file:
    text = file.read()
    word = []
    if not text:
        print("The file is empty.")
    for char in text:
        if char not in skip_chars:
            word.append(char.lower())
            chars += 1
        else:
            if char == "\n":
                lines += 1
            if len(word) != 0:
                words.append("".join(word))
                word = []
            else:
                word = []
if len(word) != 0:
    words.append("".join(word))
    word = []
counter = Counter(words)

print(f"Number of words: {len(words)}")
print(f"Number of characters: {chars}")
print(f"Number of lines: {lines}")
print(f"Most common words: {counter.most_common(10)}")

