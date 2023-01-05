def missingno(n):
    number = set(n)
    length = len(n)
    output = []

    for i in range(1,n[-1]):
        if i not in number:
            output.append(i)
    return output

numberset = [1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 13, 14, 16]
print(missingno(numberset))
      
    
