import sys
from PyQt5.QtWidgets import QApplication,QWidget,QDesktopWidget,QLineEdit,QLabel
from PyQt5.QtGui import QIcon, QMovie
from PyQt5.Qt import *
from ctypes import cdll
from ctypes.wintypes import HWND
import DataMiner
import random
from system_hotkey import SystemHotkey


def getRandomSet(bits):#Ouputs random string
    num_set = [chr(i) for i in range(48,58)]
    char_set = [chr(i) for i in range(97,123)]
    total_set = num_set + char_set
    value_set = "".join(random.sample(total_set, bits))
    return value_set

"""self.rota = Obj()
        self.scene =  QGraphicsScene(self)
        self.scene.setSceneRect(-self.width*0.285,self.height*0.02,self.width/60,self.height/60)
        self.scene.addItem(self.rota.anitem)
        self.setScene(self.scene)

        self.rota.anim.start()"""

"""
    def paintEvent(self,e):
       painter = QPainter(self)
       painter.setRenderHint(QPainter.Antialiasing)
       painter.setPen(Qt.NoPen)
       painter.setBrush(self.bgColor)
       painter.drawRoundedRect(self.rect(), 20, 20)
"""

BL_outer = 0

class UI(QWidget):#Main window UI
    def hidornot(self):
        self.Dict_input.setVisible("False")
    def getScrnInfo1(self):#Get screen resolution
        Screen = QDesktopWidget()#Define screen as QDW() object
        S_width = Screen.screenGeometry().width()#S_W = screen width
        S_height = Screen.screenGeometry().height()#S_H = scrren height
        return S_width, S_height#Return W,H

    def __init__(self):
        super(UI,self).__init__()
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool)       #--]
        self.setAttribute(Qt.WA_TranslucentBackground)              #  ]
        self.bgColor = QColor(100,100,100,80)#Background Color      #  ] -> Blur Settings
        hWnd = HWND(int(self.winId()))                              #  ]
        cdll.LoadLibrary('aero\\aeroDll.dll').setBlur(hWnd)         #--]
        self.Dict_input = QLineEdit(self)#Define Dictionay Input as QLE() Object
        self.Dict_input.setFocus()
        self.Dict_input.setFocusPolicy(Qt.TabFocus)
        self.width,self.height = self.getScrnInfo1()#Define self.width self.height Screen width height
        self.setGeometry(self.width * 0.2, self.height * 0.08, self.width * 0.6, self.height * 0.05)  # Define window position and size
        self.boolen_counter = 0#initialize translate counter,0 means has not been translated
        self.Empty_QVLayout = QVBoxLayout()
        self.initUI()#Run function initUI()
        self.sub_win = TrnsDspl()#Set sub_windows TrnsDspl()
        self.HotKey = QShortcut(QKeySequence('Alt+M'),self,self.show_excute)

    def show_excute(self):
        if self.isMinimized() or not self.isVisible():
            self.showNormal()
            self.activateWindow()
            self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint | Qt.Tool)
            self.show()
        else:
            self.showMinimized()
            self.setWindowFlags(Qt.SplashScreen)
            self.show()

    def paintEvent(self, e):                                        #--]
        painter = QPainter(self)                                    #  ]
        painter.setRenderHint(QPainter.Antialiasing)                #  ] -> Blur Settings
        painter.setPen(Qt.NoPen)                                    #  ]
        painter.setBrush(self.bgColor)                              #  ]
        painter.drawRoundedRect(self.rect(), 20, 20)                #--]

    def initUI(self):#Main Window Function
        self.Tran_btn = QPushButton(self)#Define translate button
        self.Tran_btn.setShortcut(Qt.Key_Return)#Set hot key "Enter" for translate button
        self.Tran_btn.setIcon(QIcon("DicPic.png"))#Set button icon
        self.Tran_btn.setStyleSheet("background:transparent;border-width:0;border-style:outset;")#Set Translate Button sytle: transparent background and borderless
        self.Tran_btn.setIconSize(QSize(96,96))#Set size of Translate Button icon
        self.Tran_btn.resize(self.height*0.05,self.height*0.05)#Set size of Translate Button
        self.Tran_btn.move(self.width*0.6-self.height*0.05,0)#Set Position of Translate Button
        self.Tran_btn.clicked.connect(lambda:self.prnt_dspl())#Link function prnt_dspl() to Translate Button
        self.Dict_input.resize(self.width*0.565,self.height*0.05)#Set size of Dictionary Input
        self.Dict_input.move(self.width*0.01,0)#Set position of Dictionay Input
        self.Dict_input.setFont(QFont("Calibri Light",24))#Set font of Dictionary Input, Calibri Light, size of 24
        self.Dict_input.setStyleSheet("background:transparent;border-width:0;border-style:outset;color:rgb(210,210,210)")#Set Dictionary Input style: transparent background and borderless

    def prnt_dspl(self):#Display the translate result
        cntner = QWidget()#Define container as QW() Object
        if(self.boolen_counter == 0):#When self.boolen_counter equals 0: When the target has not been translated
            self.Dict_input.setFocus()
            self.Dict_input.setFocusPolicy(Qt.TabFocus)
            trans_tar = self.Dict_input.text()#Define trans_tar as the Dictionary Input
            #print("trans_tar is:",trans_tar)
            self.sub_win.initUI(trans_tar,cntner)#Pass parameter translate target and the container(QWidget) to the sub window
            #print("Backed to UI!")
            self.sub_win.show()#Display the sub window
            #print("sub window Showed!")
            self.boolen_counter = 1#Now the target has been translated
            BL_outer = 1
        else:#When the target has been translated
            self.boolen_counter = 0#Now next traget will be translated
            BL_outer = 0
            self.Dict_input.setText("")#Clear the Dictionary Input for next input
            #print("Text removed!")
            """item_list = list(range(self.sub_win.vbox.count()))
            a = self.sub_win.vbox.count()
            print("item list acquried!")
            item_list.reverse()

            for i in item_list:
                item = self.sub_win.vbox.itemAt(i)
                self.sub_win.vbox.removeItem(item)
                if item.widget():
                    item.widget().deleteLater()
            b = self.sub_win.vbox.count()
            print("all item in layout removed!")
            print("Elements in layout Before:",a,",After:",b)"""
            cntner = None#Clear the container(QWidget) for next define
            self.sub_win.close()#Close the sub window

