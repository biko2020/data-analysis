#!/usr/bin/env python3

def reverse_dictionary(d):
    reversed_dict = {}
    for english_word, finnish_list in d.items():
        for finnish_word in finnish_list:
            if finnish_word not in reversed_dict:
                reversed_dict[finnish_word]=[]
            reversed_dict[finnish_word].append(english_word)
    return reversed_dict

def main():
    d={
       'move': ['liikuttaa'], 
       'hide': ['piilottaa', 'salata'], 
       'six': ['kuusi'], 
       'fir': ['kuusi']
       }
    reversed_d = reverse_dictionary(d)
    print(reversed_d) 

if __name__ == "__main__":
    main()
