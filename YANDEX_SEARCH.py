import httplib2
from bs4 import BeautifulSoup
import re
def GET_HTTP_YANDEX(x): # Функция получения ссылок по заданому слову в поисковике
    key = "03.160401204:e30c87055db4234f0562a0ac4d383052"
    http = httplib2.Http()  # А это хттплиб2, ага. Он работает по-другому. Ваш К.О. p.s. Это для http1, http2 не поддерживает httplib2, для http2 нужен hyper, см. поиск гугла.
    response, content = http.request('https://yandex.com/search/xml?l10n=en&userы=fwerfad&key=' + key + "&query=" + str(x), 'GET')
    soup = BeautifulSoup(content, "lxml")
    M = [] # Массив ссылок
    for link in soup.find_all("url"):  # h2 - в яндексе там находится ссылка на статью
        S = link.string
        T = True  # Нужна для проверки
        if S != None:  # Уборка мусора
            m = ['search', 'wikipedia', 'youtube', 'zoon', 'syl']  # Массив ключевых слов, позволяющих отбрасывать определенные результаты поиска. Вводить часть нежелаемого ресурса.
            for i in m:
                if i in S:
                    T = False  # Уборка мусора х2
            if T == True:
                M.append(S)
    return(M)