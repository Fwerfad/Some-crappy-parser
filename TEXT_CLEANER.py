#Функция очистки текста от пустого пространства. Из-за того, что используется несколько раз напротяжении работы программы, вынесенна в отдельную функцию.
def CLEAN(Text):
    lines = (line.strip() for line in Text.splitlines()) # Разбиваем на строчки и убираем пустые места
    chunks = (phrase.strip() for line in lines for phrase in line.split("  ")) # Собираем несколько пустых строчек в одну
    return('\n'.join(chunk for chunk in chunks if chunk)) # Выкидываем пустые строчки