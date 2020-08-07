#!/usr/bin/env python

import sys

def cat():
    print("Meow")

def main():
    """Main Function
    :returns: TODO

    """
    if len(sys.argv) > 1 and sys.argv[1] == "cat":
        cat()
    else:
        print("HELLO WORLD")

if __name__ == "__main__":
    main()
