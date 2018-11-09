board = [['*','*','*'],['*','*','*'],['*','*','*']]

def printBoard(board):
   print('\n')
   for i in range(0,3):
      print("%c%c%c" % (board[i][0],board[i][1],board[i][2]))
   print('\n')

square=''
while(square!='stop'):
	square=input("Which square?\n")
	if square=='UL':
		board[0][0]='x'
	elif square=='UC':
		board[0][1]='x'
	elif square=='UR':
		board[0][2]='x'
	elif square=='CL':
		board[1][0]='x'
	elif square=='C':
		board[1][1]='x'
	elif square=='CR':
		board[1][2]='x'
	elif square=='LL':
		board[2][0]='x'
	elif square=='LC':
		board[2][1]='x'
	elif square=='LR':
		board[2][2]='x'
	printBoard(board)
print("Thanks for playing!")
