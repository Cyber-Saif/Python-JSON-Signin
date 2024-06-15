#January ‎13, ‎2022
import json
import string
import random

digt = list(string.digits)
lwr_case = list(string.ascii_lowercase)
upper_case = list(string.ascii_uppercase)
punc = list(string.punctuation)

yes = ['Y','y']
No = ['N','n']
rpl = ['Y', 'y', 'N', 'n']
file = open("data.json", "r")
x = file.readline()
listA = json.loads(x)


def data_writer(value, key):
    listA[value] = key
    js = json.dumps(listA)
    file = open("data.json", "w")
    file.write(js)
    file.close()

def password_generator(total, capital, punctuations, digits):
    total, capital, punctuations, digits = int(total), int(capital), int(punctuations), int(digits)
    passwd = []
    count = capital + punctuations + digits

    if count>total:
        print(f'\nYour have given {total} characters for total, but you according to your need {count} characters generated')

    calc = 0

    if count == 0:
        calc = total
    else:
        calc = total - count
        
    
    if total:
        for capital in range(capital):
            passwd.append(random.choice(upper_case))

        for digit in range(digits):
            passwd.append(random.choice(digt))
        
        for punctuation in range(punctuations):
            passwd.append(random.choice(punc))

        for total in range(calc):
            passwd.append(random.choice(lwr_case))

    if len(passwd)<8:
        print("\n!!your total characters are less than 8! pls selec more than 7 press N or n, to generate a new one ")

    random.shuffle(passwd)
    return "".join(passwd)
    

    
def main():
    print("please select at least 8 characters")

    total = input('\ntype total characters you want: ')
    while total == "":
        print("Total characters are 0 program will not go further, try again")
        total = input('\ntype total characters you want: ')
        if total == "done":
            print(">>exiting the program")
            exit()
    
    while not total.isdigit():
        print("intigers expected")
        total = input('\ntype total characters you want: ')
        if total == "done":
            exit()

    while int(total)<8:
        print("your tootal is little short,to generate a secure one type 8 or more")
        total = input('\ntype total characters you want: ')
        if total =="done":
            print(">>exiting the program")
            exit()

    if total == "done":
        print(">>exiting the program")
        exit()


    capital = input('\nnumber of capital letters you want: ')   
    while capital == "":
        print("You must have one Capital letters")
        capital = input('\nnumber of capital letters you want: ')   
    
    if capital == "done":
        print(">>exiting the program")
        exit()
    
    while not capital.isdigit():
        print("intigers expected")
        capital = input('\nnumber of capital letters you want: ')   


    pnc = input('\nnumber of punctuations you want: ')
    while pnc == "":
        print("You must have one punctuations")
        pnc = input('\nnumber of punctuations you want: ')
        
    
    if pnc == "done":
        print(">>exiting the program")
        exit()

    while not pnc.isdigit():
        print("intigers expected")
        pnc = input('\nnumber of punctuations you want: ')     


    nmbr = input('\ntype total digits you want: ')
    while nmbr == "":
        print("You must have one digit")
        nmbr = input('\ntype total digits you want: ')
    
    if nmbr == "done":
        print(">>exiting the program")
        exit()

    while not nmbr.isdigit():
        print("intigers expected")
        nmbr = input('\ntype total digits you want: ')

    pwd = password_generator(total, capital, pnc, nmbr)
    print(f'Generated Pssword Is>> {pwd}')
     
    return pwd
    


def password_checker(string):
    strg = len(string)
    string = list(string)
    points = 0
    
    if strg<8:
        print(f'Your password only have {strg} characters which is not good')
    if strg>7:
        points+=1
    if string:
        for i in range(strg):
            if string[i] in upper_case:
                points+=1
                break
        else:
            print("!Capital letter missing")
            
        
        for j in range(strg):
            if string[j] in punc:
                points+=1
                break
        else:
            print("!No Punctuations found")


        for s in range(strg):
            if string[s] in digt:
                points+=1
                break
        else:
            print("!Digits missing")
    
    if points == 4:
        print(f'Good password')
    else:
        print("password is not secure, use a different password")

    return points

def account_login():    
    login = input("please input your username: ")
    
    #checking login info
    while login == "":
        print("\nyou must have a username")
        login = input("please input your username: ")
    
    if login == 'done':
        print(">>exiting the program")
        exit()
    
    
    for elements in listA:
        #making sure that the usrname is alredy exist or not    
        if login in listA:
            print(f"Welcome back {login}")
            #if it is then asking for password and checking if it is correct or not
            password = input("Enter your password here: ")
            if password == listA[login]:
                print("loged-in successfully")
                exit()
            if password == "done":
                print(">>exiting the program")
                exit()
            
            #if password is incorrect it will keep asking till it get the right psd or when usr type done
            while not password == listA[login]:
                print("password was incorrect try again")
                password = input("Enter your password here: ")
                if password == listA[login]:
                    print("login successfully")
                    exit()
                if password == "done":
                    exit()
                else:
                    continue

        #if usr is new
        elif login not in elements:  
            print(f"Welcome to the program {login}")
            npsd = input("Enter your new password here: ")
            if npsd == "done":   
                print(">>exiting the program")         
                exit()
            while npsd == "":
                npsd = input("Enter your new password here: ")

            check = password_checker(npsd)
            
            #if password is not secure
            if check<4:
                options = ['1','2','3']
                ask = input("Press[1] To keep your password, Press[2] to re-enter your password , Press[3] to generate a secure password by program\n1, 2 or 3: ")
                
                if ask == "done":
                    print(">>exiting the program")
                    exit()
                
                while ask not in options:
                    print("pls choose 1,2 or 3 not anything else")
                    ask = input("1,2 or 3: ")
                    if ask == "done":
                        print(">>exiting the program")
                        exit()

                if ask in options:                    
                    #generate a new password by program
                    if ask == "3":
                        generate = main()
                        confirm = input("are you happy with this password?Yes press<Y> No press<N>: ")
                        
                        while confirm == "":
                            confirm = input("are you happy with this password?Yes press<Y> No press<N>: ")
                        
                        while confirm not in rpl:
                            confirm = input("Pls select 'Y' or 'N': ")
                        
                        if confirm == "done":
                            exit()

                        if confirm in yes:
                            writedata = data_writer(login, generate)
                            print(f"{login} your account has created :)")
                            break
                            
                        while confirm in No:
                            regen = main()
                            confirm = input("are you happy with this password?Yes press<Y> No press<N>: ")
                            while confirm == "":
                                confirm = input("are you happy with this password?Yes press<Y> No press<N>: ")
                            while confirm not in rpl:
                                confirm = input("are you happy with this password?Yes press<Y> No press<N>: ")
                            if confirm in yes:
                                write = data_writer(login, regen)
                                print(f"{login} your account has created :)")
                                exit()

                        
                    #if usr wants to re-entering password
                    if ask == "2":
                        while check<4:
                            again = input("\npls re-enter your password: ")
                            
                            if again == "done":
                                write = data_writer(login, again)
                                print(">>exiting the program")
                                exit()

                            if again:
                                recheck = password_checker(again)
                            
                            if recheck>3:
                                print(f"{login} your account has created :)")
                                write = data_writer(login, again)
                                exit()
                    
                    #keeping their password as it is it
                    if ask == "1":
                        writer = data_writer(login, npsd)
                        print(f"{login} your account has created :)")
                        break

            elif check == 4:
                wr = data_writer(login, npsd)
                print("f{login} your account has created :)")
                exit()

        else:
            print("something went wrong")
            exit()





account_login()

