import os

def save(file, folder, fileName):
    if 'save' not in os.listdir():
        os.mkdir('save')
    if folder not in os.listdir('save\\'):
        os.mkdir(f'save\\{folder}')
    with open(f'save\\{folder}\\{fileName}', 'w') as f:
        for row in file:
            f.write(';'.join(str(cell) for cell in row) + '\n')
