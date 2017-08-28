import re
from TEXT_CLEANER import CLEAN
def GET_CONTENT(soup):
    for script in soup(["script", "style"]):  # kill all script and style elements
        script.extract()  # rip it out
    N = ['comm', 'footer', 'inject']
    for j in N:
        for i in soup.find_all(class_=re.compile(j)):
            i.decompose()
    M = ['p', 'br']
    text = ''
    for x in M:
        for i in soup.find_all('div'):
            h = 0
            for j in i.contents:
                if j.name == x:
                    h += 1
            if h > 2:
                text += str(i)
    return(CLEAN(text))

