#todo: store new chapters
import feedparser
import re

mangafox = 'https://feeds2.feedburner.com/mangafox/latest_manga_chapters'
mangahere = 'http://feeds.feedburner.com/207/oIeP'
mangacow = 'http://mngcow.co/manga-rss'
mangapark = 'https://mangapark.me/rss/latest.xml'
sites = [mangafox, mangahere, mangacow, mangapark]
current = {'God of Martial Arts': 42.2, 'Tales of Demons and Gods': 166, 'Wu Dong Qian Kun': 64, 'Red Storm': 278, 'Shokugeki no Soma': 254,
           'Haikyuu': 293, 'Douluo Dalu': 204, 'Doupo Cangqiong': 215}

for eachSite in sites:
    data = feedparser.parse(eachSite) #grab rss feed
    for eachEntry in data.entries:
        for eachCurrent in current:
            if eachCurrent in eachEntry.title:
                if float(re.sub("[^0-9]+(\.[0-9])", "", eachEntry.title.split(' ')[-1])) > current[eachCurrent]:
                    print(eachEntry.title + ' ' + eachEntry.link)
