def count_char(s):
    count = {}

    for i in s:
        if i in count:
            count[i] = count[i] +1
        else:
            count[i]=1
    print(count)
print(count_char("Thecleverprogrammer"))
      
