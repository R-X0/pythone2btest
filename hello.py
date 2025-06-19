#!/usr/bin/env python3

def main():
    name = input("What's your name? ")
    if name.strip():
        print(f"Hello, {name}! Welcome to Python!")
    else:
        print("Hello, World!")
    
    print("Have a great day!")

if __name__ == "__main__":
    main()