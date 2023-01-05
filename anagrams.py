from collections import defaultdict

def groupanagram(a):
    defdict=defaultdict(list)

    for i in a:
        sorted_i = " ".join(sorted(i))
        defdict[sorted_i].append(i)
    return defdict.values()

words=["tea", "eat", "bat", "ate", "arc", "car"]
print(groupanagram(words))
