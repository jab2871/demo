#!/usr/bin/env python

import sys

def dog():
    print("woof")

def cat():
    print("Meow")

def cow():
    print("moo")

def main():
    """Main Function
    :returns: TODO

    """
    if len(sys.argv) > 1 and sys.argv[1] == "dog":
        dog()
    elif len(sys.argv) > 1 and sys.argv[1] == "cat":
        cat()
    elif len(sys.argv) > 1 and sys.argv[1] == "cow":
        cow()
    else:
        print("HELLO WORLD")

if __name__ == "__main__":
    main()
