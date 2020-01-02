import os

position = [" "," "," "," "," "," "," "," "," "," "]
print("{0:*^70}".format("TicTacToe"))
print("   |   |   ")
print("{0:^4}{1:^4}{2:^4}".format("1","2","3"))
print("   |   |   ")
print("-----------")
print("   |   |   ")
print("{0:^4}{1:^4}{2:^4}".format("4","5","6"))
print("   |   |   ")
print("-----------")
print("   |   |   ")
print("{0:^4}{1:^4}{2:^4}".format("7","8","9"))
print("   |   |   ")
print("{0:-^60}{1}".format("Instructions","\nChoose the position of your mark according to writen on the above box "))
#Taking input from player 1 and 2 like X or O
count = True
while True:
	user_input03 = input("Press enter to play---")
	player1 = input("-------Player1 Choose your sign from X And O------").upper().strip()
	if player1=="O":
		player2="X"
		print("player1 chooses 'O'\n and player2 chooses 'X'")
		break
	elif player1=="X":
		player2="O"
		print("player1 chooses 'X'\n and player2 chooses 'O'")
		break
	else:
		print("Invalid")
print("lets start the game")
flag = True
while flag:
	if count:
		player_1 = input("Choose your position between 1 to 9 player 1-----")
		if player_1 >="A" and player_1 <="z" or len(player_1) > 1:
			print("Invalid input!")
		else:
			player_1 = int(player_1)
			
			if player_1 not in range(1,10):
				print("invalid spot")
			elif position[player_1] == "X" or position[player_1] =="O":
				print("Position already taken")
			elif player_1 == 1:
				position[1] =  player1
				count = False
			elif player_1 == 2:
				position[2] = player1
				count = False
			elif player_1 == 3:
				position[3] = player1
				count = False
			elif player_1 == 4:
				position[4] = player1
				count = False
			elif player_1 == 5:
				position[5] = player1
				count = False
			elif player_1 == 6:
				position[6] = player1
				count = False
			elif player_1 == 7:
				position[7] = player1
				count = False
			elif player_1 == 8:
				position[8] = player1
				count = False
			elif player_1 == 9:
				position[9] = player1
				count = False
		
		print("   |   |   ")
		print("{0:^4}{1:^4}{2:^4}".format(position[1],position[2],position[3]))
		print("   |   |   ")
		print("-----------")
		print("   |   |   ")
		print("{0:^4}{1:^4}{2:^4}".format(position[4],position[5],position[6]))
		print("   |   |   ")
		print("-----------")
		print("   |   |   ")
		print("{0:^4}{1:^4}{2:^4}".format(position[7],position[8],position[9]))
		print("   |   |   ")
		if (position[1]=="O" and position[2]=="O" and position[3]=="O") or \
			(position[4]=="O" and position[5]=="O" and position[6]=="O") or  \
			(position[7]=="O" and position[8]=="O" and position[9]=="O") or \
			(position[1]=="O" and position[4]=="O" and position[7]=="O") or \
			(position[2]=="O" and position[5]=="O" and position[8]=="O") or\
			(position[3]=="O" and position[6]=="O" and position[9]=="O") or \
			(position[1]=="O" and position[5]=="O" and position[9]=="O") or\
			(position[3]=="O" and position[5]=="O" and position[7]=="O"):
				print("player1 wins")
				flag = False
		elif (position[1]=="X" and position[2]=="X" and position[3]=="X") or \
			(position[4]=="X" and position[5]=="X" and position[6]=="X") or\
			(position[7]=="X" and position[8]=="X" and position[9]=="X") or \
			(position[1]=="X" and position[4]=="X" and position[7]=="X") or \
			(position[2]=="X" and position[5]=="X" and position[8]=="X") or\
			(position[3]=="X" and position[6]=="X" and position[9]=="X") or \
			(position[1]=="X" and position[5]=="X" and position[9]=="X") or\
			(position[3]=="x" and position[5]=="X" and position[7]=="X"):
			print("player1 wins")
			break
		elif (position[1]!=" " and position[2]!=" " and position[3]!=" ") and \
			(position[4]!=" " and position[5]!=" " and position[6]!=" ") and\
			(position[7]!=" " and position[8]!=" " and position[9]!=" ") and \
			(position[1]!=" " and position[4]!=" " and position[7]!=" ") and \
			(position[2]!=" " and position[5]!=" " and position[8]!=" ") and\
			(position[3]!=" " and position[6]!=" " and position[9]!=" ") and \
			(position[1]!=" " and position[5]!=" " and position[9]!=" ") and\
			(position[3]!=" " and position[5]!=" " and position[7]!=" "):
			print("match draw")
			break
	elif not count:
		player_2 = int(input("Choose your position between 1 to 9 player 2-----"))
		if player_2 not in range(1,10):
			print("invalid spot")
		elif position[player_2] == "X" or position[player_2] =="O":
			print("Position already taken")
		elif player_2 ==1:
			position[1]=player2
			count = True
		elif player_2 == 2:
			position[2] = player2
			count = True
		elif player_2 == 3:
			position[3]= player2
			count = True
		elif player_2 == 4:
			position[4] = player2
			count = True
		elif player_2 == 5:
			position[5] = player2
			count = True
		elif player_2 == 6:
			position[6] = player2
			count = True
		elif player_2 == 7:
			position[7] = player2
			count = True
		elif player_2 == 8:
			position[8] =player2
			count = True
		elif player_2 == 9:
			position[9] = player2
			count = True
		else:
			print("invalid")
		print("   |   |   ")
		print("{0:^4}{1:^4}{2:^4}".format(position[1],position[2],position[3]))
		print("   |   |   ")
		print("-----------")
		print("   |   |   ")
		print("{0:^4}{1:^4}{2:^4}".format(position[4],position[5],position[6]))
		print("   |   |   ")
		print("-----------")
		print("   |   |   ")
		print("{0:^4}{1:^4}{2:^4}".format(position[7],position[8],position[9]))
		print("   |   |   ")

		if (position[1]=="X" and position[2]=="X" and position[3]=="X") or \
		(position[4]=="X" and position[5]=="X" and position[6]=="X") or\
		(position[7]=="X" and position[8]=="X" and position[9]=="X") or \
		(position[1]=="X" and position[4]=="X" and position[7]=="X") or \
		(position[2]=="X" and position[5]=="X" and position[8]=="X") or\
		(position[3]=="X" and position[6]=="X" and position[9]=="X") or \
		(position[1]=="X" and position[5]=="X" and position[9]=="X") or\
		(position[3]=="x" and position[5]=="X" and position[7]=="X"):
			print("player2 wins")
			flag = False
		if (position[1]=="O" and position[2]=="O" and position[3]=="O") or \
			(position[4]=="O" and position[5]=="O" and position[6]=="O") or  \
			(position[7]=="O" and position[8]=="O" and position[9]=="O") or \
			(position[1]=="O" and position[4]=="O" and position[7]=="O") or \
			(position[2]=="O" and position[5]=="O" and position[8]=="O") or\
			(position[3]=="O" and position[6]=="O" and position[9]=="O") or \
			(position[1]=="O" and position[5]=="O" and position[9]=="O") or\
			(position[3]=="O" and position[5]=="O" and position[7]=="O"):
				print("player2 wins")
				break