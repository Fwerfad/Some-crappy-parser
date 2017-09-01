from os import path
from os import makedirs
import sys
import time
sys.path.append(path.abspath("")) # Необходимо для сохранения результатов
from URL_GRABBER import GET_URL
from HTML_PARSER import PARSER
from TEXT_GRABBER import GRAB_TEXT
from META import GET_META
from HTML_CONTENT import GET_CONTENT

if not path.exists("Output"): # Создание места для хранения результатов
    makedirs("Output")
D = open('input.txt','r') # Чтение текстовика
Z = [i.replace('\n', '') for i in D.readlines()]
D = ""
for x in Z:
    d = ""
    H = 0  # Переменная для названий. Для каждого ключевого слова обнуляется.
    if not path.exists(path.abspath("Output" + "\\" + x)): # Еще одна папка, уже для ключевого слова
        makedirs("Output" + "\\" + x)
    for z in GET_URL(x):
        try:
            d = z + "\n"
            soup = PARSER(z) # Отпарсенная страница, полученная по ссылки из гугла\яндекса
            meta = z + '\n' + GET_META(soup) # Мета страницы, с ссылкой на страницу в начале
            text = GRAB_TEXT(soup) # Текст страницы
            Content = GET_CONTENT(soup) # Текст с тегами страницы
            if meta != "404 Not Found" and text != "": # Если мета 404 страницы или нету текста - мимо
                H += 1 # Счетчик для названия
                if not path.exists(path.abspath("Output" + "\\" + x + "\\" + str(H))): #Место хранения уже готовой информции
                    makedirs(path.abspath("Output" + "\\" + x + "\\" + str(H)))
                with open(path.abspath("Output" + "\\" + x) + '\\' + str(H) + "\\" + "Body" + ".html", "wb") as Sf: # Сама страница.
                    Sf.write(soup.prettify('utf-8'))
                    Sf.close()
                with open(path.abspath("Output" + "\\" + x) + '\\' + str(H) + "\\" + "Text" + ".txt", "w") as Sf: # Текст страницы
                    Sf.write(text)
                    Sf.close()
                with open(path.abspath("Output" + "\\" + x) + '\\' + str(H) + "\\" + "Meta" + ".txt", "w") as Sf: # Мета страницы
                    Sf.write(meta)
                    Sf.close()
                with open(path.abspath("Output" + "\\" + x) + '\\' + str(H) + "\\" + "Content" + ".html", "w") as Sf: # Текст страницы с тегами
                    Sf.write(Content)
                    Sf.close()
                with open(path.abspath("Output" + "\\" + x) + '\\' + str(H) + "\\" + "Urls" + ".txt", "w") as Sf: # Все ссылки с ключевого слова
                    Sf.write(Content)
                    Sf.close()
                D += text + "\n" +"\n"
                time.sleep(0.5)
        except (TimeoutError, UnicodeEncodeError) as e: # Если сервер не отвечает или юникод теряет символы..ну, надо будет подумать над этим
            continue
        time.sleep(1)
with open(path.abspath("Output\\All.csv"), "w") as Sf:
    Sf.write(D)
    Sf.close()