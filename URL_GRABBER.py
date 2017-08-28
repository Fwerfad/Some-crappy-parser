from bs4 import BeautifulSoup
import requests
from hyper.contrib import HTTP20Adapter

def GET_HTTP(x): # Функция получения ссылок по заданому слову в поисковике
    M = [] # Массив ссылок
    s = requests.Session() # Ну, так работает хайпер, ничего больше сказать не могу.
    s.mount('https://google.com/search?q=' + str(x), HTTP20Adapter())
    response = s.get('https://google.com/search?q=' + str(x))
    soup = BeautifulSoup(response.text, "lxml")
    for link in soup.find_all("h3"): # h3 - в гугле там находится ссылка на статью
        if link.find('a') != None: # Уборка мусора
            if "search" not in link.find('a').get('href') and "wikipedia" not in link.find('a').get('href') and "youtube" not in link.find('a').get('href') and "zoon" not in link.find('a').get('href'): # Уборка мусора х2
                s = link.find('a').get('href').replace("/url?q=", "")
                S = s.split('&sa=U&ved=')
                M.append(S[0])
    return(M)












