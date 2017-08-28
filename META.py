from TEXT_CLEANER import CLEAN
def GET_META(soup):
    M = ""
    if soup.find('title').string != None:
        M += soup.find('title').string
    for tag in soup.find_all("meta"):
        if tag.attrs.get("name") == "description" or tag.attrs.get("name") == "keywords":
            if tag.attrs.get("content") != None:
                M += tag.attrs.get("content")
    return(CLEAN(M))