from gpiozero import LED
from time import sleep

led1=LED(4)
led2=LED(26)
led3=LED(17)
led1.on()
sleep(3)
led1.off()
led2.on()
sleep(3)
led2.off()
led3.on()
sleep(3)
led3.off()
