from collections import Counter
words = []
for _ in range(int(input())):
    words.extend(input().split())
counter = Counter(words)
pairs = [(-pair[1], pair[0]) for pair in counter.most_common()]
words = [pair[1] for pair in sorted(pairs)]
print('\n'.join(words))


#Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt
#ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris
#nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit
#esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt
#in culpa qui officia deserunt mollit anim id est laborum