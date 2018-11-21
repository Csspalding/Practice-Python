#battleshipGamePython tutorial from Code Academy with additional notes
#game logic code adapted and extended 11hby Csspalding
#python 3 is being used and differs from python 2, in input() in p3 is raw_imput in p2, print is a function in p3 so needs paraethases ()  but does not in p2 
from random import randint

board = []
#create a grid 5 by 5 using the captial letter "O"
for x in range(0, 5):# makes the grid loop 5 times for 5 rows
  board.append(["O"] * 5)# prints 5 "O"'s in a line for 5 columns

#prints the grid with no "" marks around the O's
def print_board(board):
  for row in board:
    print(" " .join(row))
# print "~".join(row) would give ~ between the O's  O~O~O~O~O


# call the print_board function to print out the grid
print_board(board)


#functions to selects a row then a col using randint as imported above 
# to select a space on the grid to hide a ship
def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

# hidden_ship = [ship_row] [ship_col]
ship_row = random_row(board)
ship_col = random_col(board)
#the following commands reveal the hidden ship but have been commented out
#print ship_row
#print ship_col

#loop to run the programme 14 times for a user, counting each turn
for turn in range(15):
  print ("Turn", turn + 1)
  #raw_input allows user to input a string, concatinated to a int so
  # a user can guess a number, -1 for the users the row/col count 1-5 into computer count 0-4
  guess_row = int(input("Guess Row: ")) -1
  guess_col = int(input("Guess Col: ")) -1

    #in the loop several actions
  if guess_row == ship_row and guess_col == ship_col:
    print ("Congratulations! You sank my battleship!") 
    break
  else:
    if guess_row not in range(5) or \
      guess_col not in range(5):
      print ("Oops, that's not even in the ocean.")
    elif board[guess_row][guess_col] == "X":
      print("You guessed that one already." )
    else:
      if (turn == 14):
        print ("Game Over")
      else:
         print ("You missed my battleship!")
      board[guess_row][guess_col] = "X"
    print_board(board)