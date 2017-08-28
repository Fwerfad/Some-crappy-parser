from os import path
from os import makedirs
import sys
import time
sys.path.append(path.abspath("")) # Необходимо для сохранения результатов
from URL_GRABBER import GET_HTTP
from HTML_PARSER import PARSER
from TEXT_GRABBER import GRAB_TEXT
from META import GET_META
from HTML_CONTENT import GET_CONTENT

if not path.exists("Output"): # Создание места для хранения результатов
    makedirs("Output")
D = open('input.txt','r') # Чтение текстовика
Z = D.readlines()
for x in Z:
    H = 0  # Переменная для названий
    if not path.exists(path.abspath("Output" + "\\" + x)): # Еще одна папка, уже для ключевого слова
        makedirs("Output" + "\\" + x)
    for z in GET_HTTP(x):
        try:
            soup = PARSER(z)
            meta = z + '\n' + GET_META(soup)
            text = GRAB_TEXT(soup)
            Content = GET_CONTENT(soup)
            if meta != "404 Not Found" and text != "": # Если мета 404 страницы или нету текста
                H += 1
                if not path.exists(path.abspath("Output" + "\\" + x + "\\" + str(H))): #Место хранения уже готовой информции
                    makedirs(path.abspath("Output" + "\\" + x + "\\" + str(H)))
                with open(path.abspath("Output" + "\\" + x) + '\\' + str(H) + "\\" + "Body" + ".html", "wb") as Sf:
                    Sf.write(soup.prettify('utf-8'))
                    Sf.close()
                with open(path.abspath("Output" + "\\" + x) + '\\' + str(H) + "\\" + "Text" + ".txt", "w") as Sf:
                    Sf.write(text)
                    Sf.close()
                with open(path.abspath("Output" + "\\" + x) + '\\' + str(H) + "\\" + "Meta" + ".txt", "w") as Sf:
                    Sf.write(meta)
                    Sf.close()
                with open(path.abspath("Output" + "\\" + x) + '\\' + str(H) + "\\" + "Content" + ".html", "w") as Sf:
                    Sf.write(Content)
                    Sf.close()
                time.sleep(2)
        except (TimeoutError, UnicodeEncodeError) as e: # Если сервер не отвечает или юникод теряет символы..ну, надо будет подумать над этим
            continue
        time.sleep(1)