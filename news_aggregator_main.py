import feedparser


def first_five(feed, lst):
    
    if len(lst) >= 5:
        return(lst)
    
    else:
        lst.append(feed[0])
        lst = first_five(feed[1:], lst)
        return(lst)
        

def title(sources):
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
   
    bbc5 = first_five(bbc.entries, lst)
    cnn5 = first_five(cnn.entries, lst2)
    wash5 = first_five(wash.entries, lst3)

    sources = [bbc5, cnn5, wash5]
    
    title(sources)
    



main()
    
