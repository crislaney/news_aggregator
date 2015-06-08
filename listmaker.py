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

def lists_overlap(list1, list2): #takes 2 lists
    overlap_bool = bool(set(list1) & set(list2))
    overlap_int = len(set(list1) & set(list2))

    if overlap_int > 2:
        return(True)
    else:
        return(False)

     #returns the overlap_int, which is the number of elements in both list1 and list2, and overlap_bool, a boolean (True means they have elements in common, False means they do not).
