from TEXT_CLEANER import CLEAN

def GET_META(soup):
    M = "" # Стринг, содержащий искомую информацию.
    m = ["description", "keywords"] # Массив с искомыми тегами
    s = soup.find("title")
    if s != None and s.string != None: # Если титульный тег не равен нулю - записываем его.
        M += soup.find("title").string
    for tag in soup.find_all("meta"): # Если в мета тегах есть искомые теги - записать их содержимое
        if tag.attrs.get("name") in m:
            if tag.attrs.get("content") != None:
                M += tag.attrs.get("content")
    return(CLEAN(M))