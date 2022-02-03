#1 adat beolvasása
from selenium.webdriver.common.keys import Keys
import selenium
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import ElementClickInterceptedException
print(f"Kérlek add meg a chromedrivered elérésének a helyét:")
eleres=input()
print(f"Kérlek írd be az alábbiak közül valamelyiket: OTP\nMOL\nRichter\nMTELEKOM")
reszveny=input()
oldalak= {"OTP":"https://www.bet.hu/oldalak/adatletoltes?marketType=prompt&instrument=otp",
          "MOL":"https://www.bet.hu/oldalak/adatletoltes?marketType=prompt&instrument=mol",
          "Richter":"https://www.bet.hu/oldalak/adatletoltes?marketType=prompt&instrument=richter",
          "MTELEKOM":"https://www.bet.hu/oldalak/adatletoltes?marketType=prompt&instrument=mtelekom"}

valasztottoldal=oldalak[f"{reszveny}"]
driver = webdriver.Chrome(eleres)
driver.get(f"{valasztottoldal}")
time.sleep(1)

driver.maximize_window()

dropdown_classname = "select2-selection--single"
dropdowns = driver.find_elements_by_class_name(dropdown_classname)
dropdowns[0].click()
dropdowns[0].send_keys(Keys.DOWN)
dropdowns[0].send_keys(Keys.ENTER)

time.sleep(1)
naptol="#instrumentStartingDate"
naptol=driver.find_element_by_css_selector(naptol)
naptol.click()
time.sleep(2)
for i in range (11):
    naptol.send_keys(Keys.BACKSPACE)
naptol.send_keys("2017.01.01.")
naptol.send_keys(Keys.ENTER)

napig="#instrumentEndingDate"
napig=driver.find_element_by_css_selector(napig)
napig.click()
for i in range (11):
    napig.send_keys(Keys.BACKSPACE)
napig.send_keys("2021.12.31.")
napig.send_keys(Keys.ENTER)

dropdowns[4].click()
dropdowns[4].send_keys(Keys.UP)
dropdowns[4].send_keys(Keys.ENTER)

dropdowns[5].click()
dropdowns[5].send_keys(Keys.DOWN)
dropdowns[5].send_keys(Keys.DOWN)
dropdowns[5].send_keys(Keys.ENTER)

driver.execute_script("window.scrollBy(0, 250)")

time.sleep(3)
letolt="promptButton"
letolt=driver.find_element_by_id(letolt)
time.sleep(2)


while True:
    try:
        letolt.click()
        break
    except ElementClickInterceptedException:
        pass
time.sleep(10)
driver.close()
#letolthelye=input
#letoltott=(r"C:\Users\PKeve\Desktop\Prog projekt\historikus_2017_12_06__2022_01_01.txt")2017_01_01__2021_12_31
#letoltott=(f'{letolthelye}\historikus_2017_12_06__2022_01_01_.txt')
opciok=["OTP","MOL","Richter","MTELEKOM"]
opciolink=["OTP.txt","MOL.txt","Richter.txt","MTELEKOM.txt"]
for i in range (len(opciok)):
    if reszveny==opciok[i]:
        letoltott=opciolink[i]

f=open(letoltott, mode="r", encoding="utf-8")
raw=(f.read())
data=raw.split()
#1.1 adat struktúrálása
eltav=['Név', 'Dátum', 'Utolsó', 'ár', 'Forgalom', '(db)', 'Forgalom', '(HUF', 'érték)', 'Forgalom', '(EUR', 'érték)', 'Kötések', 'száma', 'Nyitó', 'ár', 'Minimum', 'ár', 'Maximum', 'ár', 'Deviza', 'Átlag', 'ár', 'Kapitalizáció']
for i in eltav:
    data.remove(i)
napokszama=int((len(data))/13)
atlag=[]
for i in range (napokszama):
    atlag.append(float(data[11+13*i]))
forgalomHUF=[]
for i in range (napokszama):
    forgalomHUF.append(float(data[4+13*i]))

napok=[]
for i in range (napokszama):
    napok.append(i)
#2 elemzési segédletek számítása
kulonbseg=[]
for i in range (napokszama):
    if i>=1:
        kulonbseg.append((atlag[i]-atlag[i-1])/atlag[i])
    else:
        kulonbseg.append(0)
emelkedes=[]
eses=[]
for i in kulonbseg:
    if i>0:
        emelkedes.append(1)
        eses.append(0)
    elif i<0:
        emelkedes.append(0)
        eses.append(1)
    else:
        emelkedes.append(0)
        eses.append(0)
#RSI
RSI=[]
RSIseged=50

for i in range (napokszama):
    if i < 14:
        RSI.append(50)
    else:
        csokken14=[]
        novekszik14=[]

        for g in range (14):
            if kulonbseg[i-g]>0:
                novekszik14.append(kulonbseg[i-g])
            elif kulonbseg[i-g]<0:
                csokken14.append(abs(kulonbseg[i-g]))
        RSI.append(100-(100/(1+((sum(novekszik14)/len(novekszik14))/14)/(((sum(csokken14))/len(csokken14))/14))))

RSIpont=[]
for i in range (napokszama):
    if RSI[i]>70:
        RSIpont.append(-1)
    elif RSI[i]<30:
        RSIpont.append(1)
    else:
        RSIpont.append(0)
#50 napos mozgóátlag
MA50=[]
for i in range (napokszama):
    if i<50:
        MA50.append(atlag[i])
    else:
        seged=0
        for f in range (50):
            seged+=atlag[i-f]
        MA50.append(seged/50)
MA50VSAR=[]
for i in range (napokszama):
    if atlag[i]>MA50[i]:
        MA50VSAR.append(1)
    elif atlag[i]==MA50[i]:
        MA50VSAR.append(0)
    else:
        MA50VSAR.append(-1)

#kereskedési segédpont
Kereskedesipont=[]
for i in range (napokszama):
    Kereskedesipont.append(MA50VSAR[i]+RSIpont[i])
#kereskedés szimulálása
toke=1000000
piacipozicio=bool(False)
birtokoltreszveny=0
portfolio=[]
for t in range (napokszama):
    if t>50:
        if piacipozicio==True and Kereskedesipont[t]<=-1:
            toke=birtokoltreszveny*atlag[t]
            birtokoltreszveny=0
            piacipozicio=False
        elif piacipozicio==False and Kereskedesipont[t]>=1:
            birtokoltreszveny=toke/atlag[t]
            toke=0
            piacipozicio=True
    portfolio.append(toke+birtokoltreszveny*atlag[t])

teljeshozam=(((portfolio[napokszama-1])/(portfolio[0]))-1)*100
eveshozam=(((portfolio[napokszama-1])/(portfolio[0]))**(1/5)-1)*100


#egyéb
print(f"Portfólió kezdeti értéke:{portfolio[0]}\nPortfólió végső értéke:{portfolio[napokszama-1]} \nTeljes hozam: {teljeshozam}% \nÉvesített hozam: {eveshozam}%")


import pandas as pd
from matplotlib import pyplot as plt

#plt.plot(napok, MA50)
plt.plot(napok, atlag)
plt.plot(napok, portfolio)
plt.title("A portfólió időbeli alakulása")
plt.xlabel("Eltelt kereskedési napok száma")
plt.ylabel("Portfólió értékének alakulása")
plt.show()
