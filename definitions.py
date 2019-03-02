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



# NA
alaska = node('alaska','na', [(0,1),(1,0),(2,0),(2,1.5)], (0,1.5))
alberta = node('alberta', 'na', [(0,0), (0,1.5), (3,1.5), (3,0)],(2,2.5))
central_america = node('central_america', 'na',[(0,0),(2.5,0), (2.5,1),(3.5,5), (0.5, 1)],(2,7), 'Text-align:top;')
eastern_us = node('eastern_us', 'na',[(1.3, 0), (4,0), (2, 3), (0,3), (0,2), (1.3,2)],(4,4))
greenland = node('greenland', 'na',[(0,0.3),(1.5,0.1),(3,0), (4,0.3),(3.5,1.5), (1,3.5),(0.5,3.5),  (0.5,2.3), (1,1.8),(1, 0.5)],(9.5,0))
nw_territory = node('nw_territory', 'na',[(0,0),(0,1),(4,1), (5,0)],(2,1.5))
ontario = node('ontario', 'na',[(0,0), (1,0), (2,1), (2,1.5), (0, 1.5)],(5,2.5))
quebec = node('quebec', 'na',[(0, 1.5), (0,2), (1,2), (1.8,1), (1,0)],(7,2))
western_us = node('western_us', 'na',[(1,0), (0,1.8), (1,3), (3,3), (3,2), (4.3,2), (4.3,0)],(1,4))

# South America
argentina = node('argentina', 'sa',[(0,0), (2.5,0),(1.7, 2), (1.7,3.3),(2.2,4),(1,3.5),(0.5,2.5),(0.2,1.5)],(5.5,16.5))
brazil = node('brazil', 'sa',[(0,1.5), (2,0), (3.5, 1.5), (2,4), (1,4)],(6,12.5))
peru = node('peru', 'sa',[(0.5,0), (1.5,0.5),(2.5, 3), (1,3), (0, 0.5)],(4.5,13.5))
venezuela = node('venezuela', 'sa',[(1,0), (3,1),(1,2.5), (0,2), (0.5,0.5)],(5,11.5))

# EU
great_britain = node('great_britain', 'eu',[(0,0), (0.2,0), (0.6,1),(0,1.1)],(14.9,3.5))
iceland = node('iceland', 'eu',[(0,0), (0.7,0), (0.7,0.5), (0,0.5)],(13.2,2.3))
northern_eu = node('northern_eu', 'eu',[(0.5,0),(2.5,0),(2.5,0.7),(0.5,0.7), (0,0.2)],(15.8,4.3))
scandinavia = node('scandinavia', 'eu',[(0,1.8),(1,0.5),(1.7,0),(3,0.3),(3,1.5),(2,1.5),(1.8,1.3),(2.3,1),
										(2,0.8),(1.3,1.5),(1,2.3),(0.7,2.3),(0.7,2),(0,2.3)],(16.3,1.7))
southern_eu = node('southern_eu', 'eu',[(0,0),(0,0.5),(1.3,2),(1.4,1.8),(0.5,0.5),(0.8,0.5),(2,2.5),(2,2),(2.8,1),(3,0)],(16.3,5))
ukraine = node('ukraine', 'eu',[(1,0),(2,0.3),(4,0.5),(4,2.5),(3,2.5),(3,4.5),(2.5,4.3),(2,3),(0,3),(0,2.3),(1,1.5)],(18.3,2))
western_eu = node('western_eu', 'eu',[(1.8,0),(2.3,0.5),(2.3,1),(1.8,1.2),(1,2),(0,2),(0,1),(1,1),(1,0.3)],(14,4.5))

# Asia
afghanistan = node('afghanistan', 'as', [(0,0.5),(1,0.5),(1,0),(2,0),(4,1),(4,2),(2,3.2),(1,2.8),(0.5,1),(0,1)], (21.3,4))
china = node('china', 'as',[(0.5,0),(1,0),(3.5,2),(4.8,1.5),(5.1,1.8),(4.8,2),(6.5,3.8),(6.3,4),(4.5,4.5),
							(4,4.5),(3,3.9),(0.8,2.8),(0.8,2.5),(0,1.7),(0.5,1.4)],(24.8,4.6))
