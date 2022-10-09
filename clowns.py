clowns=[]
person=[]
with open("people_jobs-1.txt", "r") as f:
    a=f.readlines()
    for line in a:
        line=line.strip().split(",")
        person.append(line)

for i in person:
     if i[2]=="clown":
        clowns.append((i[0]+ " "+i[1]))
print(clowns)
print(str(len(clowns)) + " clowns")
f.close()