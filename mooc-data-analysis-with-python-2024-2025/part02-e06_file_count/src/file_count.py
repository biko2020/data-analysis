#!/usr/bin/env python3

import sys

def file_count(filename):
    number_of_line =0
    number_of_word =0
    number_of_character= 0
    with open(filename, 'r') as file:
        for line in file:
            number_of_line +=1
            words = line.split()
            number_of_word += len(words)
            number_of_character += len(line)
    return (number_of_line, number_of_word, number_of_character)

def main():
    for filename in sys.argv[1:]:
        lines, words, chars = file_count(filename)
        print(f"{lines}\t{words}\t{chars}\t{filename}")

if __name__ == "__main__":
    main()
