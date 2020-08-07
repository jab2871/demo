#!/usr/bin/env python

import sys

def dog():
    print("woof")

def main():
    """Main Function
    :returns: TODO

    """
    if len(sys.argv) > 1 and sys.argv[1] == "dog":
        dog()
    else:
        print("HELLO WORLD")

if __name__ == "__main__":
    main()
