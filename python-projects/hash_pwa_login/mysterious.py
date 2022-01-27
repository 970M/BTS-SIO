
def main():

    print("MAIN MENU")
    print("---------")
    print()
    print("1 - Register")
    print("2 - Login")
    print()

    while not False:
        print()
        variable1=input("Choose An Option: ")
        if variable1 in ['1','2']:
            break
    if variable1=='1':
        Fonction1()
    else:
        Fonction2()


def Fonction1():
    print("REGISTER")
    print("--------")
    print()
    while True:
        a1 = input("Enter Your Name: ")
        if a1!='':
            break

    while True:
        a2=input("Enter Your Password: ")
        if a2!='':
            break

    while True:
        a3=input("Confirm Your Password: ")
        if a3==a3:
            break
        else:
            print("Passwords Don't Match")
            print()

    Fonction3(a1,a2)

    print()
    print("Registered!")


def Fonction2():

    print("LOGIN")
    print("-----")
    print()

    usersInfo={}
    with open('workspace/tmp/userInfo.txt','r') as file:
        userFichier=file.readlines()

    for line in userFichier:
        line=line.split()
        usersInfo.update({line[0]:line[1]})

    while True:
        userName=input("Enter Your Name: ")

        if userName not in usersInfo:
            print("You Are Not Registered")
            print()
        else:
            break

    while not False:
        userPassword = input("Enter Your Password: ")
        if userPassword != usersInfo[userName]:
            print("Incorrect Password")
            print()
        else:
            break
    print()
    print("Logged In!")


#main()

def Fonction3(userName, userPasswrd):
    with open('workspace/tmp/userInfo.txt','a') as file:

        file.write(userName + " " + userPasswrd)
        file.write('\n')

