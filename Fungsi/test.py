def parser(csv,list,token):
    file = open(csv,"r")
    i = -1
    for line in file:
        if i == -1:
            i += 1
            continue
        else:
            h = 0
            temp = ""
            for j in range(len(line)):
                if line[j] == token or line[j] == '\n':
                    list[i][h] = temp
                    temp = ""
                    h += 1
                else:
                    temp += line[j]
            if temp != "":
                list[i][h] = temp
            i += 1
    return list


# users = [[0,0,0] for i in range(102)]
# users = load("FileCSV//user.csv",users,";")
# print(users)

# candi = [[0,0,0,0,0] for i in range(100)]
# candi = load("FileCSV//candi.csv",candi,";")
# print(candi)

bahan_bangunan = [[0,0,0] for i in range(3)]
bahan_bangunan = parser("FileCSV//bahan_bangunan.csv",bahan_bangunan,";")
print(bahan_bangunan)