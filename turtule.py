#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
show some striung
"""


def main():
    """main function"""
    STR = "this is a string"
    for cc in list(STR):
        print("ch: {} codepoint: {}".format(cc, hex(ord(cc))))


if __name__ == "__main__":
    main()
