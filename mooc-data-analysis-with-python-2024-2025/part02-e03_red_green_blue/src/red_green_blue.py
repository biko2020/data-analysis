#!/usr/bin/env python3

import re

def red_green_blue(filename="src/rgb.txt"):
    result = []
    with open(filename) as file:
        next(file)
        for line in file:
            match = re.match(r'\s*(\d+)\s+(\d+)\s+(\d+)\s+(.*\S)', line)
            if match:
                red, green, blue, color = match.groups()
                result.append(f"{red}\t{green}\t{blue}\t{color}")
    return result



def main():
    read_list = red_green_blue()
    for line in read_list[:5]:
        print(line)

if __name__ == "__main__":
    main()