india = node('india', 'as', [(0,0.9),(1.5,0),(2.3,0.8),(2.3,1.1),(4,2),(4,3),(4,3.5),(3.5,3.5),(2.8,4),
							(2.3,5.8),(2,5.8),(1.5,3),(0.2,2.7)], (23.3,6.3))
irkutsk = node('irkutsk', 'as',[(0,1.4),(1.3,0),(4.3,0.3),(4.8,1.4)],(26,3.2))
japan = node('japan', 'as', [(0.5,0),(1,0),(1,1.8),(0,2),(0,1.5),(0.5,1.5)], (32.5,5),'Text-align:right;')
kamchatka = node('kamchatka', 'as',[(0,1.3),(1.7,0),(4,0.2),(3.5,1.8),(3.2,1.3),(3.2,1),(0.8,1.3),(0.8,1.8),
									(1,1.8),(1.5,2.3),(1.5,3.3),(1,3.3),(1,2.8),(0.5,2.3)],(30.3,2.2), 'Text-align:top;')
middle_east = node('middle_east', 'as', [(0,0.5),(1,0),(1.8,0.3),(2.3,0.5),(2.6,1),(3.3,0.8),(4.3,1.2),
										(4.5,3),(3,2.5),(2.9,2.3),(2.7,2.3),(2.7,2.6),(3.3,3.5),(3.8,3.5),
										(4.3,4),(2.2,5.3),(1.2,2.7),(1,2.5),(1,1),(0.2,1)], (19,6))
mongolia = node('mongolia', 'as', [(0,0),(5,0),(5.5,0.5),(5.5,2),(6,2.5),(5.8,2.6),(5,2),(4,1.8),(3.7,1.5),(2.5,2)], (25.8,4.6))
siam = node('siam', 'as', [(0,0),(1.5,0.9),(2,0.9), (2,1.5), (2.5,2), (2.5,3),(2,3.5), (1,2.5), (1,3.5),
							(1.5,4.5),(1.3,4.3),(0.8,3.5),(0.8,2.3),(0,1.5)], (27.3,8.2))
siberia = node('siberia', 'as', [(0,0.5),(2,0),(3,0.3),(3.5,1.5),(2.2,2.8),(1.5,2.8),(1.5,2.5)],(23.8,1.8))
ural = node('ural', 'as', [(0,0.2),(1.5,0),(3,2),(3,2.7),(1,1.7),(0,1.7)],(22.3,2.3))
yakutsk = node('yakutsk', 'as',[(0,0),(5.2,0.2),(3.5,1.5),(0.5,1.2)],(26.8,2))

# Africa
congo = node('congo', 'af',[(0,1.5),(0.5,1.5),(1.5,0),(2.5,1.5),(3,1.5),(2,3),(1,3),(1,2.5),(0,2.5)],(16.5,11.5))
east_af = node('east_af', 'af',[(0,0.3),(0,1.8),(1,3.3),(1.5,3.3),(0.5,4.8),(2,4.8),(2,3.8),(3,2.8),(4,1.8),
								(3,1.8),(2.3,0),(0.5,0),(0.5,0.3)],(18,9.7))
egypt = node('egypt', 'af',[(0,0),(1.5,0.5),(1.5,0),(3.5,0.5),(3.7,0.7),(3.5,1),(3.8,1.8),(2,1.8),(2,2),(1.5,2),(0,1)],(16.5,8))
madagascar = node('madagascar', 'af',[(0.6,0),(0.8,0.2),(0.6,1.6),(0,1.6),(0.1,0.5)],(21,14.7))
north_af = node('north_af', 'af',[(4,0),(4,2),(5.5,3),(5.5,4.5),(4.5,6),(4,6),(4,5.5),(3.5,5),(1.5,5.2),(0,3.5),(0,2.5),(1.5,0.3)],(12.5,7))
south_af = node('south_af', 'af',[(0,0),(1,4),(2,4),(3.5,1),(3.5,0.5),(1,0.5),(1,0)],(16.5,14))

