import numpy
import PyQt5
import sys
from PyQt5.QtWidgets import *#QMainWindow, QApplication, QWidget, QGraphicsEllipseItem
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import copy
import definitions

players = []

colors = [definitions.blue, definitions.green, definitions.red, definitions.yellow, definitions.purple]


nodes = list(definitions.graph.keys())

def init_graph(nodes):
	for state in nodes:
		state.fraction = None
		state.units = 0

def conquer_state(state, fraction):
	state.fraction = fraction
	state.units = 1

def calculate_additional_armys(player):
	australia = 0
	asia = 0
	europe = 0
	africa = 0
	north_america = 0
	south_america = 0
	total = 0
	result = 0
	for state in nodes:
		if state.fraction == player:
			total += 1
			if state.continent == 'aus':
				australia += 1
			elif state.continent == 'as':
				asia += 1
			elif state.continent == 'eu':
				europe += 1
			elif state.continent == 'af':
				africa += 1
			elif state.continent == 'na':
				north_america += 1
			elif state.continent == 'sa':
				south_america += 1

	if australia == 4:
		result += 2
	if asia == 12:
		result += 7
	if europe == 7:
		result += 5
	if africa == 6:
		result += 3
	if north_america == 9:
		result += 5
	if south_america == 4:
		result += 2

	if int(total/3) < 3:
		result += 3

	else:
		result += int(total/3)
	return result




def start_armys(player):
	return numpy.ceil(2*len(nodes)/player)





def calculate_attack(number_of_attackers, number_of_defenders):
	number_attackers_dice = number_of_attackers
	number_defenders_dice = number_of_defenders
	attackers_result = []
	defenders_result = []
	fallen_attackers = 0
	fallen_defenders = 0
	if number_of_attackers > 3:
		number_attackers_dice = 3
	if number_of_defenders > 2:
		number_defenders_dice = 2

	for x in range(number_attackers_dice):
		dice_result = numpy.random.randint(1,7)
		attackers_result.append(dice_result)

	for x in range(number_defenders_dice):
		dice_result = numpy.random.randint(1,7)
		defenders_result.append(dice_result)

	attackers_result.sort(reverse = True)
	defenders_result.sort(reverse = True)

	r = len(defenders_result)
	if len(attackers_result) < len(defenders_result):
		r = len(attackers_result)

	for x in range(r):
		if attackers_result[x] > defenders_result[x]:
			fallen_defenders += 1
		else:
			fallen_attackers += 1

	return (fallen_attackers,fallen_defenders),(attackers_result, defenders_result)


def attack(attacking_state, defending_state, number_of_attackers, number_of_defenders):
	if defending_state not in definitions.graph[attacking_state]:
		print('states are not neighbours')
		return False
	if number_of_attackers > attacking_state.units -1:
		print('the attacking army isn\'t large enough')
		return False
	if number_of_defenders > defending_state.units:
		print('the defending army isn\'t large enough')
		return False
	if attacking_state.fraction == defending_state.fraction:
		print('you can\'t attack your own state')
		return False
	[fallen, dice_results] = calculate_attack(number_of_attackers, number_of_defenders)
	print('dice results attackers: ', dice_results[0], ' dice results defenders: ' , dice_results[1])
	print('fallen attackers: ', fallen[0], ' fallen defenders: ', fallen[1])
	attacking_state.units -= fallen[0]
	defending_state.units -= fallen[1]
	if defending_state.units == 0:
		conquer_state(defending_state, attacking_state.fraction)
		attacking_state.units -= 1

	attacking_state.print_node()
	defending_state.print_node()
	return True

def init_game(graph = nodes, number_of_players = 2):
	init_graph(graph)
	r = number_of_players
	if number_of_players > len(colors):
		r = len(colors)
	for x in range(r):
		players[x] = colors[x]



class app(QMainWindow):
	def __init__(self):
		super().__init__()
		w = QWidget()
		w.resize(300,300)
		w.move(300,300)
		w.setWindowTitle("risk")
		w.show()



rad = 5
class graphic_node(QGraphicsEllipseItem):

	def __init__(self, path, index):
		super(graphic_node, self).__init__(-rad, -rad, 2*rad, 2*rad)
		self.rad = rad
		self.path = path
		self.index = index



