import re
from TEXT_CLEANER import CLEAN
def GRAB_TEXT(soup):
    for script in soup(["script", "style"]):  # kill all script and style elements
        script.extract()  # rip it out
    N = ['comm', 'footer', 'inject']  # Удаляемые части дерева, обычно содержат кучу ненужной нам информации
    for j in N:
        for i in soup.find_all(class_=re.compile(j)):
            i.decompose()
    text = ""
    M = ['p', 'br'] #Теги, по которым искать. Опционально.
    for x in M:
        for i in soup.find_all('div'): #Ищем все дивы и смотрим кол-во тегов, содержащих текст.
            h = 0
            for j in i.contents:
                if j.name == x:
                    h += 1
            if h > 2:
                text += i.get_text() + "\n"
    return(CLEAN(text))
