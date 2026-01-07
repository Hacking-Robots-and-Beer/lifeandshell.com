import feedparser
import json

rss_url = 'https://feed.podbean.com/devsecops/feed.xml'
feed = feedparser.parse(rss_url)


podcasts=[]
if feed.status == 200:
    f = open("/code/hugo/data/podcast.json", "w")
    f.write(json.dumps(feed.entries))
    f.close()    
    
    
    #for entry in feed.entries:
    #    print(entry)
    #    print("#######")
        

else:
    print("Failed to get RSS feed. Status code:", feed.status)