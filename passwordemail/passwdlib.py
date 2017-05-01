import string, random

def generatepassword(num):
    password = ''

    for n in range(num):
        x= random.randint(0,94)
        password += string.printable[x]
    return password    
        

for n in range(100):
    print(generatepassword(16))
