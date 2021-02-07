# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 18:58:43 2021

@author: Akaash Preetham
"""

"""
This code will:
    1. Take a document path
    2. Read file contents
    3. Return the text as a variable
"""
"""

with open("Blog.txt", 'w') as writer:
    writer.write("Hello,hello,world;wow wow,hello")

    #for i in range(10):
        #writer.write("Hello world " + str(i+1) + '\n')
"""

path = "Contents/"

def getProperFileName(title):
    """
    Removes special characters from file name
    """
    filename = ""
    for character in title:
        if character.isalnum():
            filename += character
    return filename

def createDoc(filename):
    #path = filename + ".txt"
    try:
        file = open(path + filename, "w+")
    finally:
        file.close()

def writeDoc(filename, content):
    #path = filename + ".txt"
    try:
        writer = open(path + filename, "a+")
        print("---------\nWriting into " + filename + "\n------\n")
        writer.write(content)
    finally:
    #with open(filename, 'a+') as writer:
        #writer.write(content)
        writer.close()

def readDoc(filename):
    try:
        reader = open(path + filename, "r")
    #with open(path, 'r') as reader:
        contents = reader.read()
    finally:
        reader.close()
        return contents