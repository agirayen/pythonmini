# mean
list1=[12, 16, 20, 20, 12, 30, 25, 23, 24, 20]

mean = sum(list1)/len(list1)

print(mean)

#median

list2 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]

if len(list2 ) % 2 == 0:

    m1 = list2[len(list2) // 2]
    m2 = list2[len(list2) // 2 -1]

    median=(m1+m2) /2

else:

    median = list2[len(list2) // 2]
print(median)

# mode

list3 = [12, 16, 20, 20, 12, 30, 25, 23, 24, 20]

frequency={}

for i in list3:
    frequency.setdefault(i,0)
    frequency[i]=frequency[i] + 1
    
print(frequency)    

frequent = max(frequency.values())
for i,j in frequency.items():
    print(i,j)
    if j == frequent :
        mode = i
print(mode)        
