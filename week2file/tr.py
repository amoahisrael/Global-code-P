from gpiozero import LED
from time import sleep

led1 = LED(17)
led2 = LED(27)
led3 = LED(22)

while True:
    led1.on()
    sleep(5)
    led1.off()
    
 
    led2.on()
    sleep(2)
    led2.off()
    
    led3.on()
    sleep(4)
    led3.off()