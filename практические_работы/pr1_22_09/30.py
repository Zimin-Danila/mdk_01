import re
res = """Input file contains:
{} letters
{} words
{} lines
"""
with open(r'C:\3.Programming\FileDP\Opredelenie.txt', encoding='utf-8') as fh:
    f = fh.read().rstrip()
count_lines = len(f.split('\n'))
count_words = len(re.findall(r"\w+", f))
count_letters = sum([1 for x in f if x.isalpha()])
print(res.format(count_letters, count_words, count_lines))