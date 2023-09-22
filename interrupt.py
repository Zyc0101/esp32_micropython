#导入Pin模块
from machine import Pin
import time

#定义按键控制对象
key1=Pin(27,Pin.IN,Pin.PULL_UP)
key2=Pin(26,Pin.IN,Pin.PULL_UP)



#KEY1外部中断函数
def key1_irq(key1):
    print('1按下了')
#KEY2外部中断函数
def key2_irq(key2):
    print('2按下了')

key1.irq(key1_irq,Pin.IRQ_FALLING)  #配置key1外部中断，下降沿触发
key2.irq(key2_irq,Pin.IRQ_FALLING)  #配置key2外部中断，下降沿触发
#程序入口
if __name__=="__main__":
  
    
    
    while True:
        pass

