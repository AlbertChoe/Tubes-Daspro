import os

def save(file :tuple , fileName:tuple) ->None:
    folder = input("Masukkan nama folder: ")
    print("Saving...")
    
    if 'save' not in os.listdir():
        print("Membuat folder save...")
        print(f"Membuat folder save/{folder}...")
        os.mkdir('save')
    elif folder not in os.listdir('save\\'):
        print(f"Membuat folder save/{folder}...")
        os.mkdir(f'save\\{folder}')
    
    for x in range(3):
        with open(f'save\\{folder}\\{fileName[x]}', 'w') as f:
            if x == 0:
                f.write("username;password;role\n")
                for i in range(102):
                    for j in range(3):
                        if j != 2:
                            f.write(f'{file[x][i][j]};')
                        else:
                            f.write(f'{file[x][i][j]}')
                    f.write('\n')
            elif x == 1:
                f.write("id;pembuat;pasir;batu;air\n")
                for i in range(100):
                    for j in range(5):
                        if j != 4:
                            f.write(f'{file[x][i][j]};')
                        else:
                            f.write(f'{file[x][i][j]}')
                    f.write('\n')
            else:
                f.write("nama;deskripsi;jumlah\n")
                for i in range(3):
                    for j in range(3):
                        if j != 2:
                            f.write(f'{file[x][i][j]};')
                        else:
                            f.write(f'{file[x][i][j]}')
                    f.write('\n')
    print(f"Berhasil menyimpan data di folder save/{folder}!")
