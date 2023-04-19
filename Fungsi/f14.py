import os

def save(file, fileName):
    folder = input("Masukkan nama folder: ")
    print("Saving...")
    
    if 'save' not in os.listdir():
        print("Membuat folder save...")
        print(f"Membuat folder save/{folder}...")
        os.mkdir('save')
    if folder not in os.listdir('save\\'):
        print(f"Membuat folder save/{folder}...")
        os.mkdir(f'save\\{folder}')
    
    with open(f'save\\{folder}\\{fileName}', 'w') as f:
        for row in file:
            f.write(';'.join(str(cell) for cell in row) + '\n')
    print(f"Berhasil menyimpan data di folder save/{folder}!")
