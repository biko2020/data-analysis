#!/usr/bin/env python3

def triple(i):
    return i * 3

def square(i):
    return i ** 2

def main():
    for j in range(1, 11):
        squ = square(j)
        trip = triple(j)
        if squ > trip:
            break
        print(f"triple({j})=={trip} square({j})=={squ}")
if __name__ == "__main__":
    main()
