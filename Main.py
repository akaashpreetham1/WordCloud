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

import DocumentRead as dr
import WordCount as wc
import WebScraper as ws
import DataVisualization as dv
import UserInterface as UI

def main():
    
    #url = input("Enter the url of blog: ")
    
    
    app = UI.App()
    url = str(app.returnURL())
    
    print("URL = " + str(url) + "\n------")
    posts = ws.scrapeBlog(url)
    print("Scrapingok \n------")
    
    for post in posts:
        print("into the loop")
        filename = ws.scrapePost(post)
        
        
        #path = input("Enter the name of the file: ")
        #The League of Extraordinary Gentlemen – Akaash Preetham
        text = dr.readDoc(filename)
        
        #text = input("Enter text here at main: ")
        
        #sortedWords = wc.countWords(text)
        #for word in sortedWords:
        #    print(str(word[0]) + '-' + str(word[1]))
        
        #wordcount = wc.countWords(text)
        #dv.visualizeData(wordcount)
        dv.visualizeData(text, filename)

if __name__ == "__main__":
    main()
