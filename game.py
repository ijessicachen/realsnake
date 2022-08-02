# REDO OF THE GAME SNAKE
# ---original version in LearnCodingInPython under L3
# ---purpose is to make the structure more intuitive and to actually 
#    complete the game

import curses
from curses import textpad

def intro(snakeGame):
  # cool typing effect / show one at a time
  x = "Hello! Welcome to SNAKE"
  for r in range(1, len(x)+1):
    snakeGame.addstr(1, r, x[r-1])
    snakeGame.getch()
  x = [
    "Please select your game mode",
    "'select this' 'name of type' (x, y, speed)"
   #"size of a block (show a char that fills block)"
  ]
  for r in range(len(x)):
    snakeGame.addstr(2+r, 1, x[r])
    snakeGame.getch()

  # actual options
  x = [
    "1 standard (240, 160, idk)",
    "2 adaptable (maxX, maxY, standard speed)"
  ]
  for r in range(len(x)):
    snakeGame.addstr(5+r, 3, x[r])
    snakeGame.getch()

#end message
def end(snakeGame):
  snakeGame.erase() #idk what's different between this and clear
  x = "thanks for playing SNAKE"
  for r in range(len(x)):
    snakeGame.addstr(0, r, x[r])
    snakeGame.getch()

def board(snakeGame): #NOT ACTUALLY SET TO DIFFERENT SIZES YET
  snakeGame.erase()
  box = bounds(snakeGame)
  while True: 
    #test drawing something
    snakeGame.addstr(0, 0, chr(1058))
    if snakeGame.getch() == ord('0'): #hold screen here for now
      break

def bounds(snakeGame):
  box = [
    [5, 10],
    [30, 55]
  ]
  textpad.rectangle(snakeGame, box[0][0], box[0][1], box[1][0], box[1][1])
  return box
  
# run the game
def game(snakeGame): 
  curses.curs_set(0) #hide the cursor
  snakeGame.nodelay(1) #animate?
  snakeGame.timeout(100) #timeout is at 0.1 seconds

  intro(snakeGame)
  x = snakeGame.getch()
  while x != ord('q'):
    if x == ord('1') or x == ord('2'):
      board(snakeGame)
    x = snakeGame.getch()
  end(snakeGame)

curses.wrapper(game)