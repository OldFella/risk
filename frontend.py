import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QPainter, QPolygon, QRegion, QFont
from PyQt5.QtCore import QPoint, Qt
#import shapely
import copy
import definitions
import numpy
import gamerules

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

	def __init__(self,number_of_players, size = -1):
			super().__init__()
			self.buttons = {}
			self.initUI()
			self.size = size
			self.player1 = True 
			self.tabletoggle = True
			
			if number_of_players > 6:
				number_of_players = 6
			self.players = gamerules.colors[0:number_of_players]
			start_armys = gamerules.start_armys(number_of_players)
			for player in self.players:
				player.units = start_armys
			self.initializedStates = list(definitions.graph.keys())
			self.lastplayer = self.players[number_of_players-1]
			self.currentPhase = 'Inititialiation'


	def initUI(self):

		self.setWindowTitle('frontend')
		self.setGeometry(100, 100, 1000, 600)
		self.setStyleSheet('background-color:#060149;')
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
				
				start_x = state.startpoint[0]*size
				start_y = state.startpoint[1]*size
				qpoints.append(QPoint(point[0]*size,point[1]*size))

			poly = QPolygon(qpoints)
			button = QPushButton(self)
			button.setMask(QRegion(poly))
			button.move(state.startpoint[0]*(size),state.startpoint[1]*(size))
			button.resize((max_x-min_x)*(size),(max_y-min_y)*(size))
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
		TableButton = QPushButton('Overview',self)
		TableButton.clicked.connect(self.onClick_Table)
		self.show()


	def onClick_Table(self):
		window = QMainWindow(self)
		window.setWindowTitle('Overview')
		window.setGeometry(200,100,780,580)
		tableWidget = QTableWidget(window)
		tableWidget.setRowCount(18)
		tableWidget.setColumnCount(7)
		for x in range(len(states)):
			tableWidget.setItem(3*numpy.floor(x/7)+0,x%7, QTableWidgetItem(states[x].name))
			tableWidget.setItem(3*numpy.floor(x/7)+1,x%7, QTableWidgetItem(states[x].fraction))
			#print(states[x].units)
			tableWidget.setItem(3*numpy.floor(x/7)+2,x%7, QTableWidgetItem(str(states[x].units)))
		tableWidget.resize(780,580)
		window.setStyleSheet('background-color: #FFFFFF')
		window.show()


	def onClick_init(self):
		thisButton = self.sender()
		thisState = self.buttons[self.sender()]
		pal = 'background-color: '
		thisPlayer = self.players[0]
		successfullAction = False
		if self.initializedStates != []:

			if thisState in self.initializedStates:

				thisState.units = 1
				thisState.fraction = thisPlayer.name
				
				thisButton.setStyleSheet(thisState.alignment+pal + thisPlayer.color)
				thisButton.setText(str(thisState.units))

				successfullAction = True
				self.initializedStates.remove(thisState)

		else:

			if thisState.fraction == thisPlayer.name and thisPlayer.units > 0:
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
		additional_units = gamerules.calculate_additional_armys(current_player)
		current_player.units = additional_units
		self.currentPhase = 'Reinforcement'
		#print(current_player.units)

	def onClick_beginning_Phase(self):
		#print('onClick_beginning_Phase')
		current_player = self.players[0]
		current_button = self.sender()
		current_state = self.buttons[current_button]
		if current_player.units > 0 and current_state.fraction == current_player.name:
			current_state.units += 1
			current_player.units -= 1
			current_button.setText(str(current_state.units))
			#print(current_player.units)
			self.repaint()

		if current_player.units == 0:
			pass





		

	def paintEvent(self,Event):
		paint = QPainter()
		paint.begin(self)
		paint.setBrush(Qt.yellow)
		paint.setPen(Qt.black)
		for x in range(60):
			paint.drawLine(0, x*size, 1600, x*size)
			paint.drawLine(x*size,0, x*size, 1600)
		start_x = size
		start_y = size
		paint.setPen(Qt.white)
		paint.setFont(QFont('Decorative', 10))
		paint.drawText(Event.rect(),Qt.AlignRight,(self.players[0].name + ': '+ str(self.players[0].units)))
		paint.drawText(size*19,size ,self.currentPhase)
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
	size = app.desktop().screenGeometry().height()/30
	ex = frontend(6, size)
	sys.exit(app.exec_())