import feedparser
from listmaker import *
from jrewrite import *
from lst_check import *

#parameters: list of sites, list of sites, keywords
#operation: cross checks each story with keyword master, getting rid of any repetitions
#return: list of sites with no repetitions
def build_top(sites, frst, keywords):
        
    for item in sites:

        fin_list = list_check(keywords, item, frst)
        
        if item == sites[0]:
            fin_list[1].append(sites[1][0])
                       
    return(fin_list[1])

#parameters: a list of sites
#return: the links to the article
def get_links(sites):
    for item in sites:
        print(item.title)
        print(item.link, "\n")

#parameters: the list of all 15 website entries, and a list of numbers
#return: creates a list of selected sites
def selected_sites(fin_list, link_list):
    selected = []
    for i in range(len(link_list)):
        selected.append(fin_list[link_list[i]-1])

    return(selected)

#prnt_title takes a list of lists of entries
#prints out all entries from each website list
#returns nothing
def prnt_title(sources):
    lst = sources
    
    for i in range(len(lst)):
        print("({}) {}".format(i+1, lst[i].title))
            


def main():

    x = True

    while x == True:
        
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
        
        print(" ")
        choice = input("Would you like to read more, refresh, or stop? \n")

        if choice.lower() == "read more" or choice.lower() == "read":
            print("\n")
            
            story_links = input("Please type the numbers of each story you would like the link to, seperated by a coma and a space \n")
            link_list = [int(s) for s in story_links.split(", ")]

            select_list = selected_sites(fin_list, link_list)

            get_links(select_list)

            if input("refresh or stop? \n").lower() == "refresh":
                x = True
            else:
                x = False


        elif choice.lower() == "refresh":
            print("\n")
            x = True

        elif choice.lower() == "stop":
            print("\n")
            x = False

        else:
            print("That is not an option. Refreshing page...")

    



main() 
    
