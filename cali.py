import time
from machine import Pin

clock=Pin(5,Pin.IN)
data=Pin(4,Pin.IN)
led=Pin(2,Pin.OUT)

nuppi=Pin(0,Pin.IN)

led.value(0)

prevnum=160
JUMP=0

loki=open('loki.txt','a')
loki.write("==========\n")

mittaus=1

while True:
    if nuppi.value()==0:
        led.value(1)
        print(prevnum,mittaus,"<===")
        loki.write(str(prevnum)+" "+str(mittaus)+"\n")
        time.sleep(1)
        led.value(0)
        mittaus+=1
    if clock.value()==0:
        numero=0
        for z in range(20):
            while clock.value()==0: pass
            if data.value()==1: numero=numero|1<<z
            while clock.value()==1: pass
        numero=numero/100.
        sign=0
        for z in range(2):
            while clock.value()==0: pass
            if data.value()==1: sign=sign|1<<z
            while clock.value()==1: pass
        if sign==1: numero=-numero
        if abs(numero)<160 and abs(numero-prevnum)<1:
            numero=round((numero+3*prevnum)/4,2) # averaging 
            if numero!=prevnum or JUMP==-1:
                print(numero)
                JUMP=0
            prevnum=numero
        elif JUMP>5: # Big Jump, forget the accuracy
            print("!")
            prevnum=numero
            JUMP=-1
        else: JUMP+=1
        time.sleep(0.2)
        
    
     
