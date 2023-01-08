import getpass

database= {"sparky":"12345","jacky":"678910"}

username = input("Enter username : ")

password = getpass.getpass("Enter password : ")

for i in database.keys():
    if username == i:
        while password != database.get(i):
            password = getpass.getpass("Enter password again : ")
        break
print("verified")    
    
