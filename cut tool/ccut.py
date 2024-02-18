import csv 
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-f', type=int,nargs='+',help='the column index to read from ')
parser.add_argument('-d', type=str, help="specify the delimeter to use in reading the file")
parser.add_argument('-filename', type=str, help='the name of the file tobe opened')
args = parser.parse_args()
dlmtr = args.d if args.d else '\t'
multiple = True if len(args.f) > 1 else False

def read_mutiple(list, line,):
    multi_cols = []
    for element in list:
        multi_cols.append(line[element])
    return multi_cols

def print_cols(cols,multiple=False, n=0):
    if not multiple:
        for item in cols:
            print(item)
    for row in cols:
        print('')
        for element in row:
            print(element,end='\t')
    print('')

if not sys.stdin.isatty():
    fileobj = sys.stdin.readlines()
    cols_read = []
    for line in fileobj:
        cols_read.append(read_mutiple(args.f, line.split()))
    print_cols(cols_read,multiple=multiple)
else:
    with open(args.filename) as tsvfile:
        cols_read = []
        for line in csv.reader(tsvfile,delimiter=dlmtr):
            cols_read.append(read_mutiple(args.f, line))
        print_cols(cols_read,multiple=multiple)