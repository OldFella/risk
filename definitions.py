class node:

	def __init__(self, name, continent, shape = [],startpoint = (-1,-1),alignment = 'Text-align:center;', fraction = None, units = 0):
		self.name = name
		self.fraction = fraction
		self.units = units
		self.continent = continent
		self.shape = shape
		self.startpoint = startpoint
		self.alignment = alignment


	def print_node(self):
		print(self.name,self.continent, self.fraction, self.units)



test_polygon = [(0.5,0),(1,0),(1,1.8),(0,2),(0,1.5),(0.5,1.5)]

# NA
alaska = node('alaska','na', [(0,1),(1,0),(2,0),(2,1.5)], (1,2))
alberta = node('alberta', 'na', [(0,0), (0,1.5), (3,1.5), (3,0)],(3,3))
central_america = node('central_america', 'na',[(0,0),(2.5,0), (2.5,1),(3.5,5), (0.5, 1)],(3,7.5), 'Text-align:top;')
eastern_us = node('eastern_us', 'na',[(1.3, 0), (4,0), (2, 3), (0,3), (0,2), (1.3,2)],(5,4.5))
greenland = node('greenland', 'na',[(0,0.3),(1.5,0.1),(3,0), (4,0.3),(3.5,1.5), (1,3.5),(0.5,3.5),  (0.5,2.3), (1,1.8),(1, 0.5)],(10.5,0.5))
nw_territory = node('nw_territory', 'na',[(0,0),(0,1),(4,1), (5,0)],(3,2))
ontario = node('ontario', 'na',[(0,0), (1,0), (2,1), (2,1.5), (0, 1.5)],(6,3))
quebec = node('quebec', 'na',[(0, 1.5), (0,2), (1,2), (1.8,1), (1,0)],(8,2.5))
western_us = node('western_us', 'na',[(1,0), (0,1.8), (1,3), (3,3), (3,2), (4.3,2), (4.3,0)],(2,4.5))

# South America
argentina = node('argentina', 'sa',[(0,0), (2.5,0),(2.2, 2), (3,4),(1.5,3.3)],(6.5,17))
brazil = node('brazil', 'sa',[(0,1.5), (2,0), (3.7, 1.6), (2,4), (1,4)],(7,13))
peru = node('peru', 'sa',[(0.5,0), (1.5,0.5),(2.5, 3), (1,3), (0, 0.5)],(5.5,14))
venezuela = node('venezuela', 'sa',[(1,0), (3,1),(1,2.5), (0,2), (0.5,0.5)],(6,12))

# EU
great_britain = node('great_britain', 'eu',[(0,0), (0.2,0), (0.6,1),(0,1.1)],(15.9,4))
iceland = node('iceland', 'eu',[(0,0), (0.7,0), (0.7,0.5), (0,0.5)],(14.2,2.8))
northern_eu = node('northern_eu', 'eu',[(0.5,0),(2.5,0),(2.5,0.7),(0.5,0.7), (0,0.2)],(16.8,4.8))
scandinavia = node('scandinavia', 'eu',[(0,1.8),(1,0.5),(1.7,0),(3,0.3),(3,1.5),(2,1.5),(1.8,1.3),(2.3,1),(2,0.8),(1.3,1.5),(1,2.3),(0.7,2.3),(0.7,2),(0,2.3)],(17.3,2.2))
southern_eu = node('southern_eu', 'eu',[(0,0),(0,0.5),(1.3,2),(1.4,1.8),(0.5,0.5),(0.8,0.5),(2,2.5),(2,2),(2.8,1),(3,0)],(17.3,5.5))
ukraine = node('ukraine', 'eu',[(1,0),(2,0.3),(4,0.5),(4,2.5),(3,2.5),(3,4.5),(2.5,4.3),(2,3),(0,3),(0,2.3),(1,1.5)],(19.3,2.5))
western_eu = node('western_eu', 'eu',[(1.8,0),(2.3,0.5),(2.3,1),(1.8,1.2),(1,2),(0,2),(0,1),(1,1),(1,0.3)],(15,5))

