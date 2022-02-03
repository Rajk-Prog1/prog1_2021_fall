#2018 1.1
f=open("input1.txt", mode="r", encoding="UTF-8")
adat=f.read()
adat1=[]
adat1=adat.split()
eredmeny1=0
for i in adat1:
    eredmeny1+=int(i[0:len(i)])
print(eredmeny1)

#1.2

f=open("input1.txt", mode="r", encoding="UTF-8")
adat=f.read()
adat2=[]
adat2=adat.split()
eredmeny11=[]
segedt11=[]
seged11=0
sadat2=[]
sadat2=adat2*200

for i in range (len(sadat2)):
    seged11=seged11+int(sadat2[i])
    if seged11 in segedt11:
        eredmeny11.append(seged11)
    segedt11.append(seged11)
print(eredmeny11)

#2.1
f=open("input2.txt", mode="r", encoding="UTF-8")
adat=f.read()
adat3=[]
betunkent=[]
adat3=adat.split()
ketto=int()
harom=int()
abc=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
for i in range (len(adat3)):
    adat3[i]=split(adat3[i])
for i in adat3:
    kettob=0
    haromb=0
    for f in abc:
        if i.count(f)==2:
            kettob=1
        elif i.count(f)==3:
            haromb=1
    ketto=ketto+kettob
    harom=harom+haromb
print(ketto*harom)

#2.2
f=open("input2.txt", mode="r", encoding="UTF-8")
adat=f.read()
adat4=[]
adat4=adat.split()

talalat = False
for i in range(len(adat4)):
    if talalat:
        break
    a = adat4[i]
    for j in range(i + 1, len(adat4)):
        b = adat4[j]
        kulonbseg = 0
        k = 0
        eredmeny = ""
        while kulonbseg <= 1 and k < len(a):
            if a[k] != b[k]:
                kulonbseg += 1
            else:
                eredmeny += a[k]
            k += 1
        if kulonbseg == 1:
            print(eredmeny)
            talalat = True
            break
print(adat4)
 
#3.1
with open("input3.txt") as f:
    adat = f.readlines()

adat5 = [x.strip().split(' ') for x in adat]

teljes = [ [0 for x in range(1000)] for x in range(1000)]

for adat in adat5:
    kezdX = int(adat[2].split(',')[0])
    kezY = int(adat[2].split(',')[1].strip(':'))
    sor = int(adat[3].split('x')[0])
    oszlop = int(adat[3].split('x')[1])
    for i in range(kezY, kezY + oszlop):
        for j in range(kezdX, kezdX + sor):
            teljes[i][j] += 1

eredmeny = 0
for f in range(1000):
    for g in range(1000):
        if teljes[f][g] >= 2:
            eredmeny += 1

print(eredmeny)

#3.2
with open("input3.txt") as f:
    adat = f.readlines()

adat6 = [x.strip().split(' ') for x in adat]

teljes = [ [[] for x in range(1000)] for x in range(1000)]

for adat in adat6:
    kezdX = int(adat[2].split(',')[0])
    kezdY = int(adat[2].split(',')[1].strip(':'))
    sor = int(adat[3].split('x')[0])
    oszlop = int(adat[3].split('x')[1])
    for i in range(kezdY, kezdY + oszlop):
        for j in range(kezdX, kezdX + sor):
            teljes[i][j].append(adat[0])

for adat in adat5:
    kezdX = int(adat[2].split(',')[0])
    kezdY = int(adat[2].split(',')[1].strip(':'))
    sor = int(adat[3].split('x')[0])
    oszlop = int(adat[3].split('x')[1])
    egy = True
    for i in range(kezdY, kezdY + oszlop):
        for j in range(kezdX, kezdX + sor):
            if len(teljes[i][j]) != 1:
                egy = False
    if egy == True:
        print(adat[0])
print(adat5)


#+1 késés: 2020 1.1

f=open("20201.txt", mode="r", encoding="UTF-8")
adat=f.read()
adat5=[]
adat5=adat.split()
eredmeny=()
for i in adat5:
    for f in adat5:
        if int(f)+int(i)==2020:
            eredmeny=(f'Két szám: {f} és {i}\n szorzatuk {int(i)*int(f)}')
print(eredmeny)
print(adat5)
