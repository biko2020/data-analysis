#!/usr/bin/env python3

def merge(L1, L2):
    i,j=0,0
    merged = []
    while i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            merged.append(L1[i])
            i+=1
        else:
            merged.append(L2[j])
            j+=1
    merged.extend(L1[i:])
    merged.extend(L2[j:])
    return merged

def main():
    L1=sorted([1,2,2])
    L2=sorted([2,5,8]) 
    print("Merged:", merge(L1, L2))

if __name__ == "__main__":
    main()
