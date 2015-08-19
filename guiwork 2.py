import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import socket
import time

class worker(QThread):
	
	signal = pyqtSignal(str, list)
	
	def __init__(self,ip,name,movex,movey):
		QThread.__init__(self, parent=app)
		
		self.ip = ip
		self.name = name

		self.movex = movex
		self.movey = movey

		self.s =  socket.socket ()
		
	def run(self):
		print ('Starting '+str(self.name)+' '+str(self.ip))
		try:
			self.s.connect ((self.ip, 135))
		except socket.error as e:
			print('run: '+str(self.name)+' '+str(self.ip)+', '+str(e))
			self.signal.emit(self.name+"off.png", [self.movex,self.movey])
		else:
			self.signal.emit(self.name+"on.png", [self.movex,self.movey])
		
class Window(QMainWindow):

	def __init__(self):
		super(Window, self).__init__()  # SELF CAN REPLACE THE COMMAND WINDOW INSIDE CLASS WINDOW. EG. SELF.SHOW()  for   WINDOW.SHOW()

		

		self.setGeometry(200,100, 900, 600)  # WINDOW SIZE
		self.setWindowTitle("Radha Communications")   # WINDOW TITLE
		self.setWindowIcon(QIcon('LED.png'))   # LOGO AT TOP LEFT CORNER
		
		Exit = QAction("Exit", self) # ADDING EXIT BUTTON IN FILE MENU
		Exit.setShortcut("Ctrl+Q")         # SETTING SHORTCUT
		Exit.setStatusTip('Close The Window')
		Exit.triggered.connect(self.close_application)

		Info = QAction("Info", self)    #ADDING INFO BUTTON
		Info.setShortcut("Ctrl+I")
		Info.setStatusTip('Information')
		
		Aboutus = QAction("About us", self)    #ADDING About us BUTTON
		Aboutus.setStatusTip('About Us')
		
		mainMenu = self.menuBar()
		fileMenu = mainMenu.addMenu('&File')
		fileMenu.addAction(Exit)
		

		HelpMenu = mainMenu.addMenu('Help')
		HelpMenu.addAction(Info)
		HelpMenu.addAction(Aboutus)

		##  pc
		
		#pc0 = self.ping("192.168.1.10","pc0",50,90, self)
		thread = worker("192.168.1.10","pc0",50,90)

		thread.signal.connect(self.testfunc)

		thread.start()
		
		

		#pc1 = self.ping("192.168.1.19","pc1",200,90, self)
		thread = worker("192.168.1.19","pc1",200,90)
		
		thread.signal.connect(self.testfunc)
		thread.start()

		pc2 = self.ping("192.168.0.127","pc2",350,90,self)
		
#23
		pc3 = self.ping("192.168.0.38","pc3",50,180,self)

#22
		pc4 = self.ping("192.168.0.114","pc4",200,180,self)
		
#21
		pc5 = self.ping("192.168.0.128","pc5",350,180,self)
		
#20
		pc6 = self.ping("192.168.0.20","pc6",50,270,self)
		
#19
		pc7 = self.ping("192.168.0.152","pc7",200,270,self)
		
#18
		pc8 = self.ping("192.168.0.153","pc8",350,270,self)
		
#17
		pc9 = self.ping("192.168.0.2","pc9",50,360,self)
		

#16
		pc10 = self.ping("192.168.0.128","pc10",200,360,self)

#16
		pc11 = self.ping("192.168.0.128","pc11",350,360,self)
	
	def testfunc(self, sigstr,cord):
		print ('sigstr: '+ sigstr)
		
		self.img = sigstr
		pixmap = QPixmap(sigstr)
		lbl0 = QLabel(self.obj)
		lbl0.setPixmap(pixmap)
		lbl0.move(cord[0],cord[1])
		lbl0.resize(120,70)
		lbl0.show()

	def ping(self,ip,name, movex , movey , obj ,status="off"):
		self.ip = ip
		self.name = name
		self.obj = obj
		

		self.img = str(self.name) + str(status) + '.png'
		self.movex = movex
		self.movey = movey

	def pingPc(self):
		try:
			self.s.connect ((self.ip, 135))
		except socket.error:
			self.setImage('off')
		else:
			self.setImage('on')
		self.s.close()
		self.setLabel()
	
	def setLabel(self):
		pixmap = QPixmap(self.img)
		self.lbl = QLabel(self.obj)
		self.lbl.setPixmap(pixmap)
		self.lbl.move(self.movex,self.movey)
		self.lbl.resize(120,70)


	def setImage(self,st):
		self.img = str(self.name) + (st) + '.png'
	



	def close_application(self):            # Close Conformation
		choice = QMessageBox.question(self, 'Exit!',
											"Do you really want to quit",
											QMessageBox.Yes | QMessageBox.No)
		if choice == QMessageBox.Yes:
			print("Exit")
			sys.exit()
		else:
			pass



##-------------------------------------------------------------------------------------------------
		
app = QApplication(sys.argv)  #DEFINE THE APP
GUI = Window()          #CALLING THE CLASS WINDOW
GUI.show()
GUI.statusBar()
sys.exit(app.exec_())
