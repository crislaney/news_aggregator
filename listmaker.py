import feedparser
import re

def title(sources):  #creates list of titles
    lst = sources
    list_of_titles = []

    for i in range(len(sources)):
        list_of_titles.append(sources[i].title)

    return list_of_titles

def remove_commons(titles): #gets rid of common words in the headings, such as "on" and "it"
 
    badwords = ["be","of","it","on", "and", "the", "in", "says", "must", "to"]

    up_titles = []
    
    for item in titles:
        
        remove = '|'.join(badwords)
        regex = re.compile(r'\b('+remove+r')\b', flags=re.IGNORECASE)
        out = regex.sub("", item)

        up_titles.append(out)
    
    
            
    return(up_titles)

def word_lists(titles):    #creates a list of lists of words from each title
    final = []
    for item in titles:
        words = []
        item.split(" ")
        final.append(item.split(" ")) #splitting by " " returns a list of words seperated by spaces
    return(final)

##def listmaker():
##    bbc = feedparser.parse("http://feeds.bbci.co.uk/news/technology/rss.xml")
##    cnn = feedparser.parse("http://rss.cnn.com/rss/edition.rss")
##    wash = feedparser.parse("http://www.wsj.com/xml/rss/3_7085.xml")
##
##    bbc5 = first_five(bbc.entries)
##    cnn5 = first_five(cnn.entries)
##    wash5 = first_five(wash.entries)
##    sources = [bbc5, cnn5, wash5]
##    
##    titles = title(sources)
##
##    remove_commons(titles)
##   
##    titles = word_lists(titles) #this is the list of lists of words for each heading
##
##    print(titles[0])
##
##listmaker()
