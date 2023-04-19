import os

def save(file, fileName):
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
            if file[x] == 'users':
                for i in range(102):
                    for j in range(3):
                        if j != 2:
                            f.write(f'{file[i][j]};')
                        else:
                            f.write(f'{file[i][j]}')
                    f.write('\n')
            elif file[x] == 'candi':
                for i in range(100):
                    for j in range(4):
                        if j != 3:
                            f.write(f'{file[i][j]};')
                        else:
                            f.write(f'{file[i][j]}')
                    f.write('\n')
            else:
                for i in range(3):
                    for j in range(3):
                        if j != 2:
                            f.write(f'{file[i][j]};')
                        else:
                            f.write(f'{file[i][j]}')
                    f.write('\n')
    print(f"Berhasil menyimpan data di folder save/{folder}!")
