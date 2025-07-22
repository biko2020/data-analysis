#!/usr/bin/env python3

import re


def file_listing(filename="src/listing.txt"):
    result = []
    pattern = re.compile(
        r'^\S+\s+\d+\s+\S+\s+\S+\s+(\d+)\s+(\w{3})\s+(\d+)\s+(\d+):(\d+)\s+(.*)$'
        )
    with open(filename) as file:
        for line in file:
            mo = pattern.match(line)
            if mo:
                size =int(mo.group(1))
                month = mo.group(2)
                day = int(mo.group(3))
                hour = int(mo.group(4))
                minute = int(mo.group(5))
                file_name = mo.group(6)
                result.append((size,month,day,hour, minute, file_name))
    return result
def main():
    for item in file_listing():
        print(item)

if __name__ == "__main__":
    main()
