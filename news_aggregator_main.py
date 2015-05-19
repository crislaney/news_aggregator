import feedparser
from listmaker import *
from jrewrite import *
from lst_check import *
from bs4 import *

def build_top(sites, frst, keyword_master):

    for item in sites:
        fin_list = list_check(keyword_master, item, frst)
        return(fin_list[1])


#prnt_title takes a list of lists of entries
#prints out all entries from each website list
#returns nothing
def prnt_title(sources):
    lst = sources
    
    for i in range(len(lst)):
        print("({}) {}".format(i+1, lst[i].title))
            


def main():

    bbc = feedparser.parse("http://feeds.bbci.co.uk/news/technology/rss.xml")
    cnn = feedparser.parse("http://rss.cnn.com/rss/edition.rss")
    wash = feedparser.parse("http://www.wsj.com/xml/rss/3_7085.xml")

    bbc5 = first_five(bbc.entries)
    pre_cnn = first_fif(cnn.entries)
    pre_wash = first_fif(wash.entries)
    sites = [pre_cnn, pre_wash]
    fin_list = []

    keyword_master = flatten(word_lists(remove_commons(title(bbc5))))
    
    fin_list = build_top(sites, bbc5, keyword_master)
    
    prnt_title(fin_list)

##    story_links = input("Please type the numbers of each story you would like to read more about seperated by spaces \n")
##    link_list = [int(s) for s in story_links.split(",")]



main() 
    
