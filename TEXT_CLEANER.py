def CLEAN(Text):
    lines = (line.strip() for line in Text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    return('\n'.join(chunk for chunk in chunks if chunk))