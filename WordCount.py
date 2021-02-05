# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 20:30:22 2021

@author: Akaash Preetham
"""

"""
This code will 
1. make a list of all words used in a piece of text
2. keep a count of each word's occurrence
3. display them in descending order of word count
"""

def countWords(text):
    #text = input("Enter text here: ")
    #text = "hello world world hello world babe"
    
    words = text.casefold().split(' ')
    wordcount = {}
    
    for word in words:
        if word in wordcount:
            wordcount[word] += 1
        else:
            wordcount[word] = 1
    
    results = sorted(wordcount.items(), key = lambda kv:(kv[1], kv[0]), reverse = True)
    for result in results:
        print(result[0])
