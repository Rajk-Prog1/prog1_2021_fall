import numpy as np
import string
import datetime

switchdict = {",": "+", "#": "-"}
reverse_switchdict = {v: k for k, v in switchdict.items()}

#######################################################################################
# IDE ÍRD A SAJÁT FÜGGVÉNYEID
#######################################################################################
def cal_diff(ev, honap, nap):
    now = datetime.datetime.now()
    most_ev = now.year
    most_honap = now.month
    most_nap = now.day
    
    eltelt_evek = most_ev - ev
    eltelt_napok = eltelt_evek * 365
    
    szokoev = lambda ev: (ev % 4 == 0 and ev % 100 != 0) or (ev % 400 == 0)
    szokonapok = len([*filter(szokoev, [*range(ev + 1, most_ev)])])
    
    if szokoev(most_ev) and most_honap > 2:
        szokonapok += 1
    
    if szokoev(ev) and honap < 3:
        szokonapok += 1
        
    eltelt_napok += szokonapok
    
    if most_honap > honap:
        for kul_honap in range(honap, most_honap):
            if kul_honap in [1, 3, 5, 7, 8, 10, 12]:
                eltelt_napok += 31
            elif kul_honap == 2:
                eltelt_napok += 28
            else:
                eltelt_napok += 30
    else:
        for kul_honap in range(most_honap, honap):
            if kul_honap in [1, 3, 5, 7, 8, 10, 12]:
                eltelt_napok -= 31
            elif kul_honap == 2:
                eltelt_napok -= 28
            else:
                eltelt_napok -= 30
        
    eltelt_napok += most_nap - nap
    
    return eltelt_napok

def day_diff(inp1, inp2):
    return cal_diff(inp1[0], inp1[1], inp1[2]), cal_diff(inp2[0], inp2[1], inp2[2])

def check_day(own_func, inp1, inp2):
    
    out1, out2 = own_func(inp1, inp2)
    out1_, out2_ = day_diff(inp1, inp2)
    
    if out1 == out1_ and out2 == out2_:
        print('Gratulálok! Megoldottad a feladatot!')
    else:
        print('Sajnos nem sikerült, próbáld újra!')
        
#######################################################################################


def bcommon_div(inp1, inp2):

    max_oszto = 1
    
    for i in range(2, inp1//2 + 1):
        if inp1 % i == 0 and inp2 % i == 0:
            max_oszto = i
            
    return max_oszto


def check_bcom(own_func, inp1, inp2):
    
    if own_func(inp1, inp2) == bcommon_div(inp1, inp2):
        print('Gratulálok! Megoldottad a feladatot!')
    else:
        print('Sajnos nem sikerült, próbáld újra!')

#######################################################################################
#######################################################################################

def remove_chars(inp):

    return "".join([c for c in list(inp) if c not in list(string.ascii_lowercase)])


def check_rem(own_func, inp):
    
    if own_func(inp) == remove_chars(inp):
        print('Gratulálok! Megoldottad a feladatot!')
    else:
        print('Sajnos nem sikerült, próbáld újra!')
        
#######################################################################################xx


def replace_chars(inp):

    for k, v in reverse_switchdict.items():
        inp = inp.replace(k, v)

    return inp


def check_rep(own_func, inp):
    
    if own_func(inp) == replace_chars(inp):
        print('Gratulálok! Megoldottad a feladatot!')
    else:
        print('Sajnos nem sikerült, próbáld újra!')
        
#######################################################################################


def select_chars(inp1, inp2):

    return "".join([inp1[k * inp2 - 1] for k in range(1, int(len(inp1) / inp2) + 1)])


def check_sel(own_func, inp1, inp2):
    
    if own_func(inp1, inp2) == select_chars(inp1, inp2):
        print('Gratulálok! Megoldottad a feladatot!')
    else:
        print('Sajnos nem sikerült, próbáld újra!')        
    