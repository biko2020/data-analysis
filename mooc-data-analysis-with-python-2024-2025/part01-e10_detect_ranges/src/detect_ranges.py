#!/usr/bin/env python3

def detect_ranges(L):
    L = sorted(L)
    result = []
    i= 0
    while i < len(L):
        start =L[i]
        end = start +1 
        while i + 1 < len(L) and L[i + 1] == L[i] +1:
            i+=1
            end = L[i]+1
        if end > start +1:
            result.append((start, end))
        else:
            result.append(start)
        i+=1
    return result

def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print(L)
    print(result)

if __name__ == "__main__":
    main()
