import re
from TEXT_CLEANER import CLEAN

def GET_CONTENT(soup):
    for script in soup(["script", "style"]):  # Скрипты лезут в get_text()
        script.decompose()  #
    N = ['comm', 'footer', 'inject'] # Удаляемые части дерева, обычно содержат кучу ненужной нам информации
    for j in N:
        for i in soup.find_all(class_=re.compile(j)): # Удаляется всё, что может содержать потенциально ненужную информацию. И то, что потенциально есть.
            i.decompose()
    text = ''
    M = ['p', 'br'] #Теги, по которым искать. Опционально. Пусть будет именем\именами искомого тега.
    for x in M:
        for i in soup.find_all('div'): #Ищем среди всех дивов
            h = 0 # Обнуляем счетчик
            for j in i.contents: # Смотрим *детей* просмартиваемого дива
                if j.name == x:
                    h += 1
            if h > 2: # Если внутри тега есть два ребёнка-тега с искомым именем - записать текст тег с текстом.
                text += str(i)
    return(CLEAN(text))

