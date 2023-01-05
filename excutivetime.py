from time import time

start = time()

word = "god bless"
text = word.split()
a= ""

for i in text:
    a = a + str(i[2]).upper()
print(a)

end = time()

extime = end - start

print(extime)
