def splitter(kata,token):
    result = []
    temp = ""
    
    for i in range(length(kata)):
        if kata[i] == token  :
            result=append(result,temp)
            temp = ""
        elif kata[i]=="\n":
            result=append(result,temp)
            return result
        else:
            temp += (kata[i])
            
    

def append(list,x):
    list=[*list,x]
    return list

def length (list):
    list_temp=append(list,"%")
    j=0
    while list_temp[j]!="%":
        j+=1
    return j


def load(csv):
    file = open(csv, "r")
    result = []
    
    for row in file:
        result_temp = splitter(row,";")
        if not result_temp:
            break
        result=append(result,result_temp)
    return result



users=load("user.csv")
print(users)
