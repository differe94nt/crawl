from urllib import urlopen

def get_page(url):
    try:return urlopen(url).read()
    except:return ''

def get_next_link(page):
    start_link=page.find('<a href=')
    if start_link==-1:return None,0
    start_quote=page.find('"',start_link)
    end_quote=page.find('"',start_quote+1)
    link=page[start_quote+1:end_quote]
    return link,end_quote

def get_all_links(page):
    links=[]
    while True:
        link,endpos=get_next_link(page)
        if link:
            links.append(link)
            page=page[endpos:]
        else:return links

tocrawl=['http://msn.com.tw']
crawled=[]
while tocrawl:
    link=tocrawl.pop()
    page=get_page(link)
    tocrawl+=get_all_links(page)
    crawled.append(link)
    if len(crawled)>9:break
print crawled