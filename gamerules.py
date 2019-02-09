import numpy
import PyQt5
import sys
from PyQt5.QtWidgets import *#QMainWindow, QApplication, QWidget, QGraphicsEllipseItem
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import copy
import definitions

players = []

colors = [definitions.blue, definitions.green, definitions.red, definitions.yellow, definitions.purple, definitions.white]


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
	return int(result)




def start_armys(player):
	return int(numpy.ceil(2*len(nodes)/player))





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