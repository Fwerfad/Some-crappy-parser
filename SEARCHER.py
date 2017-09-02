from bs4 import BeautifulSoup
import requests
from hyper.contrib import HTTP20Adapter

def check(x):
    T = True
    m = ['search', 'wikipedia', 'youtube', 'zoon']  # Массив сайтов, подлежащих отсеву
    for i in m:
        if i in x:
            T = False
    if T == True:
        return(x)
def SEARCH(x,y,z): #X - слово, y - поисковик, z - таг, где ссылки
    M = []  # Массив ссылок
    key = "03.160401204:e30c87055db4234f0562a0ac4d383052" #Ключ от яндекса
    user = "fwerfad" #Логин от яндекса
    m = ['search', 'wikipedia', 'youtube', 'zoon'] # Массив сайтов, подлежащих отсеву
    s = requests.Session()  # Ну, так работает хайпер, ничего больше сказать не могу.
    s.mount(y + str(x), HTTP20Adapter())
    if "yandex" in y: #Яндексу нужен ключ, остальным(пока только гуглу) он не нужен
        response = s.get(y + user + "&key=" + key + "&query="+ str(x))
    else:
        response = s.get(y + str(x))
    soup = BeautifulSoup(response.text, "lxml")
    if "google" in y:
        for link in soup.find_all(z):
            S = check(link.find('a').get('href').replace("/url?q=", "").split('&sa=U&ved=')[0]) #В гугле ссылки немного *грязные*, это их очищает.
            if S != None:
                M.append(S)
    elif "yandex" in y:
        for link in soup.find_all("url"):
            S = check(link.string)
            if S != None:
                M.append(S)
    return(M)