class TrnsDspl(QWidget):#The translated massage UI
    def getScrnInfo(self):#Get the screen resolution
        Screen = QDesktopWidget()
        S_width = Screen.screenGeometry().width()
        S_height = Screen.screenGeometry().height()
        return S_width, S_height

    def __init__(self):
        super(TrnsDspl, self).__init__()
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool)       #--]
        self.setAttribute(Qt.WA_TranslucentBackground)              #  ]
        self.bgColor = QColor(100,100,100,80)                       #  ] -> Blur Settings
        hWnd = HWND(int(self.winId()))                              #  ]
        cdll.LoadLibrary('aero\\aeroDll.dll').setBlur(hWnd)         #--]
        self.width, self.height = self.getScrnInfo()#Define w,h as screen w,h
        self.move(self.width * 0.2, self.height * 0.13)#Set position of translate window
        self.setFixedWidth(self.width * 0.6)#Set fixed width of translate window
        #print("initUI executed!")
        self.scroll = QScrollArea()#Define self.scroll as the QSA() Object
        self.scroll.setStyleSheet("background:transparent;border-width:0;border-style:outset;")#Set style of self.scroll: transparent background and borderless
        self.scroll.setFixedHeight(self.height * 0.7)#Set self.scroll a fixed height
        self.vbox = QVBoxLayout()#Define self.vbox as a QVBL() Object
        #print("Defined!")

    def paintEvent(self, e):                                        #--]
        painter = QPainter(self)                                    #  ]
        painter.setRenderHint(QPainter.Antialiasing)                #  ] -> Blur Settings
        painter.setPen(Qt.NoPen)                                    #  ]
        painter.setBrush(self.bgColor)                              #  ]
        painter.drawRoundedRect(self.rect(), 20, 20)                #--]

    def initUI(self,trans_tar,cntner):#Window function of translate window
        #print("UI().Dict_input.text() value is:",trans_tar)
        self.AdL_Count(cntner,trans_tar)#Pass parameter container(QWidget) and translate target(string)
        #print("Function executed!")
        self.scroll.setWidget(cntner)#Set Widget of self.scroll(QScrollArea) as container(QWidget)
        #print("scroll setWidget")
        vscrollbar = self.scroll.verticalScrollBar()#Define vscrollbar as self.scroll's verticalScrollBar
        vscrollbar.setStyleSheet("QScrollBar {width:0px;}")#Set style of vscrollbar: width: 0px,
        self.vbox.addWidget(self.scroll)#Add Widget self.scroll(QScrollArea) to self.vbox(QVBoxLayout)
        #print("vbox addWidget")
        self.setLayout(self.vbox)#Set QVBoxLayout as translate window layout
        #print("TrnsDspl initUI completely executed!")

    def AdLbl(self, tmp, trans_val, wFreq):#Function of single message translation
        #print("function starts!")
        Adons1 = QLineEdit(trans_val)#Define Adons as QLE() Object, translate value is inside
        Adons1.setFont(QFont("Microsoft YaHei",18))#Set Font MS YaHei size of 18
        Adons1.setFixedSize(self.width*0.485,self.height*0.04)#Set the Fixed Size
        Adons1.setStyleSheet("background:transparent;border-width:0;border-style:outset;color:rgb(210,210,210)")#Set the style: transparent background and bourderless and Font color
        #print("1 defined")
        wFreq = "wFreq:" + str(wFreq)
        #print("wdefined")
        Adons2 = QLineEdit(wFreq)  # Define Adons as QLE() Object, translate value is inside
        Adons2.setFont(QFont("Microsoft YaHei", 14))  # Set Font MS YaHei size of 18
        Adons2.setFixedSize(self.width * 0.07, self.height * 0.04)  # Set the Fixed Size
        Adons2.setStyleSheet("background:transparent;border-width:0;border-style:outset;color:rgb(100,100,100)")  # Set the style: transparent background and bourderless and Font color
        print("attribute defined!")
        tmp2 = QHBoxLayout()
        tmp2.addWidget(Adons1)
        tmp2.addWidget(Adons2)
        Adons = QWidget()
        Adons.setStyleSheet("background:transparent;border-width:0;border-style:outset")
        Adons.setLayout(tmp2)
        tmp.addWidget(Adons)#Add Widget Adons(QLineEdit) to tmp(QVBoxLayout)
        sep_line = QLabel()#Define seperate line as QL() Object
        sep_line.setFixedSize(QSize(self.width*0.57,2))#Set Fixed Size of seperate line
        Gray_line = QPixmap("FG.png")#Define Gray line as QP() Object and contains image FG.png
        Gray_line.scaled(sep_line.width(),2)#Set gray line's size
        #print("lines Defined!")
        sep_line.setPixmap(Gray_line)#Put gray line(QPixmap) into seperate line(QLabel)
        tmp.addWidget(sep_line)#Add seperate line(QLabel) to tmp(QVBoxLayout)
        #print(trans_val)

    def AdL_Count(self, vbox, trans):#Function of translate
        #print("Function Started!")
        print("trans value is:", trans)
        trans_dict = DataMiner.demi1()#Get translated dictionary from DataMiner.py, and store it into translate dictionary
        print(trans_dict)
        #print("Dict Got!")
        tmp = QVBoxLayout()#Define tmp as QVBoxLayout() Obj
        print("tmp setted!")
        for i in trans_dict:#Transval the whole dictionary
            print(i, "set")
            self.AdLbl(tmp, i['name'], i['wordFreq'])#Put the translate target into tmp(QVBoxLayout)
        vbox.setLayout(tmp)#Set tmp as vbox's layout
        #print("layout Setted!")

