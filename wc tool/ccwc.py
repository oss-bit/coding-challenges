import argparse
import os
import sys

parser = argparse.ArgumentParser(description='count the number of words, lines, and bytes in a file')
parser.add_argument('-c',action='store_true', help='outputs the number of bytes in a file')
parser.add_argument('-l', action='store_true', help='outputs the number of lines in a file')
parser.add_argument('-w', action='store_true', help='outputs the number of words in a file')
parser.add_argument('-m', action='store_true', help='outputs the number of characters in a file based on the locale')
parser.add_argument('filename', type=str, help='the filename or directory where the file is stored')

args = parser.parse_args()

num_lines = 0
num_words = 0
num_characters = 0
num_bytes = 0
if args.c:
    num_bytes = os.path.getsize(args.filename)
with open(args.filename) as f:
    for line in f.readlines():
        if args.w:
            word_list = line.split()
            num_words += len(word_list)
        if args.l:
            num_lines += 1
        if args.m:
            word_list = line.split()
            num_characters += sum(len(word) for word in word_list)
        if not args.w and not args.m and not args.l and args.filename:
            num_lines += 1
            word_list = line.split()
            num_words += len(word_list)
            word_list = line.split()
            num_characters += sum(len(word) for word in word_list)
            num_bytes = os.path.getsize(args.filename)
        
    print(f'{num_bytes if args.c or args.filename else ""}   {num_lines if args.l or args.filename else ""}   {num_words if args.w or args.filename else ""}   {num_characters if args.m or args.filename else ""}  {args.filename}')


