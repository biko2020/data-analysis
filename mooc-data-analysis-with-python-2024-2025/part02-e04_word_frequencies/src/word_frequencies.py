#!/usr/bin/env python3


def word_frequencies(filename):
    frequencies = {}
    with open(filename, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                cleaned = word.strip("""!"#$%&'()*,-./:;?@[]_""").lower()
                if cleaned:
                    frequencies[cleaned] = frequencies.get(cleaned, 0) + 1
    return frequencies

def main():
    frequencies = word_frequencies("src/alice.txt")
    for word, value in sorted(frequencies.items()):
        print(f"{word}\t{value}")

if __name__ == "__main__":
    main()
