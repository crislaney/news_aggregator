import feedparser


def first_five(feed):
    lst = []
    feed1 = feed
    
    for i in range(5):
        lst.append(feed[i])

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


    bbc5 = first_five(bbc.entries)
    cnn5 = first_five(cnn.entries)
    wash5 = first_five(wash.entries)

    sources = [bbc5, cnn5, wash5]

    title(sources)
    



main()
    
