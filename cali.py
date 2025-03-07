import time
from machine import Pin

clock=Pin(5,Pin.IN)
data=Pin(4,Pin.IN)
led=Pin(2,Pin.OUT)

nuppi=Pin(0,Pin.IN)

led.value(0)

def almost_equal(num1, num2):
    return abs(num1-num2)<1

prevnum=170


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
        if numero==prevnum: pass
        elif numero<160 and almost_equal(prevnum,numero):
            print(numero)
        prevnum=numero
        time.sleep(0.2)
        
    
     
