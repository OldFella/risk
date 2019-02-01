import numpy
import PyQt5
import sys
from PyQt5.QtWidgets import *#QMainWindow, QApplication, QWidget, QGraphicsEllipseItem
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import shapely
import copy
import definitions

size = 25

#NA
Alaska = [(0,1),(1,0),(2,0),(2,1.5)]
Alberta = [(0,0), (0,1.5), (3,1.5), (3,0)]
Central_America = [(0,0),(2.5,0), (2.5,1),(3.5,5), (0.5, 1)]
Eastern_US = [(1.3, 0), (4,0), (2, 3), (0,3), (0,2), (1.3,2)]
Greenland = [(0,0.3),(1.5,0.1),(3,0), (4,0.3),(3.5,1.5), (1,3.5),(0.5,3.5),  (0.5,2.3), (1,1.8),(1, 0.5)]
NW_Territory = [(0,0),(0,1),(4,1), (5,0)]
Ontario = [(0,0), (1,0), (2,1), (2,1.5), (0, 1.5)]
Quebec = [(0, 1.5), (0,2), (1,2), (1.8,1), (1,0)]
Western_US = [(1,0), (0,1.8), (1,3), (3,3), (3,2), (4.3,2), (4.3,0)] 

#SA
Argentinia = [(0,0), (2.5,0),(2.2, 2), (3,4),(1.5,3.3)]
Brazil = [(0,1.5), (2,0), (3.7, 1.6), (2,4), (1,4)]
Peru = [(0.5,0), (1.5,0.5),(2.5, 3), (1,3), (0, 0.5)]
Venezuela = [(1,0), (3,1),(1,2.5), (0,2), (0.5,0.5)]

#EU
Great_Britain = [(0,0), (0.2,0), (0.6,1),(0,1.1)]
Iceland = [(0,0), (0.7,0), (0.7,0.5), (0,0.5)]
Northern_Europe = [(0.5,0),(2.5,0),(2.5,0.7),(0.5,0.7), (0,0.2)]
Scandinavia = [(0,1.8),(1,0.5),(1.7,0),(3,0.3),(3,1.5),(2,1.5),(1.8,1.3),(2.3,1),(2,0.8),(1.3,1.5),(1,2.3),(0.7,2.3),(0.7,2),(0,2.3)]
Southern_Europe = [(0,0),(0,0.5),(1.3,2),(1.4,1.8),(0.5,0.5),(0.8,0.5),(2,2.5),(2,2),(2.8,1),(3,0)]
Eastern_Europe = [(1,0),(2,0.3),(4,0.5),(4,2.5),(3,2.5),(3,4.5),(2.5,4.3),(2,3),(0,3),(0,2.3),(1,1.5)]
Western_Europe = [(1.8,0),(2.3,0.5),(2.3,1),(1.8,1.2),(1,2),(0,2),(0,1),(1,1),(1,0.3)]

#AF
Congo = [(0,1.5),(0.5,1.5),(1.5,0),(2.5,1.5),(3,1.5),(2,3),(1,3),(1,2.5),(0,2.5)]
East_Africa = [(0,0.3),(0,1.8),(1,3.3),(1.5,3.3),(0.5,4.8),(2,4.8),(2,3.8),(3,2.8),(4,1.8),(3,1.8),(2.5,0),(0.5,0),(0.5,0.3)]
Egypt = [(0,0),(1.5,0.5),(1.5,0),(3.5,0.5),(3.7,0.7),(3.5,1),(4,1.8),(2,1.8),(2,2),(1.5,2),(0,1)]
Madagascar = [(0.6,0),(0.8,0.2),(0.6,1.6),(0,1.6),(0.1,0.5)]
North_Africa = [(4,0),(4,2),(5.5,3),(5.5,4.5),(4.5,6),(4,6),(4,5.5),(3.5,5),(1.5,5.2),(0,3.5),(0,2.5),(1.5,0.3)]
South_Africa = [(0,0),(1,4),(2,4),(3.5,1),(3.5,0.5),(1,0.5),(1,0)]

#AS
Afghanistan = []
China= []
India = []
Irkutsk = []
Japan = []
Kamchatka = []
Middle_East = []
Mongolia = []
Siam = []
Siberia = []
Ural = []
Yakutsk = []

#AUS
Eastern_Australia = []
Indonesia = []
New_Guinea = []
Western_Australia = []

polygonlist2 = [Alaska,Alberta,Central_America, Eastern_US,Greenland, NW_Territory, Ontario,Quebec, Western_US,
			Argentinia, Brazil, Peru, Venezuela,
			Great_Britain, Iceland, Northern_Europe,Scandinavia, Southern_Europe, Eastern_Europe, Western_Europe,
			Congo, East_Africa, Egypt, Madagascar, North_Africa, South_Africa]

