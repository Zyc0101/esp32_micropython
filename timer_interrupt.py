#导入Pin模块
from machine import Pin
from machine import Timer


timer0=Timer(0)
timer1=Timer(-1)
timer2=Timer(2)
timer3=Timer(3)

        
#程序入口
if __name__=="__main__":
    timer0.init(period=1000,mode=Timer.ONE_SHOT,callback=lambda t:print('定时器0,1s'))
    timer1.init(period=2000,mode=Timer.ONE_SHOT,callback=lambda t:print('定时器1,2s'))
    timer2.init(period=3000,mode=Timer.ONE_SHOT,callback=lambda t:print('定时器2,3S'))
    timer3.init(period=4000,mode=Timer.ONE_SHOT,callback=lambda t:print('定时器3,4S'))
    while True:
        pass
