#!/usr/bin/env python3

def positive_list(L):

    return (list(filter(lambda number:number > 0, L)))

def main():
    L = [2,-2,0,1,-7]
    print(positive_list(L))

if __name__ == "__main__":
    main()
