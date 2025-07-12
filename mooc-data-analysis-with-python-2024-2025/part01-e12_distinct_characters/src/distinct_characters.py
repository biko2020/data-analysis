#!/usr/bin/env python3

def distinct_characters(L):
    characters={}
    for character in (L):
        characters[character] = len(set(character))
    return characters

def main():
    print(distinct_characters(["check", "look", "try", "pop"]))

if __name__ == "__main__":
    main()
