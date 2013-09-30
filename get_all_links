def get_all_links(page):
    links=[]
    while True:
        link,endpos=get_next_target(page)
        if link:
            links=links+link
            page=page[endpos:]
        else:return links