states = list(definitions.graph.keys())

points = []
for point in North_Africa:
			start_x = 13.5*size
			start_y = 7.5*size
			points.append(QPoint(point[0]*size,point[1]*size))
polygon = QPolygon(points)


startpoints = [(size, 2*size),		#Alaska
			(3*size, 3*size),		#Alberta
			(3*size, 7.5*size),		#Central_America
			(5*size, 4.5*size),		#Eastern_US
			(10.5*size, 0.5*size), 	#Greenland
			(3*size, 2*size), 		#NW_Territory
			(6*size, 3*size), 		#Ontario
			(8*size,2.5*size), 		#Quebec
			(2*size, 4.5*size),		#Western_US

			(6.5*size,17*size),		#Argentinia
			(7*size, 13*size),		#Brazil
			(5.5*size, 14*size),	#Peru
			(6*size, 12*size),		#Venezuela

			(15.9*size, 4*size),	#Great_Britain
			(14.2*size, 2.8*size),	#Iceland
			(16.8*size,4.8*size),	#Northern_Europe
			(17.3*size,2.2*size),	#Scandinavia
			(17.3*size,5.5*size),	#Southern_Europe
			(19.3*size,2.5*size),	#Eastern_Europe
			(15*size,5*size),		#Western_Europe

			(17.5*size, 12*size),	#Congo
			(19*size, 10.2*size),	#East_Africa
			(17.5*size, 8.5*size),	#Egypt
			(22*size, 15.2*size),	#Madagascar
			(13.5*size, 7.5*size),	#North_Africa
			(17.5*size,14.5*size)	#South_Africa
			]

class polygons(QMainWindow):

	def __init__(self):
			super().__init__()
			self.buttons = []
			self.initUI()

	def initUI(self):
		#self.statusBar().showMessage('Ready')
		self.setWindowTitle('Polygons')
		self.setGeometry(100, 100, 1000, 600)
		self.setStyleSheet('background-color:#060149;')
		#self.setCentralWidget(buttons)
		pal = 'background-color: '
		color = pal + '#FFFF00;'
		for state in states:
			qpoints = []
			if state.startpoint[0] == -1:
				break
				
			for point in state.shape:
				
				start_x = state.startpoint[0]*size
				start_y = state.startpoint[1]*size
				qpoints.append(QPoint(start_x + point[0]*size,start_y + point[1]*size))

			poly = QPolygon(qpoints)
			button = QPushButton(state.name,self)
			button.setMask(QRegion(poly))
			button.resize(45*size,30*size)
			if state.continent == 'sa':
				color = pal + '#00CBEF;'
			if state.continent == 'eu':
				color = pal + '#FF0000;'
			if state.continent == 'af':
				color = pal + '#F88901;'
			if state.continent == 'na':
				color = pal + '#FFFF00;'
			button.setStyleSheet(color) #+ 'border-width:5px;border-style: solid;border-color: black')
			#button.setStyleSheet()
			self.buttons.append(button)
		#self.button = QPushButton('0,\n None',self)
		#self.button.setMask(QRegion(polygon))
		#self.button.resize(6*size,6*size)
		#self.button.move(13.5*size,7.5*size)
		#self.button.setStyleSheet('background-color:#F88901;')
		self.show()

	def paintEvent(self,Event):
		paint = QPainter()
		paint.begin(self)
		paint.setBrush(Qt.yellow)
		paint.setPen(Qt.black)
		#for x in range(60):
		#	paint.drawLine(0, x*size, 1600, x*size)
		#	paint.drawLine(x*size,0, x*size, 1600)
		# start_x = size
		# start_y = size
		# for x in range(len(polygonlist)):
		# 	qpoints = []
		# 	for point in polygonlist[x]:
		# 		start_x = startpoints[x][0]
		# 		start_y = startpoints[x][1]
		# 		qpoints.append(QPoint(start_x + point[0]*size,start_y + point[1]*size))
		# 	if x == 9:
		# 		paint.setBrush(QColor('#00CBEF'))
		# 	if x == 13:
		# 		paint.setBrush(Qt.red)
		# 	if x == 20:
		# 		paint.setBrush(QColor('#F88901'))
		# 	poly = QPolygon(qpoints)
		# 	paint.drawPolygon(poly)
		# 	#print(poly.size())

		paint.end()

if __name__ == '__main__':

	app = QApplication(sys.argv)
	ex = polygons()
	sys.exit(app.exec_())