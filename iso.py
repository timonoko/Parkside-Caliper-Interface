"""
+-------+-------+-------+-------+
|TIETO- |LAMPPU |LAMPPU |       |
|KONE   |YLÄ    |KATTO  |       |
|       |       |       |       |
+-------+-------+-------+-------+
|4RELE  |4RELE  |4RELE  |4RELE  |
|   1   |  2    |  3    |  4    |
|       |       |       |       |
+-------+-------+-------+-------+
|CLAS-  |CLAS-  |       |       |
| RELE  | RELE  |       |       |
|    1  |   2   |       |       |
+-------+-------+-------+-------+
| CLAS- | CLAS- | YKSI  | MOVIE |
| LAMPPU| LAMPPU| RUUTU |       |
|    1  |   2   |       |       |
+-------+-------+-------+-------+
| JUOTIN|TOKMANN|TOKMANN|RESET/ |
|       | RELE  |  RELE |REPROGR|
|       |  61   |   62  |       |
+-------+-------+-------+-------+
        | ALL   |
        | OFF   |
        |       |
        +-------+

"""
#import upip
#upip.install('urequests')

import urequests

print("Versio=2")

import time,machine,sys

from machine import TouchPad,Pin

led=Pin(2,Pin.OUT)
outti=Pin(12,Pin.OUT)
led2=Pin(13,Pin.OUT)
A=Pin(19,Pin.OUT)
B=Pin(21,Pin.OUT)
C=Pin(22,Pin.OUT)
D=Pin(23,Pin.OUT)

Pir=Pin(18,Pin.IN)

XT=TouchPad(Pin(4))
X0=TouchPad(Pin(14))
X1=TouchPad(Pin(15))
X2=TouchPad(Pin(27))
X3=TouchPad(Pin(32))
X4=TouchPad(Pin(33))

def tats(x):
    A.value(x&1)
    B.value((x>>1)&1)
    C.value((x>>2)&1)
    D.value((x>>3)&1)
    time.sleep(0.03)
    return XT.read()< 45 

if tats(15):
    for x in range(21):
        led2.value(x%2)
        time.sleep(0.1)
    sys.exit()


def mysleep(x):
    for y in range(5*x):
        wdt.feed()
        time.sleep(0.2)
"""
def touch():
    led2.value(1)
    while True:
        for x in range(16):
            wdt.feed()
            if tats(x):
                led2.value(0)
                cou=0
                while tats(x) and cou<32: cou+=1
                if cou>30: return x+20
                else: return x
        for num in range(0,5):
            x="X"+str(num)+".read()<500"
            if eval(x): 
                led2.value(0)
                cou=0
                while eval(x) and cou<11:
                    time.sleep(0.1)
                    cou+=1
                if cou>10: return 120+num
                else: return 100+num

"""

WATCHDOG=0
tunti=3600
pir_count=0
no_pir=0

def touch():
    global WATCHDOG,tunti,pir_count,no_pir
    led2.value(1)
    pir_count=0
    no_pir=0
    while True:
        WATCHDOG+=1 
        print('WATCHDOG:',WATCHDOG)
        if WATCHDOG>24*tunti:
            WATCHDOG=0
            return 120
        if WATCHDOG%tunti==0:
            return 7777
        for x in range(16):
            wdt.feed()
            if tats(x):
                WATCHDOG=0
                led2.value(0)
                cou=0
                while tats(x) and cou<32: cou+=1
                if cou>30: return x+20
                else: return x
        for num in range(0,5):
            x="X"+str(num)+".read()<500"
            if eval(x): 
                led2.value(0)
                cou=0
                while eval(x) and cou<11:
                    time.sleep(0.1)
                    cou+=1
                if cou>10: return 120+num
                else: return 100+num
        if Pir.value()==1:
            wdt.feed()
            no_pir=0
            if pir_count>10:
                led2.value(0)
                time.sleep(0.005)
                led2.value(1)
                pir_count=0
                WATCHDOG=0
            else:
                print('pir_count:',pir_count)
                pir_count+=1
        else:
            no_pir+=1
            print('no_pir:',no_pir)
            if no_pir>60:
                pir_count=0
                no_pir=0
            led2.value(1)
                    
NAPIT=[[7, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
[1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
[2, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1],
[3, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0],
[4, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0],
[5, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1],
[6, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1]]

                
kamala=10
def sendpulse(x):
    iik=0
    outti.value(1)
    for z in range(50): iik+=1
    outti.value(0)
    if x==0:
        for z in range(60): iik+=1
    elif x==1:
        for z in range(5*60): iik+=1
    elif x==2:
        for z in range(kamala*60): iik+=1
        
        
def send2(x):
    global NAPIT
    for y in NAPIT:
        if y[0]==x:
            sendpulse(2)
            sendpulse(0)
            sendpulse(1)
            sendpulse(1)
            for zuu in range(4):
                sendpulse(0)
                sendpulse(1)
            for z in y[1:]:
                sendpulse(z)
            sendpulse(1)
            
def send(x):
    for z in range(6):
        send2(x)
        time.sleep(0.01)
    mysleep(1)

def urequ(x):
    led.value(1)
    print(x)
    try: urequests.get(x)
    except:
        wdt.feed()
        try: urequests.get(x)
        except: pass
    led.value(0)

def all_off():
    led2.value(0)
    send(1)
    send(3)
    send(5)
    for x in range(4): urequ('http://192.168.1.65/r%soff'%(x+1))
    for x in range(1,3): urequ('http://192.168.1.11:8083/OFF%s'%(x))
    urequ('http://192.168.1.64/5/off')
    urequ('http://192.168.1.61/5/off')
    urequ('http://192.168.1.62/5/off')

def turhat_off():
    led2.value(0)
    send(1)
    send(3)
    send(5)
    urequ('http://192.168.1.64/5/off')

from machine import WDT
wdt=WDT(timeout=5000)
    
prevtu=200            
def maini():
    global prevtu
    while True:
        print('Main LOOP')
        for x in range(16):
            wdt.feed()
            tu=touch()
            print(tu)
            if tu==0: send(2)
            elif tu==20: send(1)
            elif tu==1: send(4)
            elif tu==21: send(3)
            elif tu==2: send(6)
            elif tu==22: send(5)
            elif tu>3 and tu<8: urequ('http://192.168.1.65/r%son'%(tu-3))
            elif tu>23 and tu<28: urequ('http://192.168.1.65/r%soff'%(tu-23)) 
            elif tu>7 and tu<10: urequ('http://192.168.1.11:8083/ON%s'%(tu-7))
            elif tu>27 and tu<30: urequ('http://192.168.1.11:8083/OFF%s'%(tu-27))
            elif tu==12: urequ('http://192.168.1.64/5/on')
            elif tu==32: urequ('http://192.168.1.64/5/off')
            elif tu==13: urequ('http://192.168.1.61/5/on')
            elif tu==33: urequ('http://192.168.1.61/5/off')
            elif tu==14: urequ('http://192.168.1.62/5/on')
            elif tu==34: urequ('http://192.168.1.62/5/off')
            elif tu==35:
                led2.value(0)
                machine.reset()
            elif tu==120:  all_off()
            elif tu==7777:  turhat_off()
                # neljäs rivi välissä
            elif tu in range(101,106): urequ('http://192.168.1.11:8083/ON%s'%(tu))
            elif tu in range(121,125): urequ('http://192.168.1.11:8083/OFF%s'%(tu-20))
            else:
                    for x in range(11):
                        led2.value(x%2)
                        time.sleep(0.2)
            if tu in range(20,35):
                print('viive 3')
                time.sleep(2)  
            prevtu=tu
maini()

        
