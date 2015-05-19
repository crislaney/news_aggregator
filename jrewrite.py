from listmaker import *
from lst_check import *

#def flatten taken from stack overflow
def flatten(input):
    ret = []
    if not isinstance(input, (list, tuple)):
        return[input]
    
    for i in input:
        if isinstance(i, (list, tuple)):
            ret.extend(flatten(i))
        else:
            ret.append(i)
    return(ret)


def list_check(keywords1, entries, fin_list):
    clean_list = word_lists(remove_commons(title(entries)))
    keywords = flatten(keywords1)
    
    
    if len(fin_list) == 10 or len(fin_list) == 15 or len(clean_list) == 0:
        up_values = [keywords, fin_list]
        return(up_values)

    elif lists_overlap(keywords, clean_list[0]) == False:
        fin_list.append(entries[0])
        keywords.append(clean_list[0])
        return(list_check(keywords, entries[1:], fin_list))

    elif lists_overlap(keywords, clean_list[0]) == True:
        return(list_check(keywords, entries[1:], fin_list))

def first_fif(feed):
    lst = []
    feed1 = feed
    
    for i in range(10):
        lst.append(feed[i])

    return(lst)

def first_five(feed):
    
    lst = []
    feed1 = feed
    
    for i in range(15):
        lst.append(feed[i])

    return(lst)


    

    
