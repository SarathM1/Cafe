import sys
from PyQt4 import QtGui
import socket

class ping():
	"""To ping computers"""
	def __init__(self, ip,name, status="off"):
		self.ip = ip
		self.name = name

		self.s =  socket.socket ()
		self.s.settimeout (0.25)

		self.img = self.name + status + '.png'
	
	def ping(self):
	    try:
	        self.s.connect (("192.168.0.172", 135))
	    except socket.error:
	    	self.setImage('off')
	    else:
	        self.setImage('on')
	
	def setImage(self,st):
		self.img = self.name + st + '.png'


    s.close()	
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
        pc1 = ping("192.168.0.172",'pc1')
        
#24
        pc2 = ping("192.168.0.127","pc2")
        
#23
        pc3 = ping("192.168.0.38","pc3")

#22
        pc4 = ping("192.168.0.114","pc4")
        
#21
        pc5 = ping("192.168.0.128","pc5")
        
#20
        pc6 = ping("192.168.0.20","pc6")
        
#19
        pc7 = ping("192.168.0.152","pc7")
        
#18
        pc8 = ping("192.168.0.153","pc8")
        
#17
        pc9 = ping("192.168.0.2","pc9")


#16
        pc10 = ping("192.168.0.128","pc10")

#16
        pc11 = ping("192.168.0.128","pc11")
        


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

        pixmap = QtGui.QPixmap(pc3.img)
        lbl1 = QtGui.QLabel(self)
        lbl1.setPixmap(pixmap)
        #hbox.addWidget(lbl)
        #self.setLayout(hbox)
        lbl1.move(50,180)
        lbl1.resize(120,70)

        pixmap = QtGui.QPixmap(pc6.img)
        lbl2 = QtGui.QLabel(self)
        lbl2.setPixmap(pixmap)
        #hbox.addWidget(lbl)
        #self.setLayout(hbox)
        lbl2.move(50,270)
        lbl2.resize(120,70)

        pixmap = QtGui.QPixmap(pc9.img)
        lbl3 = QtGui.QLabel(self)
        lbl3.setPixmap(pixmap)
        #hbox.addWidget(lbl)
        #self.setLayout(hbox)
        lbl3.move(50,360)
        lbl3.resize(120,70)
        
## second coloumn

        pixmap = QtGui.QPixmap(pc1.img)
        lbl4 = QtGui.QLabel(self)
        lbl4.setPixmap(pixmap)
        #hbox.addWidget(lbl)
        #self.setLayout(hbox)
        lbl4.move(200,90)
        lbl4.resize(120,70)

        pixmap = QtGui.QPixmap(pc4.img)
        lbl5 = QtGui.QLabel(self)
        lbl5.setPixmap(pixmap)
        #hbox.addWidget(lbl)
        #self.setLayout(hbox)
        lbl5.move(200,180)
        lbl5.resize(120,70)

        pixmap = QtGui.QPixmap(pc7.img)
        lbl6 = QtGui.QLabel(self)
        lbl6.setPixmap(pixmap)
        #hbox.addWidget(lbl)
        #self.setLayout(hbox)
        lbl6.move(200,270)
        lbl6.resize(120,70)

        pixmap = QtGui.QPixmap(pc10.img)
        lbl7 = QtGui.QLabel(self)
        lbl7.setPixmap(pixmap)
        #hbox.addWidget(lbl)
        #self.setLayout(hbox)
        lbl7.move(200,360)
        lbl7.resize(120,70)

## Third coloumn

        pixmap = QtGui.QPixmap(pc2.img)
        lbl8 = QtGui.QLabel(self)
        lbl8.setPixmap(pixmap)
        #hbox.addWidget(lbl)
        #self.setLayout(hbox)
        lbl8.move(350,90)
        lbl8.resize(120,70)

        pixmap = QtGui.QPixmap(pc5.img)
        lbl9 = QtGui.QLabel(self)
        lbl9.setPixmap(pixmap)
        #hbox.addWidget(lbl)
        #self.setLayout(hbox)
        lbl9.move(350,180)
        lbl9.resize(120,70)

        pixmap = QtGui.QPixmap(pc8.img)
        lbl10 = QtGui.QLabel(self)
        lbl10.setPixmap(pixmap)
        #hbox.addWidget(lbl)
        #self.setLayout(hbox)
        lbl10.move(350,270)
        lbl10.resize(120,70)

        pixmap = QtGui.QPixmap(pc11.img)
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
