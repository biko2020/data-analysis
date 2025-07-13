#!/usr/bin/env python3

def find_matching(L, pattern):
    positions =[]
    for index, word in enumerate(L):
        if pattern in word:
            positions.append(index)

    return positions

def main():
    print(find_matching(["sensitive", "engine", "rubbish", "comment"], "en"))

if __name__ == "__main__":
    main()
