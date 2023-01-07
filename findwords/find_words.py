words =[]

with open("Letter.txt","r") as f:
    for i in f:
        words.extend(i.split())

from collections import Counter

countw=Counter(words)
findwords =countw.most_common(8)
print(findwords)
