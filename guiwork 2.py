import sys
from PyQt4 import QtGui
import socket

class ping():
	"""To ping computers"""
	def __init__(self, ip,name, movex , movey , obj ,status="off"):
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
		self.s.close()
		self.setLabel()
	
	def setLabel(self):
		pixmap = QtGui.QPixmap(self.img)
        self.lbl = QtGui.QLabel(obj)
        self.lbl.setPixmap(pixmap)
        #hbox.addWidget(self.lbl)
        #self.setLayout(hbox)
        self.lbl.move(movex,movey)
        self.lbl.resize(120,70)


	def setImage(self,st):
		self.img = self.name + st + '.png'


    	
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
##  pc
        pc0 = ping("192.168.0.222",50,90, self,'pc0')
#25
        pc1 = ping("192.168.0.172",50,180, self,'pc1')
        
#24
        pc2 = ping("192.168.0.127",50,270,self,"pc2")
        
#23
        pc3 = ping("192.168.0.38",50,360,self,"pc3")

#22
        pc4 = ping("192.168.0.114",200,90,self,"pc4")
        
#21
        pc5 = ping("192.168.0.128",200,180,self,"pc5")
        
#20
        pc6 = ping("192.168.0.20",280,270,self,"pc6")
        
#19
        pc7 = ping("192.168.0.152",280,360,self,"pc7")
        
#18
        pc8 = ping("192.168.0.153",350,90,self,"pc8")
        
#17
        pc9 = ping("192.168.0.2",350,180,self,"pc9")


#16
        pc10 = ping("192.168.0.128",350,270,self,"pc10")

#16
        pc11 = ping("192.168.0.128",350,360,self,"pc11")
        
        #self.statusBar()
        #self.show() #MUST BE ADDED TO SHOW WINDOW
        
        # ADDING MENU BAR ITEMS

        

    

        
        

        
            


    
    



    



##-------------------------------------------------------------------------------------------------
        
app = QtGui.QApplication(sys.argv)  #DEFINE THE APP
GUI = Window()          #CALLING THE CLASS WINDOW
GUI.show()

sys.exit(app.exec_())
