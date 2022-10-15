with open(r'C:\3.Programming\FileDP\Chisla.txt', encoding='utf-8') as datfile:
    text = datfile.read()
print(sum(map(int, text.split(None, 2)[:2])))
