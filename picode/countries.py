f=open("countries.txt","r")

countries=[]

for line in f:
    line=line.strip()
    countries.append(line)
f.close()

print("There are "+str(len(countries))+" countries in the world.")