# AUS
eastern_aus = node('eastern_aus', 'aus',[(0,1),(1,0.2),(1,1),(2,1.3),(2,0),(3,2.5),(2,5),(1,5),(1,3),(0,3)] ,(33, 15.5))
indonesia = node('indonesia', 'aus',[(0,0.8),(1.3,0),(1.5,0.3),(1,1.5),(0,1.5)],(30, 12.5))
new_guinea = node('new_guinea', 'aus', [(0,0),(2,0.8),(2.5,1.3),(1.8,1),(1.5,1.3),(0,0.3)], (33, 13.5))
western_aus = node('western_aus', 'aus', [(0,1.7),(1.8,0) ,(2,0.2),(2,2.2),(3,2.2),(3,4.2),(2.3,3.2),(0,3.7)], (31, 16.3))

graph = {alaska:[alberta, nw_territory, kamchatka],
		alberta:[alaska, nw_territory, ontario, western_us],
		central_america:[eastern_us, western_us, venezuela],
		eastern_us:[central_america, western_us, ontario, quebec],
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
		northern_eu:[great_britain, scandinavia, southern_eu, ukraine, western_eu],
		scandinavia:[great_britain, iceland, northern_eu, ukraine],
		southern_eu:[northern_eu, ukraine, middle_east, north_af, egypt, western_eu],
		ukraine:[northern_eu, scandinavia, southern_eu, middle_east, afghanistan, ural],
		western_eu:[great_britain, northern_eu, southern_eu, north_af],
		congo:[east_af, south_af, north_af],
		east_af:[congo, egypt, madagascar, south_af, middle_east, north_af],
		egypt:[east_af, north_af, southern_eu, middle_east],
		madagascar:[east_af,south_af],
		north_af:[congo, east_af, egypt, western_eu, southern_eu, brazil],
		south_af:[congo, east_af, madagascar],
		afghanistan:[china, india, middle_east, ural, ukraine],
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
		yakutsk:[irkutsk, kamchatka, siberia, mongolia],
		eastern_aus:[new_guinea, western_aus],
		indonesia:[new_guinea, western_aus, siam],
		new_guinea:[eastern_aus, indonesia, western_aus],
		western_aus:[eastern_aus, indonesia, new_guinea]}


#Colors 

RED = '#FF0000'
YELLOW = '#FFFF00'
GREEN = '#00FF00'
BLUE = '#00F9FD'
PURPLE = '#FA02D4'
WHITE = '#FFFFFF'

#Players

class Player:
	def __init__(self, name, color, units = 0, states = {}, alive = True, mission = None):
		self.name = name
		self. color = color
		self.units = units
		self.states = states
		self.alive = alive
		self.mission = mission
		if self.states == {}:
			self.states['na'] = []
			self.states['sa'] = []
			self.states['eu'] = []
			self.states['as'] = []
			self.states['aus'] = []
			self.states['af'] = []


red = Player('red', RED)
blue = Player('blue', BLUE)
yellow = Player('yellow', YELLOW)
green = Player('green', GREEN)
purple = Player('purple', PURPLE)
white = Player('white',WHITE)

red_states_dic = {}
blue_states_dic = {}
yellow_states_dic = {}
green_states_dic = {}
purple_states_dic = {}
white_states_dic = {}

dict_list = [red_states_dic, blue_states_dic, yellow_states_dic, green_states_dic, purple_states_dic, white_states_dic]

for dic in dict_list:
	dic['na'] = []
	dic['sa'] = []
	dic['eu'] = []
	dic['as'] = []
	dic['af'] = []
	dic['aus'] = []

