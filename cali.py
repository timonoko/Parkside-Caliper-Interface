import time
from machine import Pin

led=Pin(2,Pin.OUT)
clock=Pin(5,Pin.IN)
data=Pin(4,Pin.IN)

led.value(0)
while True:
    numero=0
    if clock.value()==0:
        for z in range(20):
            while clock.value()==0: pass
            if data.value()==1: numero=numero|1<<z
            while clock.value()==1: pass
        print(numero/100.)
        time.sleep(0.02)
        
    
     
