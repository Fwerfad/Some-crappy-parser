from SEARCHER import SEARCH
def GET_URL(x):
    M = SEARCH(x, "https://google.com/search?q=", "h3") # Результаты из гугла
    for i in SEARCH(x, "https://yandex.com/search/xml?l10n=en&user=", "url"): # Неповторяющиеся резульаты из яндекса
        if i not in M:
            M.append(i)
    return(M)