# Win Missions:
class Mission:
	def __init__(self,player = None, continents = [], number_of_states = 0, eliminate_player= None, units_in_states = None,
	third_continent = False, explanation = ''):
		self.player = player
		self.continents = continents
		self.number_of_states = number_of_states
		self.eliminate_player = eliminate_player
		self.units_in_states = units_in_states
		self.missioncomplete = False
		self.third_continent = third_continent
		self.explanation = explanation


	def update_mission(self):
		if self.player == self.eliminate_player and self.player != None:
			self.eliminate_player == None
			self.number_of_states = 24
			self.explanation = 'Conquer 24 States'


	def check_continents(self):
		if self.continents == []:
			return True
		number_of_states_per_continent = -1
		for continent in self.continents:

			if continent == 'na':
				number_of_states_per_continent = 9
			elif continent == 'sa':
				number_of_states_per_continent = 4
			elif continent == 'eu':
				number_of_states_per_continent = 7
			elif continent == 'af':
				number_of_states_per_continent = 6
			elif continent == 'as':
				number_of_states_per_continent = 12
			elif continent == 'aus':
				number_of_states_per_continent = 4

			if len(self.player.states[continent]) != number_of_states_per_continent:
				return False

		return True

	def check_number_of_states(self):
		if self.number_of_states == 0:
			return True
		state_counter = 0
		for continent in self.player.states.keys():
			if self.player.states[continent] == []:
				pass
			for state in self.player.states[continent]:
				state_counter += 1
				if state_counter == self.number_of_states:
					return True

	def check_eliminate_player(self):
		if self.eliminate_player == None:
			return True
		return not self.eliminate_player.alive

	def check_units_in_states(self):
		if self.units_in_states == None:
			return True
		for continent in self.player.states.keys():
			if self.player.states[continent] == []:
				pass
			for state in self.player.states[continent]:
				if state.units < self.units_in_states:
					return False

		return True

	def check_third_continent(self):
		if not self.third_continent:
			return True
		continent_counter = 0
		for continent in self.player.states.keys():
			continent_length = len(self.player.states[continent])
			if continent == 'na' and continent_length == 9:
				continent_counter += 1
			elif continent == 'sa' and continent_length == 4:
				continent_counter += 1
			elif continent == 'eu' and continent_length == 7:
				continent_counter += 1
			elif continent == 'af' and continent_length == 6:
				continent_counter += 1
			elif continent == 'as' and continent_length == 12:
				continent_counter += 1
			elif continent == 'aus' and continent_length == 4:
				continent_counter += 1
			if counter == 3:
				return True




	def check_mission_complete(self):
		result = self.check_continents()and self.check_third_continent() and self.check_eliminate_player()
		self.missioncomplete = result and self.check_units_in_states() and self.check_number_of_states()




mission1 =  Mission(continents = ['na', 'af'], explanation = 'Conquer North America and Africa')
mission2 = Mission(continents = ['as', 'af'], explanation = 'Conquer Asia and Africa')
mission3 = Mission(continents = ['as', 'sa'], explanation = 'Conquer Asia and South America')
mission4 = Mission(eliminate_player = red, explanation = 'Eliminate Player red')
mission5 = Mission(eliminate_player = blue, explanation = 'Eliminate Player blue')
mission6 = Mission(eliminate_player = yellow, explanation = 'Eliminate Player yellow')
mission7 = Mission(eliminate_player = green, explanation = 'Eliminate Player green')
mission8 = Mission(eliminate_player = purple, explanation = 'Eliminate Player purple')
mission9 = Mission(eliminate_player = white, explanation = 'Eliminate Player white')
mission10 = Mission(number_of_states = 18, units_in_states = 2, explanation = 'Conquer 18 States with atleast 2 armies in each State')
mission11 = Mission(continents = ['na', 'aus'], explanation = 'Conquer North America and Australia')
mission12 = Mission(number_of_states = 24, explanation = 'Conquer 24 States')
mission13 = Mission(continents = ['eu', 'sa'], third_continent = True,
 					explanation = 'Conquer Europe, South America and a third Continent of your Choice')
mission14 = Mission(continents = ['eu', 'aus'], third_continent = True, 
					explanation = 'Conquer Europe, Australia and a third Continent of your Choice')

missions = []

def available_missions(number_of_players):

	missions = [mission1, mission2, mission3, mission4, mission5, mission7, mission10, mission11, mission12, mission13, mission14]
	if number_of_players > 3:
		missions.append(mission6)
	if number_of_players > 4:	
		missions.append(mission8)
	if number_of_players > 5:
		missions.append(mission9)

	return missions