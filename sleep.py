import esp32
import machine
from machine import Timer
from time import sleep_ms

def gotosleep():
    print('5s going to sleep')
    sleep_ms(5000)
    print('sleeping...')
    sleep_ms(100)
    machine.deepsleep()
    #machine.lightsleep(10000)
    
def time0_irq(time0): 
    gotosleep()
    
def init():
    print('Woken-up')
    pin25 = machine.Pin(25, machine.Pin.IN, machine.Pin.PULL_DOWN)
    esp32.wake_on_ext0(pin25, esp32.WAKEUP_ANY_HIGH)
    time0=Timer(0)  #创建time0定时器对象
    time0.init(period=10000,mode=Timer.PERIODIC,callback=time0_irq)
    
def loop():
    while True:
        pass
    
#程序入口
if __name__=="__main__":
    while True:
        init()
        loop()
    