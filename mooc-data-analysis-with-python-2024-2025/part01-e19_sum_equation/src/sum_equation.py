#!/usr/bin/env python3

def sum_equation(L):
    if not L:
        return "0 = 0"
    sumofelements = sum(L)
    reslut = " + ".join(str(x) for x in L) + " = " + str(sumofelements)
    return reslut

def main():
    print(sum_equation([1,5,7]))

if __name__ == "__main__":
    main()
