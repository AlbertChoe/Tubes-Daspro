def splitter(kata,token):
    result = []
    temp = ""
    
    for i in range(length(kata)):
        if kata[i] == token:
            result.append(temp)
            temp = ""
        else:
            temp += (kata[i])
            
    result.append(temp)
    return result

def load(csv):
    file = open(csv, "r")
    result = []
    
    for row in file:
        result_temp = splitter((row.strip()),";")
        if not result_temp:
            break
        result.append(result_temp)
    return result

def length(word):
    count=0
    for i in word :
        count+=1
    return count

users=load("user.csv")
print(users)
