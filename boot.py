
import time
from machine import Pin

led=Pin(2,Pin.OUT)
nuppi=Pin(0,Pin.IN)
ledi=0

for x in range(10):
    led.value(ledi)
    ledi=(ledi+1)%2
    if nuppi.value()==0: break
    print('waiting',10-x)
    time.sleep(0.5)
    if x==9: import cali

led.value(1)


    