# Asia
afghanistan = node('afghanistan', 'as', [(0,0.5),(1,0.5),(1,0),(2,0),(4,1),(4,2),(2,3.2),(1,2.8),(0.5,1),(0,1)], (22.3,4.5))
china = node('china', 'as',[(0.5,0),(1,0),(3.5,2),(4.8,1.5),(5.1,1.8),(4.8,2),(6.5,3.8),(6.3,4),(4.5,4.5),(4,4.5),(3,3.9),(0.8,2.8),(0.8,2.5),(0,1.7),(0.5,1.4)],(25.8,5.1))
india = node('india', 'as', [(0,0.9),(1.5,0),(2.3,0.8),(2.3,1.1),(4,2),(4,3),(4,3.5),(3.5,3.5),(2.8,4),(2.3,5.8),(2,5.8),(1.5,3),(0.2,2.7)], (24.3,6.8))
irkutsk = node('irkutsk', 'as',[(0,1.4),(1.3,0),(4.3,0.3),(4.8,1.4)],(27,3.7))
japan = node('japan', 'as', test_polygon, (33.5,5.5),'Text-align:right;')
kamchatka = node('kamchatka', 'as',[(0,1.3),(1.7,0),(4,0.2),(3.5,1.8),(3.2,1.3),(3.2,1),(0.8,1.3),(0.8,1.8),(1,1.8),(1.5,2.3),(1.5,3.3),(1,3.3),(1,2.8),(0.5,2.3)],(31.3,2.7), 'Text-align:top;')
middle_east = node('middle_east', 'as', [(0,0.5),(1,0),(1.8,0.3),(2.3,0.5),(2.6,1),(3.3,0.8),(4.3,1.2),(4.5,3),(3,2.5),(2.9,2.3),(2.7,2.3),(2.7,2.6),(3.3,3.5),(3.8,3.5),(4.3,4),(2.2,5.3),(1.2,2.7),(1,2.5),(1,1),(0.2,1)], (20,6.5))
mongolia = node('mongolia', 'as', [(0,0),(5,0),(5.5,0.5),(5.5,2),(6,2.5),(5.8,2.6),(5,2),(4,1.8),(3.7,1.5),(2.5,2)], (26.8,5.1))
siam = node('siam', 'as', [(0,0),(1.5,0.9),(2,0.9), (2,1.5), (2.5,2), (2.5,3),(2,3.5), (1,2.5), (1,3.5),(1.5,4.5),(1.3,4.3),(0.8,3.5),(0.8,2.3) ,(0,1.5)], (28.3,8.7))
siberia = node('siberia', 'as', [(0,0.5),(2,0),(3,0.3),(3.5,1.5),(2.2,2.8),(1.5,2.8),(1.5,2.5)],(24.8,2.3))
ural = node('ural', 'as', [(0,0.2),(1.5,0),(3,2),(3,2.7),(1,1.7),(0,1.7)],(23.3,2.8))
yakutsk = node('yakutsk', 'as',[(0,0),(5.2,0.2),(3.5,1.5),(0.5,1.2)],(27.8,2.5))

# Africa
congo = node('congo', 'af',[(0,1.5),(0.5,1.5),(1.5,0),(2.5,1.5),(3,1.5),(2,3),(1,3),(1,2.5),(0,2.5)],(17.5,12))
east_af = node('east_af', 'af',[(0,0.3),(0,1.8),(1,3.3),(1.5,3.3),(0.5,4.8),(2,4.8),(2,3.8),(3,2.8),(4,1.8),(3,1.8),(2.3,0),(0.5,0),(0.5,0.3)],(19,10.2))
egypt = node('egypt', 'af',[(0,0),(1.5,0.5),(1.5,0),(3.5,0.5),(3.7,0.7),(3.5,1),(3.8,1.8),(2,1.8),(2,2),(1.5,2),(0,1)],(17.5,8.5))
madagascar = node('madagascar', 'af',[(0.6,0),(0.8,0.2),(0.6,1.6),(0,1.6),(0.1,0.5)],(22,15.2))
north_af = node('north_af', 'af',[(4,0),(4,2),(5.5,3),(5.5,4.5),(4.5,6),(4,6),(4,5.5),(3.5,5),(1.5,5.2),(0,3.5),(0,2.5),(1.5,0.3)],(13.5,7.5))
south_af = node('south_af', 'af',[(0,0),(1,4),(2,4),(3.5,1),(3.5,0.5),(1,0.5),(1,0)],(17.5,14.5))

# AUS
eastern_aus = node('eastern_aus', 'aus')
indonesia = node('indonesia', 'aus')
new_guinea = node('new_guinea', 'aus')
western_aus = node('western_aus', 'aus')

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
		yakutsk:[irkutsk, kamchatka, siberia]}#,
		# eastern_aus:[new_guinea, western_aus],
		# indonesia:[new_guinea, western_aus, siam],
		# new_guinea:[eastern_aus, indonesia, western_aus],
		# western_aus:[eastern_aus, indonesia, new_guinea]}


#Colors 

RED = '#FF0000'
YELLOW = '#FFFF00'
GREEN = '#00FF00'
BLUE = '#00F9FD'
PURPLE = '#FA02D4'
WHITE = '#FFFFFF'

#Players

class Player:
	def __init__(self, name, color, units = 0):
		self.name = name
		self. color = color
		self.units = units


red = Player('red', RED)
blue = Player('blue', BLUE)
yellow = Player('yellow', YELLOW)
green = Player('green', GREEN)
purple = Player('purple', PURPLE)
white = Player('white',WHITE)