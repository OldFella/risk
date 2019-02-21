import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QTableWidget, QTableWidgetItem, QVBoxLayout, QGridLayout, QLabel, QWidget, QHBoxLayout, QLineEdit, QTextEdit
from PyQt5.QtGui import QPainter, QPolygon, QRegion, QFont, QPalette
from PyQt5.QtCore import QPoint, Qt
#import shapely
import copy
import definitions
import numpy
import gamerules
import tkinter

root = tkinter.Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()

red = ['#FF0000;', '#CC0000;', '#990000;','#770000','#FF3333','#CC3333','#993333']
yellow = ['#888800', '#AAAA22','#CCCC44','#444400','#FFFF22']


states = list(definitions.graph.keys())


def getRandomColor():
	color = '#'
	for x in range(6):
		random_number = numpy.random.randint(0,16)
		if random_number < 10:
			color += (str(random_number))
		elif random_number == 10:
			color += 'A'
		elif random_number == 11:
			color += 'B'
		elif random_number == 12:
			color += 'C'
		elif random_number == 13:
			color += 'D'
		elif random_number == 14:
			color += 'E'
		elif random_number == 15:
			color += 'F'
	return color


class frontend(QMainWindow):

	def __init__(self,number_of_players, w, h):
			super().__init__()
			self.buttons = {}
			self.width = width
			self.height = height
			self.player1 = True 
			self.tabletoggle = True
			if number_of_players < 3:
				number_of_players = 3
			if number_of_players > 6:
				number_of_players = 6
			self.players = gamerules.colors[0:number_of_players]
			start_armys = gamerules.start_armys(number_of_players)
			for player in self.players:
				player.units = start_armys
			self.initializedStates = list(definitions.graph.keys())
			self.lastplayer = self.players[number_of_players-1]
			self.currentPhase = 'Inititialization'
			self.selected_attacking_state = None
			self.selected_defending_state = None
			self.size_width = self.width/43
			self.size_height = self.height/22.5
			self.startpoint = (self.size_width, self.size_height)
			self.initUI()
			self.debug_init()
			#gamerules.calculate_missing_edges(definitions.graph)


	def initUI(self):

		self.setWindowTitle('frontend')
		self.setGeometry(0, 0, self.width, self.height)
		self.setStyleSheet('background-color:#060149;')

		#button_widget = QWidget(self)
		#button_layout = QFormLayout()
		#button_widget.setLayout(button_layout)
		#self.mainLayout = QVBoxLayout()
		pal = 'background-color: '
		color = pal + '#FFFF00;'
		for state in states:
			qpoints = []
			if state.startpoint[0] == -1:
				break
			
			max_x = -1
			max_y = -1
			min_x = 100
			min_y = 100
			for point in state.shape:
				if point[0] > max_x:
					max_x = point[0]
				if point[0] < min_x:
					min_x = point[0]
				if point[1] > max_y:
					max_y = point[1]
				if point[1] < min_y:
					min_y = point[1]
				
				start_x = state.startpoint[0]*self.size_width
				start_y = state.startpoint[1]*self.size_height
				qpoints.append(QPoint(point[0]*self.size_width,point[1]*self.size_height))

			poly = QPolygon(qpoints)
			button = QPushButton(self)
			button.setMask(QRegion(poly))
			button.move((state.startpoint[0]*(self.size_width))+ self.startpoint[0],(state.startpoint[1]*(self.size_height))+ self.startpoint[1])
			button.resize((max_x-min_x)*(self.size_width),(max_y-min_y)*(self.size_height))
			random_color = getRandomColor()
			color = pal + random_color
			# random_number = numpy.random.randint(0,7)
			# if state.continent == 'sa':
			# 	color = pal + '#00CBEF;'
			# if state.continent == 'eu':
			# 	color = pal + red[random_number]
			# if state.continent == 'af':
			# 	color = pal + '#F88901;'
			# if state.continent == 'na':
			# 	color = pal + '#FFFF00'#yellow[random_number]
			button.clicked.connect(self.onClick_init)
			button.setStyleSheet(color) #+ 'border-width:5px;border-style: solid;border-color: black')

			

			self.buttons[button] = state
			#button_layout.addWidget(button)

		TableButton = QPushButton('Overview',self)
		TableButton.clicked.connect(self.onClick_Table)

		#main_widget = QWidget(self)
		#textfieldLayout = QVBoxLayout()
		#textfieldLayout.addStretch()
		#main_widget.setLayout(textfieldLayout)
		self.textfield1 = QLabel(self)
		self.textfield2 = QLabel(self)
		self.textfield1.setStyleSheet('Color : #FFFFFF')
		self.textfield2.setStyleSheet('Color : #FFFFFF')
		self.textfield1.setText('text 1')
		self.textfield2.setText('text 2')
		self.textfield1.move(38*self.size_width, 5*self.size_height)
		self.textfield2.move(38*self.size_width, 8*self.size_height)

		self.input1 = QLineEdit(self)
		self.input2 = QLineEdit(self)
		self.input1.setStyleSheet('background-color: #FFFFFF')
		self.input2.setStyleSheet('background-color: #FFFFFF')
		self.input1.move(38*self.size_width, 6*self.size_height)
		self.input2.move(38*self.size_width, 9*self.size_height)
		self.attacking_button = QPushButton(self)
		self.attacking_button.move(38*self.size_width, 10*self.size_height)

		self.infofield = QTextEdit(self)
		self.infofield.setStyleSheet('background-color: #FFFFFF')
		self.infofield.move(1*self.size_width, 21.6*self.size_height)
		self.infofield.resize(36*self.size_width, 0.7*self.size_height)


		#textfield1.setAlignment(Qt.AlignRight)
		#textfield2.setAlignment(Qt.AlignRight)
		#textfieldLayout.addWidget(textfield1)
		#textfieldLayout.addWidget(textfield2)
		#main_widget.move(35*self.size_width, 10*self.size_height)
		#textfieldLayout.addWidget(button_widget) 
		#button_widget.setAlignment(Qt.AlignCenter)
		#self.setCentralWidget(main_widget)
		self.showFullScreen()


	def onClick_Table(self):
		window = QMainWindow(self)
		window.setWindowTitle('Overview')
		window.setGeometry(200,100,780,580)
		tableWidget = QTableWidget(window)
		tableWidget.setRowCount(18)
		tableWidget.setColumnCount(7)
		for x in range(len(states)):
			tableWidget.setItem(3*numpy.floor(x/7)+0,x%7, QTableWidgetItem(states[x].name))
			tableWidget.setItem(3*numpy.floor(x/7)+1,x%7, QTableWidgetItem(states[x].fraction.name))
			#print(states[x].units)
			tableWidget.setItem(3*numpy.floor(x/7)+2,x%7, QTableWidgetItem(str(states[x].units)))
		tableWidget.resize(780,580)
		window.setStyleSheet('background-color: #FFFFFF')
		window.show()


	def debug_init(self):
		pal = pal = 'background-color: '
		for button in self.buttons.keys():
			firstplayer = self.players[0]
			state = self.buttons[button]
			state.fraction = firstplayer
			state.units = 2
			firstplayer.units -= 2
			button.setText(str(state.units))
			button.setStyleSheet(state.alignment + pal + firstplayer.color)
			self.players = self.players[1:]
			self.players.append(firstplayer)
			button.clicked.disconnect(self.onClick_init)
			button.clicked.connect(self.onClick_beginning_Phase)
		self.calculate_begin()
		self.initializedStates = []

	def onClick_init(self):
		thisButton = self.sender()
		thisState = self.buttons[self.sender()]
		pal = 'background-color: '
		thisPlayer = self.players[0]
		successfullAction = False
		if self.initializedStates != []:

			if thisState in self.initializedStates:

				thisState.units = 1
				thisState.fraction = thisPlayer
				
				thisButton.setStyleSheet(thisState.alignment+pal + thisPlayer.color)
				thisButton.setText(str(thisState.units))

				successfullAction = True
				self.initializedStates.remove(thisState)

		else:

			if thisState.fraction == thisPlayer and thisPlayer.units > 0:
				thisState.units += 1
				thisButton.setText(str(thisState.units))

				successfullAction = True

		if successfullAction:
			thisPlayer.units -= 1
			#print(thisPlayer.name, ' ',thisPlayer.units)
			self.players = self.players[1:]
			self.players.append(thisPlayer)
			self.repaint()

		if self.lastplayer.units == 0:
			for button in list(self.buttons.keys()):
				button.clicked.connect(self.onClick_beginning_Phase)
				button.clicked.disconnect(self.onClick_init)
			self.calculate_begin()
			self.repaint()



	def calculate_begin(self):
		#print('calculate_begin')
		current_player = self.players[0]
		additional_units = gamerules.calculate_additional_armys(current_player.name)
		current_player.units = additional_units
		self.currentPhase = 'Reinforcement'
		#print(current_player.units)

	def onClick_beginning_Phase(self):
		#print('onClick_beginning_Phase')
		current_player = self.players[0]
		current_button = self.sender()
		current_state = self.buttons[current_button]
		if current_player.units > 0 and current_state.fraction == current_player:
			current_state.units += 1
			current_player.units -= 1
			current_button.setText(str(current_state.units))
			#print(current_player.units)
			self.repaint()

		if current_player.units == 0:
			self.init_attacking_phase()
			self.currentPhase = 'Attacking'
			self.repaint()



	def init_attacking_phase(self):
		for button in list(self.buttons.keys()):
			button.clicked.disconnect(self.onClick_beginning_Phase)

			if self.buttons[button].fraction == self.players[0]:
				button.clicked.connect(self.onClick_attacking)
			else:
				button.clicked.connect(self.onClick_defending)
		self.attacking_button.clicked.connect(self.onClick_attackbutton)
		self.attacking_button.setText('Attack')

	def onClick_attackbutton(self):
		attacking_state = self.selected_attacking_state
		defending_state = self.selected_defending_state
		try:
			number_attacker = int(self.input1.text())
			number_defender = int(self.input2.text())
			answer = gamerules.attack(attacking_state, defending_state, number_attacker, number_defender)
			buttons = list(self.buttons.keys())
			attacking_button = buttons[list(self.buttons.values()).index(attacking_state)]
			attacking_button.setText(str(attacking_state.units))
			defending_button = buttons[list(self.buttons.values()).index(defending_state)]
			defending_button.setText(str(defending_state.units))
			defending_button.setStyleSheet(defending_state.alignment+'background-color: ' + defending_state.fraction.color)
			self.input1.clear()
			self.input2.clear()
			self.infofield.setText(answer)
		except Exception as e:
			raise e



	def onClick_defending(self):
		current_button = self.sender()
		current_state = self.buttons[current_button]
		if self.selected_attacking_state != None:
			if self.selected_attacking_state in definitions.graph[current_state] and current_state.fraction != self.players[0]:
				self.selected_defending_state = current_state
				self.textfield2.setText('Defending:\n' +  current_state.name+'\n')
				self.repaint()


	def onClick_attacking(self):
		current_button = self.sender()
		current_state = self.buttons[current_button]
		if current_state.fraction == self.players[0]:
			self.selected_attacking_state = current_state
			self.textfield1.setText('Attacking:\n' +  current_state.name)
			self.selected_defending_state = None
			self.repaint()



		

	def paintEvent(self,Event):
		paint = QPainter()
		paint.begin(self)
		paint.setBrush(Qt.yellow)
		paint.setPen(Qt.black)
		for x in range(38):
			if x < 21.5:
				paint.drawLine(self.size_width, x*self.size_height, self.width - 6*self.size_width, x*self.size_height)

			paint.drawLine(x*self.size_width,self.size_height, x*self.size_width, self.height - self.size_height)
		paint.drawLine(self.size_width, 21.5*self.size_height, self.width - 6*self.size_width, 21.5*self.size_height)
		start_x = self.size_width
		start_y = self.size_height
		paint.setPen(Qt.white)
		paint.setFont(QFont('Decorative', 10))
		paint.drawText(Event.rect(),Qt.AlignRight,(self.players[0].name + ': '+ str(self.players[0].units)))
		paint.drawText(start_x*19,start_y ,self.currentPhase)
		# if self.currentPhase == 'Attacking':
		# 	attacking_state_string = 'None'
		# 	defending_state_string = 'None'
		# 	if self.selected_attacking_state != None:
		# 		attacking_state_string = self.selected_attacking_state.name
		# 	if self.selected_defending_state != None:
		# 		defending_state_string = self.selected_defending_state.name

		# 	paint.drawText(Event.rect(), Qt.AlignBottom, ('attacking_state: ' + attacking_state_string + ' defending_state: ' + defending_state_string))

		# for state in states:
		# 	qpoints = []
		# 	if state.startpoint[0] == -1:
		# 		break
				
		# 	for point in state.shape:
				
		# 		start_x = state.startpoint[0]*size
		# 		start_y = state.startpoint[1]*size
		# 		qpoints.append(QPoint(start_x + point[0]*size,start_y + point[1]*size))

		# 	poly = QPolygon(qpoints)
		# 	if state.continent == 'sa':
		# 		color = QColor('#00CBEF')
		# 	if state.continent == 'eu':
		# 		color = QColor('#FF0000')
		# 	if state.continent == 'af':
		# 		color = QColor('#F88901')
		# 	if state.continent == 'na':
		# 		color = QColor('#FFFF00')
		# 	paint.setBrush(color)
		# 	paint.drawPolygon(poly)

		paint.end()

if __name__ == '__main__':

	app = QApplication(sys.argv)
	ex = frontend(6, width, height)
	sys.exit(app.exec_())