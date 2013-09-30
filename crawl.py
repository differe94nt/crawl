tocrawl=['http://msn.com']
crawled=[]
while tocrawl:
    link=tocrawl.pop()
    page=get_page(link)
    tocrawl.append(get_all_links(page))
    crawled.append(link)
print crawled
