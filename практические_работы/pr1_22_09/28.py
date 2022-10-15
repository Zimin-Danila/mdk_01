with open(r'C:\3.Programming\FileDP\Znak.txt', encoding='utf-8') as f:
    print('yes' if input() in f.read() else 'no')
