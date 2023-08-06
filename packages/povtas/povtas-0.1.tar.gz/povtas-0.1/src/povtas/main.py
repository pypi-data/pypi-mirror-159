#!/usr/bin/env python
import re

def main():
    string = input("Insert a word: ")
    string = re.sub("r", "v", string)
    string = re.sub("R", "V", string)

    print("There:", string, end="\n\n")