coordinations = [(1,1),
				(2,2),
				(2,4),
				(3,3),
				(6,1),
				(2,1),
				(3,2),
				(4,2),
				(2,3),
				(3,8),
				(4,7),
				(3,7),
				(3,6),
				(8,3),
				(7,2),
				(9,3),
				(9,2),
				(9,4),
				(10,3),
				(8,4),
				(8,7),
				(9,7),
				(9,6),
				(10,7),
				(8,6),
				(9,8),
				(11,3),
				(12,3),
				(11,4),
				(13,2),
				(14,3),
				(14,1),
				(10,4),
				(12,2),
				(12,4),
				(12,1),
				(11,1),
				(13,1),
				(13,7),
				(12,6),
				(13,6),
				(12,7)]

class Risk(QMainWindow):

	currentattack = nodes[0].name
	currentdefend = nodes[0].name
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		#self.statusBar().showMessage('Ready')
		self.setWindowTitle('Risk')
		self.setGeometry(100, 100, 1000, 600)
		self.setStyleSheet('background-color:#060149;')
		comboattacking = QComboBox(self)
		combodefending = QComboBox(self)
		#polygon = QPolygon([QPoint(1,1),QPoint(1,2),QPoint(4,3)])

		states = copy.deepcopy(nodes)
		states.sort(key = lambda x: x.name)
		for state in states:
			comboattacking.addItem(state.name)
			combodefending.addItem(state.name)

		combodefending.move(100,0)
		button = QPushButton('attack',self)
		combodefending.activated[str].connect(self.onActivationD)
		comboattacking.activated[str].connect(self.onActivationA)
		#print(comboattacking.activated)
		button.clicked.connect(self.on_click)
		button.move(200,0)

		#self.setWindowTitle('Statusbar')    
		self.show()


	def onActivationA(self, x):
		self.currentattack = x

	def onActivationD(self,x):
		self.currentdefend = x

	def on_click(self):
		at = None
		de = None
		print(self.currentattack, self.currentdefend)
		for state in nodes:
			if state.name == self.currentattack:
				at = state
			if state.name == self.currentdefend:
				de = state
		print(at.units, de.units)
		attack(at,de, at.units-1, de.units)
		self.repaint()
		

	def paintEvent(self, event):
		paint = QPainter()
		paint.begin(self)
		paint.setBrush(Qt.white)
		paint.setPen(Qt.black)
		#for x in range(20):
		#	paint.drawLine(0, x*70+35, 1600, x*70+35)
		#	paint.drawLine(x*70+35,0, x*70+35, 1600)
		for x in range(len(coordinations)):
			center = QPoint(coordinations[x][0]*70,coordinations[x][1]*70)
			color = (nodes[x].fraction)
			if nodes[x].fraction == None:
				if nodes[x].continent == 'na':
					color = Qt.yellow
				if nodes[x].continent == 'sa':
					color = Qt.red
				if nodes[x].continent == 'eu':
					color = QColor('#00CBEF')
				if nodes[x].continent == 'af':
					color = QColor('#F88901')
				if nodes[x].continent == 'as':
					color = Qt.green
				if nodes[x].continent == 'aus':
					color = QColor('#94054D')

			paint.setBrush(color)
			paint.drawEllipse(center, 35,35)
			#paint.drawRect(coordinations[x][0]*70-35,coordinations[x][1]*70-35, coordinations[x][0]*70 +35,coordinations[x][1]*70+35)
			paint.setPen(Qt.black)
			paint.setFont(QFont('decorative', 7))
			paint.drawText(coordinations[x][0]*70-33,coordinations[x][1]*70, nodes[x].name+' '+ str(nodes[x].units))

		paint.end()



# definitions.siam.fraction = Qt.blue
# definitions.siam.units = 10
# definitions.indonesia.fraction = Qt.red
# definitions.indonesia.units = 3
# # indonesia.print_node()
# # siam.print_node()
# # attack(siam, indonesia, 9, 2)
# # attack(siam, indonesia, siam.units-1, indonesia.units)

# if __name__ == '__main__':
    
#     app = QApplication(sys.argv)

#     ex = Risk()
#     sys.exit(app.exec_())
