import numpy
import PyQt5
import sys
from PyQt5.QtWidgets import *#QMainWindow, QApplication, QWidget, QGraphicsEllipseItem
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import shapely
import copy
import definitions

size = -1


states = list(definitions.graph.keys())


class frontend(QMainWindow):

	def __init__(self):
			super().__init__()
			self.buttons = []
			self.initUI()

	def initUI(self):

		self.setWindowTitle('Polygons')
		self.setGeometry(100, 100, 1000, 600)
		self.setStyleSheet('background-color:#060149;')
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

			self.buttons.append(button)
		self.show()

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

		paint.end()

if __name__ == '__main__':

	app = QApplication(sys.argv)
	size = app.desktop().screenGeometry().height()/30
	ex = frontend()
	sys.exit(app.exec_())