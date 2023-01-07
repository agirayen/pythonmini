with open("Letter1.txt") as file:
    count=0
    text=file.read()
    for i in text:
        if i.isupper():
            count=count+1
    print(count)         
