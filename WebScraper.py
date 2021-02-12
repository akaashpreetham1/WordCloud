# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 21:34:45 2021

@author: Akaash Preetham
"""

"""
from urllib.request import urlopen

url = "https://preethamwhy.wordpress.com/2020/10/25/the-league-of-extraordinary-gentlemen/"

page = urlopen(url)

htmlBytes = page.read()
html = htmlBytes.decode("utf-8")

title_index = html.find("<title>")
start_index = title_index + len("<title>")
end_index  = html.find("</title>")
title = html[start_index : end_index]
print(title)
"""

from bs4 import BeautifulSoup
from urllib.request import urlopen
import DocumentRead as dr


def scrapeBlog(url):
    page = urlopen(url)
    #print("Into the func")
    
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    links = soup.find_all('a', class_ = 'post-thumbnail')
    posts = []
    for post in links:
        posts.append(post.get('href'))
    #for post in posts:
    #    print(post.get('href'))
    print("outta the func")
    return posts
    
def scrapePost(url):
    
    #url = "https://preethamwhy.wordpress.com/2020/10/25/the-league-of-extraordinary-gentlemen/"
    #words = ''
    print("----\nScraping " + url +"\n----\n")
    page = urlopen(url)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    #print(soup.title.text)
    filename = dr.getProperFileName(soup.title.text) + ".txt"
    #dr.createDoc(fileName)
    for tag in soup.find_all('div', class_ = 'entry-content'):
        #print(tag.text)
        dr.writeDoc(filename, tag.text)
    return filename
  
    #print(soup.body.text)
    #for p in soup.find_all("p")
    #    print(p.text)
    #s = soup.find_all("p")
    #print(s)
    #print(soup.get_text())