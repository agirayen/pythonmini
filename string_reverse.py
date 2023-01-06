def textreverse(string):
    return string[::-1]


text=input("Enter string : ")
text1=textreverse(text)
print(text1)

def pali(text3):
    return text3 == text3[::-1]
text=input("enter string: ")
ans=pali(text)

if ans:
    print("palindrome")
else:
    print("Not palindrome")
