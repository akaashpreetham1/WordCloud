# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 21:36:55 2021

@author: Akaash Preetham
"""

"""
Making a GUI for the wordcloud application using Tkinter
"""

from tkinter import *

#def getURL():
    
class App:
    
    def __init__(self):
        self.window = Tk()
        
        self.description = Label(text = "Enter the URL") 
        #self.description.pack()
        
        self.entry = Entry()
        #self.entry.pack()
        
        """
        def printurl():
            url = entry.get()
            print(url)
            window.destroy()
            return url
        """
        
        self.submit = Button(text = "Submit", command = self.getURL)
        
        self.pack()
        #self.submit.pack()
        
        #uri = entry.get()
    
        #self.window.mainloop()
    def pack(self):
        self.description.pack()
        self.entry.pack()
        self.submit.pack()
        self.window.mainloop()
        
    def getURL(self):
        self.url = self.entry.get()
        #print(self.url)
        self.destroy()
        
    def destroy(self):
        self.window.destroy()
        
    def generate(self):
        
        pass
    
    def returnURL(self):
        return self.url
    
    
    #print(uri + "Yolo")