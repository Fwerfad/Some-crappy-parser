from YANDEX_SEARCH import GET_HTTP_YANDEX
from GOOGLE_SEARCH import GET_HTTP_GOOGLE
def GET_HTTP(x):
    M = GET_HTTP_GOOGLE(x) # Результат из гугла
    for i in GET_HTTP_YANDEX(x): # + неповторяющиеся результаты из яндекса
        if i not in M:
            M.append(i)
    return(M) # Готовый массив ссылок
