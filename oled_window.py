from machine import I2C,Pin         #从machine模块导入I2C、Pin子模块
from ssd1306 import SSD1306_I2C     #从ssd1306模块中导入SSD1306_I2C子模块

class WINDOW:
    #传入菜单的数据列表
    def __init__(self,list,fa):
        self.oled=SSD1306_I2C(128, 64, I2C(0), addr=0x3c)
        self.oled.font_load("GB2312-24.fon")
        self.oled.fill(0)
        self.data=list#文本数据
        self.father=fa#父级菜单，father是个MENU类

    #绘制文字
    def __text(self):
        for i in range(len(self.data)):
            self.oled.text(self.data[i],15,i*16)

    def display(self):
        self.oled.fill(0)
        self.__text()
        self.oled.show()

    #进入光标所在的功能界面,参数传入界面的列表，界面的类中要有display方法
    def back(self):
        self.father.display()

        
        

if __name__=="__main__":
    menu=WINDOW(['lalalal','6666','ccccc'])
    menu.display()


