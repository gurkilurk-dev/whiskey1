f = open("athletes.csv","r")
temp = f.readline()
temp = f.readline()
print(temp)
matris=[[],[],[],[],[],[],[],[],[]]

while temp != "":
    temp=temp.split(",")
    for i in range(4,len(temp)-1):
        if temp[i]!="":
            matris[i-4].append((temp[i],temp[0],temp[1],temp[2],temp[3]))
    temp = f.readline()
print(matris[0])
print ["hej"]

