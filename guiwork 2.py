import sys
from PyQt4 import QtGui
import socket

class Window(QtGui.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()  # SELF CAN REPLACE THE COMMAND WINDOW INSIDE CLASS WINDOW. EG. SELF.SHOW()  for   WINDOW.SHOW()
        self.setGeometry(200,100, 900, 600)  # WINDOW SIZE
        self.setWindowTitle("Radha Communications")   # WINDOW TITLE
        self.setWindowIcon(QtGui.QIcon('LED.png'))   # LOGO AT TOP LEFT CORNER


        
        Exit = QtGui.QAction("Exit", self) # ADDING EXIT BUTTON IN FILE MENU
        Exit.setShortcut("Ctrl+Q")         # SETTING SHORTCUT
        Exit.setStatusTip('Close The Window')
        Exit.triggered.connect(self.close_application)

        Info = QtGui.QAction("Info", self)    #ADDING INFO BUTTON
        Info.setShortcut("Ctrl+I")
        Info.setStatusTip('Information')
        #Info.triggered.connect( )


        Aboutus = QtGui.QAction("About us", self)    #ADDING About us BUTTON
        Aboutus.setStatusTip('About Us')
        #Aboutus.triggered.connect( )


##  pc
        s = socket.socket ()
        s.settimeout (0.25)
        try:
            s.connect (("192.168.0.222", 135))
        except socket.error:
            print ("Reception Pc Offline \n")
            zero="receptionoff.png"
        else:
            print ("Reception Pc Online \n")
            zero="receptionon.png"

        s.close()
#25
        s = socket.socket ()
        s.settimeout (0.25)
        try:
            s.connect (("192.168.0.172", 135))
        except socket.error:
            one="pc1off.png"
        else:
            one="pc1on.png"
            

        s.close()

#24
        s = socket.socket ()
        s.settimeout (0.25)
        try:
            s.connect (("192.168.0.127", 135))
        except socket.error:
            two="pc2off.png"
        else:
            two="pc2on.png"
            

        s.close()

#23
        s = socket.socket ()
        s.settimeout (0.25)
        try:
            s.connect (("192.168.0.38", 135))
        except socket.error:
            three="pc3off.png"
        else:
            three="pc3on.png"
        s.close()

#22
        s = socket.socket ()
        s.settimeout (0.25)
        try:
            s.connect (("192.168.0.114", 135))
        except socket.error:
            four="pc4off.png"
        else:
            four="pc4on.png"

        s.close()
#21
        s = socket.socket ()
        s.settimeout (0.25)
        try:
            s.connect (("192.168.0.128", 135))
        except socket.error:
            five="pc5off.png"
        else:
            five="pc5on.png"     
        s.close()

#20
        s = socket.socket ()
        s.settimeout (0.25)
        try:
            s.connect (("192.168.0.20", 135))
        except socket.error:
            six="pc6off.png"
        else:
            six="pc6on.png"

        s.close()

#19
        s = socket.socket ()
        s.settimeout (0.25)
        try:
            s.connect (("192.168.0.152", 135))
        except socket.error:
            seven="pc7off.png"
        else:
            seven="pc7on.png"

        s.close()
#18
        s = socket.socket ()
        s.settimeout (0.25)
        try:
            s.connect (("192.168.0.153", 135))
        except socket.error:
            eight="pc8off.png"
        else:
            eight="pc8on.png"
        s.close()

#17
        s = socket.socket ()
        s.settimeout (0.25)
        try:
            s.connect (("192.168.0.2", 135))
        except socket.error:
            nine="pc9off.png"
        else:
            nine="pc9on.png"
        s.close()


#16
        s = socket.socket ()
        s.settimeout (0.25)
        try:
            s.connect (("192.168.0.68", 135))
        except socket.error:
            ten="pc10off.png"
        else:
            ten="pc10on.png"
        s.close()

#16
        s = socket.socket ()
        s.settimeout (0.25)
        try:
            s.connect (("192.168.0.11", 135))
        except socket.error:
            eleven="pc11off.png"
        else:
            eleven="pc11on.png"
        s.close()



##---------------------------------------------------------------------------------------------

        
## First coloumn
        
        #hbox = QtGui.QHBoxLayout(self)
        pixmap = QtGui.QPixmap(zero)
        lbl0 = QtGui.QLabel(self)
        lbl0.setPixmap(pixmap)
        #hbox.addWidget(lbl)
        #self.setLayout(hbox)
        lbl0.move(50,90)
        lbl0.resize(120,70)

        pixmap = QtGui.QPixmap(three)
        lbl1 = QtGui.QLabel(self)
        lbl1.setPixmap(pixmap)
        #hbox.addWidget(lbl)
        #self.setLayout(hbox)
        lbl1.move(50,180)
        lbl1.resize(120,70)

        pixmap = QtGui.QPixmap(six)
        lbl2 = QtGui.QLabel(self)
        lbl2.setPixmap(pixmap)
        #hbox.addWidget(lbl)
        #self.setLayout(hbox)
        lbl2.move(50,270)
        lbl2.resize(120,70)

        pixmap = QtGui.QPixmap(nine)
        lbl3 = QtGui.QLabel(self)
        lbl3.setPixmap(pixmap)
        #hbox.addWidget(lbl)
        #self.setLayout(hbox)
        lbl3.move(50,360)
        lbl3.resize(120,70)
        
## second coloumn

        pixmap = QtGui.QPixmap(one)
        lbl4 = QtGui.QLabel(self)
        lbl4.setPixmap(pixmap)
        #hbox.addWidget(lbl)
        #self.setLayout(hbox)
        lbl4.move(200,90)
        lbl4.resize(120,70)

        pixmap = QtGui.QPixmap(four)
        lbl5 = QtGui.QLabel(self)
        lbl5.setPixmap(pixmap)
        #hbox.addWidget(lbl)
        #self.setLayout(hbox)
        lbl5.move(200,180)
        lbl5.resize(120,70)

        pixmap = QtGui.QPixmap(seven)
        lbl6 = QtGui.QLabel(self)
        lbl6.setPixmap(pixmap)
        #hbox.addWidget(lbl)
        #self.setLayout(hbox)
        lbl6.move(200,270)
        lbl6.resize(120,70)

        pixmap = QtGui.QPixmap(ten)
        lbl7 = QtGui.QLabel(self)
        lbl7.setPixmap(pixmap)
        #hbox.addWidget(lbl)
        #self.setLayout(hbox)
        lbl7.move(200,360)
        lbl7.resize(120,70)

## Third coloumn

        pixmap = QtGui.QPixmap(two)
        lbl8 = QtGui.QLabel(self)
        lbl8.setPixmap(pixmap)
        #hbox.addWidget(lbl)
        #self.setLayout(hbox)
        lbl8.move(350,90)
        lbl8.resize(120,70)

        pixmap = QtGui.QPixmap(five)
        lbl9 = QtGui.QLabel(self)
        lbl9.setPixmap(pixmap)
        #hbox.addWidget(lbl)
        #self.setLayout(hbox)
        lbl9.move(350,180)
        lbl9.resize(120,70)

        pixmap = QtGui.QPixmap(eight)
        lbl10 = QtGui.QLabel(self)
        lbl10.setPixmap(pixmap)
        #hbox.addWidget(lbl)
        #self.setLayout(hbox)
        lbl10.move(350,270)
        lbl10.resize(120,70)

        pixmap = QtGui.QPixmap(eleven)
        lbl11 = QtGui.QLabel(self)
        lbl11.setPixmap(pixmap)
        #hbox.addWidget(lbl)
        #self.setLayout(hbox)
        lbl11.move(350,360)
        lbl11.resize(120,70)






##--------------------------------------------------------------------------------------------------


        self.statusBar()
        self.show() #MUST BE ADDED TO SHOW WINDOW
        
        # ADDING MENU BAR ITEMS

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('&File')
        fileMenu.addAction(Exit)
        

        HelpMenu = mainMenu.addMenu('Help')
        HelpMenu.addAction(Info)
        HelpMenu.addAction(Aboutus)

    def close_application(self):            # Close Conformation
        choice = QtGui.QMessageBox.question(self, 'Exit!',
                                            "Are you really want to quit",
                                            QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            print("Exit")
            sys.exit()
        else:
            pass

        
        

        
            


    
    



    



##-------------------------------------------------------------------------------------------------
        
app = QtGui.QApplication(sys.argv)  #DEFINE THE APP
GUI = Window()          #CALLING THE CLASS WINDOW


sys.exit(app.exec_())
