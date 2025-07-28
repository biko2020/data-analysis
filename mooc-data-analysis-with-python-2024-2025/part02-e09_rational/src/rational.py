#!/usr/bin/env python3
from math import gcd


class Rational:
    
    def __init__(self, numerator, denominator):
        common = gcd(numerator, denominator)
        self.numerator = numerator // common
        self.denominator = denominator // common
        if self.denominator < 0:
            self.numerator *= -1
            self.denominator *= -1

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
    
    def __repr__(self):
        return f"Rational({self.numerator}, {self.denominator})"
    
    def __add__(self, b):
        numerator = self.numerator * b.denominator + b.numerator * self.denominator
        denominator = self.denominator * b.denominator
        return Rational(numerator, denominator)
            
    def __sub__(self, b):
        numerator = self.numerator * b.denominator - b.numerator * self.denominator
        denominator = self.denominator * b.denominator
        return Rational(numerator, denominator)
    
    def __mul__(self, b):
        numerator = self.numerator * b.numerator
        denominator = self.denominator * b.denominator
        return Rational(numerator, denominator)
    
    def __truediv__(self, b):
        numerator = self.numerator * b.denominator
        denominator = self.denominator * b.numerator
        return Rational(numerator, denominator)
    
    def __eq__(self, b):
        return self.numerator == b.numerator and self.denominator == b.denominator

    def __lt__(self, b):
        return self.numerator * b.denominator < b.numerator * self.denominator

    def __gt__(self, b):
        return self.numerator * b.denominator > b.numerator * self.denominator


def main():
    r1 = Rational(1, 4)
    r2 = Rational(2, 3)
    print(r1)
    print(r2)
    print(r1 * r2)
    print(r1 / r2)
    print(r1 + r2)
    print(r1 - r2)
    print(Rational(1, 2) == Rational(2, 4))
    print(Rational(1, 2) > Rational(2, 4))
    print(Rational(1, 2) < Rational(2, 4))

if __name__ == "__main__":
    main()
