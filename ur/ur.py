import numpy as np 
import time

def roll():
	print("Rolling dice...")
	time.sleep(0.5)
	dice1 = np.random.randint(2)
	dice2 = np.random.randint(2)
	dice3 = np.random.randint(2)
	dice4 = np.random.randint(2)

	total = dice1 + dice2 + dice3 + dice4
	print(dice1,end="", flush=True)
	time.sleep(0.7)
	print(dice2,end="", flush=True)
	time.sleep(0.7)
	print(dice3,end="", flush=True)
	time.sleep(0.7)
	print(dice4)
	time.sleep(0.7)
	print("Rolled: ",total)

	return total

def update_board(board, pieces, home, player, move_type, position_to,position_from):
	if move_type == "n":
		board[player-1][position_to-1] = player
		pieces[player-1] = pieces[player-1]-1

	elif move_type == "m":
		if position_from > 4 and position_from < 13:
			board[0][position_from-1] = 0
			board[1][position_from-1] = 0
		else:
			board[player-1][position_from-1] = 0

		if position_to > 4 and position_to < 13:
			if board[0][position_to-1] != 0:
				if player == 1:
					pieces[1] = pieces[1] + 1
				else:
					pieces[0] = pieces[0] + 1
				print("Piece knocked off!")
			board[0][position_to-1] = player
			board[1][position_to-1] = player
		else:
			board[player-1][position_to-1] = player

	elif move_type == "h":
		if position_from > 4 and position_from < 13:
			board[0][position_from-1] = 0
			board[1][position_from-1] = 0
		else:
			board[player-1][position_from-1] = 0
		home[player-1] = home[player-1] + 1


	return board, pieces, home


def board_to_string(board):
	symbols = [" ","X","O"]
	board_string = []
	c = 0
	while c < len(board):
		board_string.append(symbols[int(board[c])])
		c = c + 1

	return board_string


def print_board(board, pieces):
	p1_board = board[0]
	p2_board = board[1]

	c = 0
	while c < pieces[0]:
		print("X",end="", flush=True)
		c = c + 1
	print("\n")

	p1 = board_to_string(p1_board)
	print("| "+p1[3]+" | "+p1[2]+" | "+p1[1]+" | "+p1[0]+" |       | "+p1[13]+" | "+p1[12]+" |")
	print("| "+p1[4]+" | "+p1[5]+" | "+p1[6]+" | "+p1[7]+" | "+p1[8]+" | "+p1[9]+" | "+p1[10]+" | "+p1[11]+" |")
	p2 = board_to_string(p2_board)
	print("| "+p2[3]+" | "+p2[2]+" | "+p2[1]+" | "+p2[0]+" |       | "+p2[13]+" | "+p2[12]+" |\n")
	
	c = 0
	while c < pieces[1]:
		print("O",end="", flush=True)
		c = c + 1
	print("\n")

pieces = [7,7]
home = [0,0]
board = np.zeros((2,14))
player = 1
print("Welcome to Ur!")
while True:
	print("Type r for rules or ENTER to contine")
	user_input = input()
	if user_input.lower() == "r" or "rules":
		print("Ur is the world's oldest known board game dating back to the mesopetamian region over 4500 years ago.")
		print("Each player is given seven pieces which move along the tiles as shown....")
		print("LAYOUT")
		print("| 4 | 3 | 2 | 1 |       | 14| 13|")
		print("| 5 | 6 | 7 | 8 | 9 | 10| 11| 12|")
		print("| 4 | 3 | 2 | 1 |       | 14| 13|\n")
		while True:
			print("Press ENTER to play")
			user_input = input()
			break




	
	
	break

while True:
	if home[0] == 7:
		print("Player 1 wins!")
		break
	elif home[1] == 7:
		print("Player 2 wins!")
		break
	else:
		print_board(board, pieces)
		while True:
			print("Press ENTER to contine")
			input()
			break
		
		print("Player",player)

		while True:
			print("Press ENTER to roll or q to quit")
			player_input = input()

			if player_input.lower() == ("q" or "quit"):
				break
			elif player_input.lower() == "":
				rolled = roll()
				break
		
		commands = []
		options = 0
		if rolled == 0:
			print("Zero rolled! No available moves.")
		else:
			if pieces[player-1] != 0 and board[player-1][rolled-1] == 0:
				commands.append([player,"n",rolled,0])
				options = options + 1
				print(str(options)+") Play new piece onto position",rolled)
			c = 0
			while c < 14:
				if board[player-1][c] == player and int(c+rolled) > 13:
					commands.append([player,"m",0,int(c+rolled)])
					options = options + 1
					print(str(options)+") Send piece",int(c+1),"home!")
				elif board[player-1][c] == player and board[player-1][int(c+rolled)] != player and int(c+rolled) != 8:
					commands.append([player,"m",int(c+1+rolled),int(c+1)])
					options = options + 1
					print(str(options)+") Move piece from",int(c+1),"to",int(c+1+rolled))
				c = c + 1

			if options != 0:
				user_input = int(input())-1
				print(commands[user_input])
				if len(commands[user_input]) == 3:
					board, pieces, home = update_board(board, pieces, home, commands[user_input][0], commands[user_input][1], commands[user_input][2])
				else:
					board, pieces, home = update_board(board, pieces, home, commands[user_input][0], commands[user_input][1], commands[user_input][2], commands[user_input][3])
			else:
				print("Sorry, no available moves!")



		if player == 1:
			player = 2
		else:
			player = 1
	