from machine import I2C,Pin         #从machine模块导入I2C、Pin子模块
from ssd1306 import SSD1306_I2C     #从ssd1306模块中导入SSD1306_I2C子模块

class MENU:
    #传入菜单的数据列表
    def __init__(self,list):
        self.oled=SSD1306_I2C(128, 64, I2C(0), addr=0x3c)
        self.oled.font_load("GB2312-12.fon")
        self.oled.fill(0)
        self.widarr=1#当前箭头在屏幕上的第几个1,2,3,4
        self.arrow=1#当前箭头在整个菜单表的第几个
        self.data=list#菜单数据
        #self.son=None

    #绘制文字
    def __text(self):
        if(self.arrow==len(self.data)):
            for i in range(4):
                self.oled.text(self.data[i+(len(self.data)-4)],15,i*16)
            return        
        for i in range(4):
            self.oled.text(self.data[i+(self.arrow-self.widarr)],15,i*16)

    #绘制箭头（不是）
    def __arrow(self):
        if(self.widarr<=4):
            self.oled.vline(0,(self.widarr-1)*16+1, 10, 1)
            self.oled.vline(1,(self.widarr-1)*16+2, 8, 1)
            self.oled.vline(2,(self.widarr-1)*16+3, 6, 1)
            self.oled.vline(3,(self.widarr-1)*16+4, 4, 1)
            self.oled.vline(4,(self.widarr-1)*16+5, 2, 1)
        if(self.widarr>4):
            self.oled.vline(0,49, 10, 1)
            self.oled.vline(1,50, 8, 1)
            self.oled.vline(2,51, 6, 1)
            self.oled.vline(3,52, 4, 1)
            self.oled.vline(4,53, 2, 1)
    #测边框绘制
    def __border(self):      
        hight=4/(len(self.data)+1)
        hight*=68 
        start=(self.arrow-self.widarr)/(len(self.data)+1)
        start*=68
        self.oled.vline(127, round(start), round(hight), 1)
        self.oled.vline(126, round(start), round(hight), 1)    

    def display(self):
        self.oled.fill(0)
        self.__arrow()
        self.__text()
        self.__border()
        self.oled.show()

    #上翻
    def menu_pageUp(self):
        if(self.arrow>1):
            self.arrow-=1
            if(self.widarr>1):
                self.widarr-=1 
        self.display()

    #下翻 
    def menu_pageDown(self):
        if(self.arrow<len(self.data)):
            self.arrow+=1
            if(self.widarr<4):
                self.widarr+=1 
        self.display()
        
        

if __name__=="__main__":
    menu=MENU(['天气','时间','游戏','设置','关于','666','7777','巴拉巴拉'])
    menu.display()


