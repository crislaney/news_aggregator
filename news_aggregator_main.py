import feedparser
from bs4 import *


#accepts an entree from one of the websites
#returns a list of entries (5 for now. Should make user adjustable)
def first_five(feed, lst):
    
    if len(lst) >= 5:
        return(lst)
    
    else:
        lst.append(feed[0])
        lst = first_five(feed[1:], lst)
        return(lst)
        

#prnt_title takes a list of lists of entries
#prints out all entries from each website list
#returns nothing
def prnt_title(sources):
    lst = sources
    
    for i in range(len(sources)):
        for j in range(len(sources[i])):

            print(sources[i][j].title)
            


def main():
    bbc = feedparser.parse("http://feeds.bbci.co.uk/news/technology/rss.xml")
    cnn = feedparser.parse("http://rss.cnn.com/rss/edition.rss")
    wash = feedparser.parse("http://www.wsj.com/xml/rss/3_7085.xml")

    lst = []
    lst2 = []
    lst3 = []
    #bbc.entries[0].link HOW TO ACCESS LINKS
    bbc5 = first_five(bbc.entries, lst)
    cnn5 = first_five(cnn.entries, lst2)
    wash5 = first_five(wash.entries, lst3)

    sources = [bbc5, cnn5, wash5]

    
main()
    
