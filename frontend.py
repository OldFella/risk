import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QTableWidget, QTableWidgetItem
from PyQt5.QtWidgets import	QVBoxLayout, QGridLayout, QLabel, QWidget, QHBoxLayout, QLineEdit, QTextEdit
from PyQt5.QtGui import QPainter, QPolygon, QRegion, QFont, QPalette, QPen
from PyQt5.QtCore import QPoint, Qt

import definitions
import numpy
import gamerules


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
			self.number_of_players = number_of_players
			if number_of_players < 3:
				number_of_players = 3
			if number_of_players > 6:
				number_of_players = 6
			self.players = gamerules.colors[0:number_of_players]
			self.give_mission_to_players()
			start_armys = gamerules.start_armys(number_of_players)
			for player in self.players:
				player.units = start_armys
			self.initializedStates = list(definitions.graph.keys())
			self.lastplayer = self.players[number_of_players-1]
			self.currentPhase = 'Inititialization'
			self.selected_attacking_state = None
			self.selected_defending_state = None
			self.selected_from_state = None
			self.selected_to_state = None
			self.toggle = True
			self.connected_actions = {}
			self.size_width = self.width/43
			self.size_height = self.height/24
			self.startpoint = (2* self.size_width, self.size_height)
			self.initUI()
			#self.debug_init()
			


	def initUI(self):

		self.setWindowTitle('frontend')
		self.setGeometry(0, 0, self.width, self.height)
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
			
			button.clicked.connect(self.onClick_init)
			self.connected_actions[button] = self.onClick_init
			button.setStyleSheet(color) 

			

			self.buttons[button] = state

		TableButton = QPushButton('Overview',self)
		TableButton.clicked.connect(self.onClick_Table)

		self.textfield1 = QLabel(self)
		self.textfield2 = QLabel(self)
		self.textfield1.setStyleSheet('Color : #FFFFFF')
		self.textfield2.setStyleSheet('Color : #FFFFFF')
		self.textfield1.setText('Attacking:')
		self.textfield2.setText('Defending:')
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
		self.attacking_button.setText('Attack')

		self.infofield = QTextEdit(self)
		self.infofield.setStyleSheet('background-color: #FFFFFF')
		self.infofield.move(1*self.size_width, 21.6*self.size_height)
		self.infofield.resize(37*self.size_width, 0.7*self.size_height)

		self.movingfield1 = QLineEdit(self)
		self.movingfield1.setStyleSheet('background-color: #FFFFFF')
		self.movingfield1.move(38*self.size_width, 13 * self.size_height)
		self.movingtextfield1 = QLabel(self)
		self.movingtextfield2 = QLabel(self)
		self.movingtextfield1.setStyleSheet('Color: #FFFFFF')
		self.movingtextfield2.setStyleSheet('Color: #FFFFFF')
		self.movingtextfield1.move(38*self.size_width, 12 * self.size_height)
		self.movingtextfield2.move(38*self.size_width, 14 * self.size_height)
		self.movingtextfield1.setText('From:')
		self.movingtextfield2.setText('To:')
		self.moving_button = QPushButton(self)
		self.moving_button.move(38*self.size_width, 15 * self.size_height)
		self.moving_button.setText('Move')
		self.moving_button.clicked.connect(self.onClick_movebutton)

		self.continue_button = QPushButton(self)
		self.continue_button.setText('Continue')
		self.continue_button.move(38*self.size_width, 17 * self.size_height)
		self.continue_button.clicked.connect(self.onClick_continue_button)

		self.showMaximized()

	def onClick_Test(self):
		thisButton = self.sender()
		thisState = self.buttons[thisButton]
		test = gamerules.calculate_connected_states(thisState)
		s = ''
		for state in test:
			s += state.name + ' '
		print(s)


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
			self.connected_actions[button] = self.onClick_beginning_Phase
		self.set_states_to_player()
		for player in self.players:
			print(player.name)
			for continent in player.states:
				print(continent)
				for state in player.states[continent]:
					print(state.name)
		self.calculate_begin()

		self.initializedStates = []



	def give_mission_to_players(self):
		missions = definitions.available_missions(self.number_of_players)

		for player in self.players:
			mission = numpy.random.choice(missions)
			player.mission = mission
			player.mission.player = player
			player.mission.update_mission
			missions.remove(mission)
			print(player.name, mission.explanation)

	def set_states_to_player(self):
		for state in states:
			
			if state.fraction.name == 'blue':
				definitions.blue_states_dic[state.continent].append(state)
			elif state.fraction.name == 'red':
				definitions.red_states_dic[state.continent].append(state)
			elif state.fraction.name == 'green':
				definitions.green_states_dic[state.continent].append(state)
			elif state.fraction.name == 'yellow':
				definitions.yellow_states_dic[state.continent].append(state)
			elif state.fraction.name == 'purple':
				definitions.purple_states_dic[state.continent].append(state)
			elif state.fraction.name == 'white':
				definitions.white_states_dic[state.continent].append(state)
		definitions.blue.states = definitions.blue_states_dic
		definitions.red.states = definitions.red_states_dic
		definitions.green.states = definitions.green_states_dic
		definitions.yellow.states = definitions.yellow_states_dic
		definitions.purple.states = definitions.purple_states_dic
		definitions.white.states = definitions.white_states_dic

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
			thisPlayer.states[thisState.continent].append(thisState)
			
			self.players = self.players[1:]
			self.players.append(thisPlayer)
			self.repaint()

		if self.lastplayer.units == 0:
			self.set_states_to_player()
			for button in list(self.buttons.keys()):
				button.clicked.connect(self.onClick_beginning_Phase)
				button.clicked.disconnect(self.connected_actions[button])
				self.connected_actions[button] = self.onClick_beginning_Phase

			self.calculate_begin()
			self.repaint()



	def calculate_begin(self):
		
		current_player = self.players[0]
		additional_units = gamerules.calculate_additional_armys(current_player)
		current_player.units = additional_units
		for button in self.buttons.keys():
			if self.connected_actions[button] != None:
				
				button.clicked.disconnect(self.connected_actions[button])
				button.clicked.connect(self.onClick_beginning_Phase)
				self.connected_actions[button] = self.onClick_beginning_Phase
		self.currentPhase = 'Reinforcement'
		

	def onClick_beginning_Phase(self):
		
		current_player = self.players[0]
		
		current_button = self.sender()
		current_state = self.buttons[current_button]
		if current_player.units > 0 and current_state.fraction == current_player:
			current_state.units += 1
			current_player.units -= 1
			current_button.setText(str(current_state.units))
			
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
				self.connected_actions[button] = self.onClick_attacking
			else:
				button.clicked.connect(self.onClick_defending)
				self.connected_actions[button] = self.onClick_defending
		self.attacking_button.clicked.connect(self.onClick_attackbutton)
		self.attacking_button.setText('Attack')
		self.attacking_button.setStyleSheet('background-color: #FF0000')


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
			if defending_state.fraction == attacking_state.fraction:
				self.players[0].states[defending_state.continent].append(defending_state)
				defending_button.clicked.connect(self.onClick_attacking)
				defending_button.clicked.disconnect(self.onClick_defending)
				self.set_states_to_player()
			self.input1.clear()
			self.input2.clear()
			self.infofield.append(answer)
		except Exception as e:
			print(e)
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



	def onClick_moving(self):
		current_button = self.sender()
		current_state = self.buttons[current_button]
		if self.toggle:
			self.selected_from_state = current_state
			self.movingtextfield1.setText('From: ' + current_state.name)
		
		else:
			self.selected_to_state = current_state
			self.movingtextfield2.setText('to: ' + current_state.name) 
		self.toggle = not self.toggle


	def init_moving_phase(self):
		for button in self.buttons.keys():
			button.clicked.disconnect(self.connected_actions[button])
			button.clicked.connect(self.onClick_moving)
			self.connected_actions[button] = self.onClick_moving
		self.currentPhase = 'Moving'
		self.attacking_button.clicked.disconnect(self.onClick_attackbutton)
		self.clear_textlabels()
		
		self.toggle = True
		self.repaint()


	def onClick_movebutton(self):
		#print(self.currentPhase)
		if not self.currentPhase == 'Moving':
			self.infofield.append('wrong phase')
			return 
		from_state = self.selected_from_state
		to_state = self.selected_to_state
		buttons = list(self.buttons.keys())
		from_button = buttons[list(self.buttons.values()).index(from_state)]
		to_button = buttons[list(self.buttons.values()).index(to_state)]
		moving_troops = int(self.movingfield1.text())
		if not moving_troops < from_state.units:
			self.infofield.append('to much units')
			return

		connected_from = gamerules.calculate_connected_states(from_state)
		if to_state in connected_from:
			from_state.units -= moving_troops
			to_state.units += moving_troops
			from_button.setText(str(from_state.units))
			to_button.setText(str(to_state.units))
			self.repaint()

		else:
			self.infofield.append('states are not connected')



	def nextPlayer(self):
		firstplayer = self.players[0]
		firstplayer.mission.check_mission_complete()
		if firstplayer.mission.missioncomplete:
			print(firstplayer.name, 'won')
			return
		self.players = self.players[1:]
		for player in self.players:
			gamerules.check_player_alive(player)
			if not player.alive:
				self.players.remove(player)
		self.players.append(firstplayer)
		
		self.calculate_begin()
		self.clear_textlabels()
		self.repaint()


	def onClick_continue_button(self):
		
		if self.currentPhase == 'Attacking':
			self.init_moving_phase()
		elif self.currentPhase == 'Moving':
			self.nextPlayer()




	def clear_textlabels(self):
		self.textfield1.setText('Attacking:')
		self.textfield2.setText('Defending')
		self.movingtextfield1.setText('From:')
		self.movingtextfield2.setText('To:')
		

	def paintEvent(self,Event):
		paint = QPainter()
		paint.begin(self)
		paint.setBrush(Qt.yellow)
		paint.setPen(Qt.black)
		for x in range(39):
			if x < 21.5:
				paint.drawLine(self.size_width, x*self.size_height, self.width - 5*self.size_width, x*self.size_height)

			paint.drawLine(x*self.size_width,self.size_height, x*self.size_width, self.height -  2.5*self.size_height)
		paint.drawLine(self.size_width, 21.5*self.size_height, self.width - 5*self.size_width, 21.5*self.size_height)
		start_x = self.size_width
		start_y = self.size_height
		paint.setPen(Qt.white)
		paint.setFont(QFont('Decorative', 10))
		paint.drawText(Event.rect(),Qt.AlignRight,(self.players[0].name + ': '+ str(self.players[0].units)))
		paint.drawText(start_x*19,start_y ,self.currentPhase)

		paint.setPen(QPen(Qt.white, 2))

		gap_x = 0.3 * self.size_width
		gap_y = 0.3 * self.size_height

		paint.drawLine(11.5 * self.size_width + gap_x, 15 * self.size_height - gap_y, 14.5 * self.size_width - gap_x, 11.5 * self.size_height + gap_y)
		
		paint.drawLine(self.size_width , 3.5 * self.size_height, 2 * self.size_width - gap_x, 3.5 * self.size_height)
		paint.drawLine(36.3 * self.size_width + gap_x, 3.5 * self.size_height, 38 * self.size_width, 3.5 * self.size_height)
		
		paint.drawLine(9 * self.size_width + gap_x, 2.5 * self.size_height - gap_y, 11.5 * self.size_width - gap_x, 1.3 * self.size_height + gap_y)
		paint.drawLine(8.5 * self.size_width + gap_x, 4 * self.size_height - gap_y, 11.5 * self.size_width - gap_x, 1.3 * self.size_height + gap_y)
		paint.drawLine(10.8 * self.size_width, 4 * self.size_height - gap_y, 11.5 * self.size_width - gap_x, 1.3 * self.size_height + gap_y)

		paint.drawLine(15 * self.size_width + gap_x, 2.5 * self.size_height + gap_y, 15.8 * self.size_width - gap_x, 3.3 * self.size_height - gap_y)

		paint.end()

if __name__ == '__main__':

	app = QApplication(sys.argv)
	width = app.desktop().screenGeometry().width()
	height = app.desktop().screenGeometry().height()
	ex = frontend(6, width, height)
	sys.exit(app.exec_())