class TrayIcon(QSystemTrayIcon,QObject):
    sig_hotkey = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.UI = UI()
        self.tray = QSystemTrayIcon()
        self.tray.setIcon(QIcon("KZ_Dic.ico"))
        self.tray.activated.connect(self.iconClicked)
        self.sig_hotkey.connect(self.MyKey_event)
        self.hk = SystemHotkey()
        self.hk.register(('alt', '0'), callback=lambda x: self.send_key())
        self.menu = QMenu()
        self.quit_ = QAction("QUIT",self,triggered = self.QUIT)
        self.menu.addAction(self.quit_)
        self.tray.setContextMenu(self.menu)

    def send_key(self):
        self.sig_hotkey.emit()

    def MyKey_event(self):
        self.icon_excute()


    def iconClicked(self,times):
        if times == 2 or times == 3:
            self.icon_excute()



    def icon_excute(self):
        if self.UI.isMinimized() or not self.UI.isVisible():
            self.UI.showNormal()
            self.UI.activateWindow()
            self.UI.setWindowFlags(Qt.Window | Qt.FramelessWindowHint | Qt.Tool)
            self.UI.show()
        else:
            self.UI.showMinimized()
            self.UI.setWindowFlags(Qt.SplashScreen)
            self.UI.show()

    def QUIT(self):
        self.tray = None
        sys.exit(app.exec_())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex1 = UI()
    #ex1.show()
    ex3 = TrayIcon()
    ex3.tray.show()
    sys.exit(app.exec_())