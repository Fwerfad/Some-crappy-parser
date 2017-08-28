import httplib2
from bs4 import BeautifulSoup

def PARSER(x):
    http = httplib2.Http() # А это хттплиб2, ага. Он работает по-другому. Ваш К.О.
    headers = {
            'Cookie': "q2p9eXA0GMU6d16sT4V4aRS5KRVp7vhOMY0BpA_pikiAPKV21aHHnm07GU87LhbSssRX5p2imuUQKlRZo4fFDjhnr1_uizHbDpy1sGxbVeh32ADRBWDAtgmu3qZjrjQP",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36"}  # Куки и *браузер
    response, content = http.request(x, 'GET', headers=headers)
    return BeautifulSoup(content, "lxml")
