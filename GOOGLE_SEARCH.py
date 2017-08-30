from bs4 import BeautifulSoup
import requests
from hyper.contrib import HTTP20Adapter

def GET_HTTP_GOOGLE(x): # Функция получения ссылок по заданому слову в поисковике
    M = [] # Массив ссылок
    s = requests.Session() # Ну, так работает хайпер, ничего больше сказать не могу.
    s.mount('https://google.com/search?q=' + str(x), HTTP20Adapter())
    response = s.get('https://google.com/search?q=' + str(x))
    soup = BeautifulSoup(response.text, "lxml")
    for link in soup.find_all("h3"): # h3 - в гугле там находится ссылка на статью
        T = True #Нужна для проверки
        S = link.find('a').get('href').replace("/url?q=", "").split('&sa=U&ved=')[0] #Готовая к перевариванию ссылка
        if S != None: # Уборка мусора
            m = ['search', 'wikipedia', 'youtube', 'zoon'] # Массив ключевых слов, позволяющих отбрасывать определенные результаты поиска. Вводить часть нежелаемого ресурса.
            for i in m:
                if i in S:
                    T = False # Уборка мусора х2
            if T == True:
                M.append(S)
    return(M)











