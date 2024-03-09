import argparse
import sys

class UniqTool:
    def __init__(self,filename):
        self.filename = filename
        self.counts = dict() 
        self.repeated = set()
        self.input_lines = self._read_lines()

    def _read_lines(self):
        if not sys.stdin.isatty():
            return sys.stdin.readlines()
        else:
            try:
                with open(self.filename) as f:
                    return f.readlines()
            except FileNotFoundError:
                print("Error: file not found")
                sys.exit(1)
    def _process_lines(self):
        i = 0
        
        self.lines = self.input_lines
        seen_line = []
        while i < len(self.lines):
            line = self.lines[i]
            if line not in seen_line:
                seen_line.append(line)
                self.counts[self.lines[i]]= 1
                i += 1
            else:
                self.counts[self.lines[i]] += 1
                self.repeated.add(self.lines[i])
                self.lines.pop(i)

    def _process_output(self, count=False,repeat=False, unique=False):
        if not any([count, repeat, unique]):
            for line in self.lines:
                print(line.strip('\n'))
        elif count:
            for value in self.counts:
                print(self.counts[value], ' ', value.strip('\n'))
        elif repeat:
            for line in set(self.repeated):
                print(line.strip('\n'))
        elif unique:
            lst = [line for line in self.lines if line not in self.repeated]
            for line in lst:
                print(line.strip('\n'))

    def process(self, count=False, repeat=False, unique=False):
        self._process_lines()
        self._process_output(count=count, repeat=repeat, unique=unique)


def main():
    parser  = argparse.ArgumentParser(description=" A program that output unique occurences and counts in a text file")

    parser.add_argument('filename', nargs='?',help="the name of the file to be processed")
    parser.add_argument('-o', help="the name of the file to save the output to ")
    parser.add_argument('-s',help='determines whether the program should read from standard input')
    parser.add_argument('-c', action='store_true', help= "Show the appearance statistics of the file")
    parser.add_argument('-d', action='store_true', help="outputs only repeated lines")
    parser.add_argument('-u',action='store_true', help='outputs only unique lines')
    args = parser.parse_args()

    if args.s == '-' and  not sys.stdin.isatty():
        print('Error: no file detected from standard input')
        sys.exit(1)


    print(args.o)
    # uniq = UniqTool(args.filename)
    # uniq.process(repeat=args.d)
if __name__ == '__main__':
    main()