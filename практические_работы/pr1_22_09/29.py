with open(r'C:\3.Programming\FileDP\ChislaMany.txt', encoding='utf-8') as t:
    print(*(sum(map(int, line.split())) for line in t.readlines()), sep='\n')
