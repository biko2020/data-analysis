#!/usr/bin/env python3


def main():
    i=1
    while i <= 10:
        j=1
        while j <=10:
            print(f"{i*j:4}", end="")
            j+=1
        print()
        i+=1

if __name__ == "__main__":
    main()
