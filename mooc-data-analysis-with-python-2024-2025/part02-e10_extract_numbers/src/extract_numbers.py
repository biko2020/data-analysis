#!/usr/bin/env python3

def extract_numbers(s):
    lists = []
    for word in s.split():
        try:
            lists.append(int(word))
        except Exception:
            try:
                lists.append(float(word))
            except Exception:
                continue

    return lists

def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))

if __name__ == "__main__":
    main()
