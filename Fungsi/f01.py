import CSV_Parser as parser

def login(user,role):
    username=input("Username: ")
    password=input("Password: ")
    for i in range (1,parser.length(user)):
        if user[i][0]==username:
            if password==user[i][1]:
                print (f'\nSelamat datang, {username}!\nMasukkan command “help” untuk daftar command yang dapat kamu panggil.')
                role=user[i][2]
                return role,username
            else:
                print("\nPassword Salah")
                return 0,0
    else:
        print("\nUsername tidak terdaftar")
        return 0,0




