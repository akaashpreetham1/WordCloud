# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 14:23:30 2021

@author: Akaash Preetham
"""

#import numpy as np
#import pandas as pd
import matplotlib.pyplot as plt
#import WordCount
from wordcloud import WordCloud, STOPWORDS
#import os

#temp = pd.DataFrame.from_dict(sortedWords, columns = ['Word', 'No. of occurrences'])

def visualizeData(text, filename):
   
    #countDF = pd.DataFrame.from_dict(wordcount, orient = 'index', columns =['Count'])
    #countDF.index.name = 'Word'
    #countDF = countDF.sort_values(by = ['Count'], ascending = False)
    #print(countDF.index)

    stopwords = list(STOPWORDS) #+ ["know", "Venom", "Akaash", "Preetham", "Yeah", "Okay", "Will", "Know", "Media omitted"]

    #for val in countDF.Count:
    #    val = str(val)
    
    wordcloud = WordCloud(width = 800, height = 800, background_color = 'white', stopwords = stopwords, min_font_size = 10).generate(text)

    plt.figure(figsize = (8,8), facecolor = None)
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.tight_layout(pad = 0)
    #plt.show()   
    path = "WordClouds/"
    print("-----\nPlotting " + filename + '.png\n-----\n')
    plt.savefig(path + filename + '.png')

    #topFive = countDF.head()
    #print(countDF.head())
    #topFive.plot.bar()
    #fig = plt.figure()
    #ax = fig.a
    
    
    