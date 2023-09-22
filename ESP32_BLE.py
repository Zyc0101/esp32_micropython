
#导入Pin模块
from machine import Pin
from machine import Timer
from time import sleep_ms
import bluetooth

BLE_MSG = ""


class ESP32_BLE():
    def __init__(self, name):
        self.led = Pin(25, Pin.OUT) #创建led灯对象
        self.timer1 = Timer(0)#创建定时器对象
        self.name = name
        self.ble = bluetooth.BLE()#创建蓝牙对象
        self.ble.active(True)#启动蓝牙
        self.ble.config(gap_name=name)#配置蓝牙名字
        self.disconnected()#定时器初始化
        self.ble.irq(self.ble_irq)#蓝牙接受中断函数
        self.register()#注册服务
        self.ble.gatts_write(self.rx, bytes(100))  #修改一次最大接收字节数100
        self.advertiser()#广播蓝牙

    def connected(self):
        self.led.value(1)
        self.timer1.deinit()

    def disconnected(self):
        #定时器中断初始化 计时100ms，自动重载模式，回调函数是让LED取反
        self.timer1.init(period=100, mode=Timer.PERIODIC, callback=lambda t: self.led.value(not self.led.value()))

    def ble_irq(self, event, data):
        global BLE_MSG
        if event == 1: #_IRQ_CENTRAL_CONNECT 手机链接了此设备
            self.connected()#连接上了，让LED常亮，并关闭定时器
            self.close_advertiser()#关闭广播
        elif event == 2: #_IRQ_CENTRAL_DISCONNECT 手机断开此设备
            self.advertiser()#广播蓝牙
            self.disconnected()#重置定时器,让LED重新闪烁
        elif event == 3: #_IRQ_GATTS_WRITE 手机发送了数据 
            buffer = self.ble.gatts_read(self.rx)
            BLE_MSG = buffer.decode('UTF-8').strip()
            
    def register(self):        
        service_uuid = '6E400001-B5A3-F393-E0A9-E50E24DCCA9E'
        reader_uuid = '6E400002-B5A3-F393-E0A9-E50E24DCCA9E'
        sender_uuid = '6E400003-B5A3-F393-E0A9-E50E24DCCA9E'

        services = (
            (
                bluetooth.UUID(service_uuid), 
                (
                    (bluetooth.UUID(sender_uuid), bluetooth.FLAG_NOTIFY), 
                    (bluetooth.UUID(reader_uuid), bluetooth.FLAG_WRITE),
                )
            ), 
        )

        ((self.tx, self.rx,), ) = self.ble.gatts_register_services(services)

    def send(self, data):
        self.ble.gatts_notify(0, self.tx, data + '\n')

    def advertiser(self):
        name = bytes(self.name, 'UTF-8')
        adv_data = bytearray('\x02\x01\x02') + bytearray((len(name) + 1, 0x09)) + name
        self.ble.gap_advertise(100, adv_data)
        print(adv_data)
        print("\r\n")
    def close_advertiser(self):
        self.ble.gap_advertise(0)
        print("close_advertiser")

def buttons_irq(pin):
    led.value(not led.value())
    print('LED is ON.' if led.value() else 'LED is OFF')
    ble.send('LED is ON.' if led.value() else 'LED is OFF')


if __name__ == "__main__":
    ble = ESP32_BLE("ESP32BLE")

    but = Pin(14, Pin.IN)
    but.irq(trigger=Pin.IRQ_FALLING, handler=buttons_irq)#把按钮设置成了中断

    led = Pin(15, Pin.OUT)

    while True:
        if BLE_MSG == 'read_LED':
            print(BLE_MSG)
            BLE_MSG = ""
            print('LED is ON.' if led.value() else 'LED is OFF')
            ble.send('LED is ON.' if led.value() else 'LED is OFF')
        sleep_ms(100)

