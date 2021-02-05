# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 21:08:17 2021

@author: Akaash Preetham
"""

"""
1. Input document
2. Find most used words
3. Display
"""

import WordCount as wc


def main():
    
    text = input("Enter text here at main: ")
    wc.countWords(text)

if __name__ == "__main__":
    main()
