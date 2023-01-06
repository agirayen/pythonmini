list =  [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]

uniquelist = []
duplist =[]

for i in list:
    if i not in uniquelist:
        uniquelist.append(i)
    elif i not in duplist:
        duplist.append(i)
print(duplist)        

list1 =["hello","world","welcome","hello","world","glow"]

def finddup(x):

    length=len(x)
    duplicate =[]

    for i in range(length):

        n=i+1
        for j in range(n,length):
            if x[i] == x[j] and x[i] not in duplicate:
                duplicate.append(x[i])
    return duplicate

print(finddup(list1))    
