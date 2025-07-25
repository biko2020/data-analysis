#!/usr/bin/env python3

import sys
import math

def summary(filename):
    numbers = []
    with open(filename, 'r') as file:
        for line in file:
            try:
                num = float(line.strip())  
                numbers.append(num)
            except ValueError:
                continue  
    
    if not numbers: 
        return (0.0, 0.0, 0.0)
    
    
    total_sum = sum(numbers)
    
    # Calculate average
    count = len(numbers)
    average = total_sum / count if count > 0 else 0.0
    
    if count > 1:
        mean_diff_squared = sum((x - average) ** 2 for x in numbers) / (count - 1)
        stddev = math.sqrt(mean_diff_squared)
    else:
        stddev = 0.0  
    
    return (total_sum, average, stddev)

def main():
    for filename in sys.argv[1:]:
        total_sum, average, stddev = summary(filename)
        print(f"File: {filename} Sum: {total_sum:.6f} Average: {average:.6f} Stddev: {stddev:.6f}")

if __name__ == "__main__":
    main()
