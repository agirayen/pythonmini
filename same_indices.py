inputindices = [[10, 20, 30,70], [40, 50, 60,77], [70, 80, 90,77]]

outputindices = []

index = 0

for i in range (len(inputindices[0])):
    outputindices.append([])

    for j in range(len(inputindices)):
        outputindices[index].append(inputindices[j][index])
    index=index+1

a,b,c,d = outputindices[0] ,outputindices[1],outputindices[2],outputindices[3]
            
print(a,b,c,d)                
                
