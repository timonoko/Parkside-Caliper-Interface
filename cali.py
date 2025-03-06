import time
from machine import Pin

clock=Pin(5,Pin.IN)
data=Pin(4,Pin.IN)
led=Pin(2,Pin.OUT)
led.value(0)

while True:
    if clock.value()==0:
        numero=0
        for z in range(20):
            while clock.value()==0: pass
            if data.value()==1: numero=numero|1<<z
            while clock.value()==1: pass
        sign=0
        for z in range(2):
            while clock.value()==0: pass
            if data.value()==1: sign=sign|1<<z
            while clock.value()==1: pass
        if sign==1: numero=-numero
        print(numero/100.)
        time.sleep(0.02)
        
    
     
