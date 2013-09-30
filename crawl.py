tocrawl=['http://msn.com']
crawled=[]
while tocrawl:
    url=tocrawl.pop()
    page=get_page(url)
    tocrawl+=get_links(page)
    crawled+=url
print crawled
