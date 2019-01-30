import numpy
import PyQt5
import sys
from PyQt5.QtWidgets import *#QMainWindow, QApplication, QWidget, QGraphicsEllipseItem
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import copy


class node:

	def __init__(self, name, continent, fraction = None, units = 0):
		self.name = name
		self.fraction = fraction
		self.units = units
		self.continent = continent 


	def print_node(self):
		print(self.name,self.continent, self.fraction, self.units)

players = []

# ----------------------------------------------------------- #

# NA
alaska = node('alaska','na')
alberta = node('alberta', 'na')
central_america = node('central_america', 'na')
eastern_us = node('eastern_us', 'na')
greenland = node('greenland', 'na')
nw_territory = node('nw_territory', 'na')
ontario = node('ontario', 'na')
quebec = node('quebec', 'na')
western_us = node('western_us', 'na')

# South America
argentina = node('argentina', 'sa')
brazil = node('brazil', 'sa')
peru = node('peru', 'sa')
venezuela = node('venezuela', 'sa')

# EU
great_britain = node('great_britain', 'eu')
iceland = node('iceland', 'eu')
northern_eu = node('northern_eu', 'eu')
scandinavia = node('scandinavia', 'eu')
southern_eu = node('southern_eu', 'eu')
ukraine = node('ukraine', 'eu')
western_eu = node('western_eu', 'eu')

# Asia
afghanistan = node('afghanistan', 'as')
china = node('china', 'as')
india = node('india', 'as')
irkutsk = node('irkutsk', 'as')
japan = node('japan', 'as')
kamchatka = node('kamchatka', 'as')
middle_east = node('middle_east', 'as')
mongolia = node('mongolia', 'as')
siam = node('siam', 'as')
siberia = node('siberia', 'as')
ural = node('ural', 'as')
yakutsk = node('yakutsk', 'as')

# Africa
congo = node('congo', 'af')
east_af = node('east_af', 'af')
egypt = node('egypt', 'af')
madagascar = node('madagascar', 'af')
north_af = node('north_af', 'af')
south_af = node('south_af', 'af')

# AUS
eastern_aus = node('eastern_aus', 'aus')
indonesia = node('indonesia', 'aus')
new_guinea = node('new_guinea', 'aus')
western_aus = node('western_aus', 'aus')

# ----------------------------------------------------------- #

colors = ['blue', 'green', 'red', 'yellow', 'purple']
nodes = [alaska, alberta,central_america, eastern_us, greenland, nw_territory, ontario, quebec, western_us,
 argentina, brazil, peru, venezuela,
 great_britain, iceland, northern_eu, scandinavia, southern_eu, ukraine, western_eu,
 congo, east_af, egypt, madagascar, north_af, south_af,
 afghanistan, china, india, irkutsk, japan, kamchatka, middle_east, mongolia, siam, siberia, ural, yakutsk,
 eastern_aus, indonesia, new_guinea, western_aus]
graph = {alaska:[alberta, nw_territory, kamchatka],
		alberta:[alaska, nw_territory, ontario, western_us],
		central_america:[eastern_us, western_us, venezuela],
		eastern_us:[central_america, eastern_us, ontario, quebec],
		greenland:[nw_territory, ontario, quebec, iceland],
		nw_territory:[alaska, alberta, ontario, greenland],
		ontario:[alberta, eastern_us, greenland, nw_territory, quebec, western_us],
		quebec:[eastern_us, greenland, ontario],
		western_us:[alberta,central_america, eastern_us, ontario],
		argentina:[brazil, peru],
		brazil:[argentina, peru, venezuela, north_af],
		peru:[argentina, brazil, venezuela],
		venezuela:[brazil, peru, central_america],
		great_britain:[iceland, northern_eu, scandinavia, western_eu],
		iceland:[great_britain, scandinavia, greenland],
		northern_eu:[great_britain, scandinavia, southern_eu, ukraine],
		scandinavia:[great_britain, iceland, northern_eu, ukraine],
		southern_eu:[northern_eu, ukraine, middle_east, north_af, egypt],
		ukraine:[northern_eu, scandinavia, southern_eu, middle_east, afghanistan, ural],
		western_eu:[great_britain, northern_eu, southern_eu, north_af],
		congo:[east_af, south_af, north_af],
		east_af:[congo, egypt, madagascar, south_af, middle_east],
		egypt:[east_af, north_af, southern_eu, middle_east],
		madagascar:[east_af,south_af],
		north_af:[congo, east_af, egypt, western_eu, southern_eu, brazil],
		south_af:[congo, east_af, madagascar],
		afghanistan:[china, india, middle_east, ural],
		china:[afghanistan, india, mongolia, siberia, ural, siam],
		india:[afghanistan, china, middle_east, siam],
		irkutsk:[kamchatka, mongolia, siberia, yakutsk],
		japan:[kamchatka, mongolia],
		kamchatka:[irkutsk, japan, mongolia, yakutsk, alaska],
		middle_east:[afghanistan, india, east_af, egypt, southern_eu, ukraine],
		mongolia:[china, irkutsk, japan, yakutsk, siberia, kamchatka],
		siam:[china, india, indonesia],
		siberia:[china, irkutsk, mongolia, yakutsk, ural],
		ural:[afghanistan, china, siberia, ukraine],
		yakutsk:[irkutsk, kamchatka, siberia],
		eastern_aus:[new_guinea, western_aus],
		indonesia:[new_guinea, western_aus, siam],
		new_guinea:[eastern_aus, indonesia, western_aus],
		western_aus:[eastern_aus, indonesia, new_guinea]}


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
	if defending_state not in graph[attacking_state]:
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



siam.fraction = Qt.blue
siam.units = 10
indonesia.fraction = Qt.red
indonesia.units = 3
# indonesia.print_node()
# siam.print_node()
# attack(siam, indonesia, 9, 2)
# attack(siam, indonesia, siam.units-1, indonesia.units)

if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    ex = Risk()
    sys.exit(app.exec_())
