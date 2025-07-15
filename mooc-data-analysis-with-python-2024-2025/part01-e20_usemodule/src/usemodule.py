#!/usr/bin/env python3

# Don't modify the below hack
try:
    from src import triangle 
except ModuleNotFoundError:
    import triangle

def main():
  print(f"Hypotenuse: {triangle.hypotenuse(8, 6)}")
  print(f"Area: {triangle.area(4, 8)}")

if __name__ == "__main__":
    main()
