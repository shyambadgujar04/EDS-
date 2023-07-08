f=open("dataset2.csv","r")
cont=f.read()
line=cont.splitlines()


word=[]
carname=[]
cprice=[]
cartype=[]
esize=[]
chorsep=[]
cartype=[]

for i in line:
    words=i.split(",")
    carname.append(word[2])
    cprice.append(words[4])
    esize.append(words[5])
    chorsep.append(words[6])
    cartype.append(words[3])

print("The Most Expensive Car : ",carname[cprice.index(max(int((cprice))))])

    
l=len(cprize)
add=sum(cprice)

print("\nAverage sale of all cars : ",add/l)

count=0
for r in cartype:
    if r=="Passenger":
        count= count+1

print("\nTotal Number of Passenger cars : ",count)
print("The Car having maximum engine size : ",carname[esize.index(max(int((esize))))])
print("The Car having minimum horsepower : ",carname[chorsep.index(min(int((chorsep))))])


    
