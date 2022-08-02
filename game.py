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
  box = bounds(snakeGame) #make game boundaries

  # set up starting snake
  body = chr(9646)
  snake = [
    [int((box[1][0]-box[0][0])/2+box[0][0]), int((box[1][1]-box[0][1])/2+box[0][1])],
    [int((box[1][0]-box[0][0])/2+box[0][0]), int((box[1][1]-box[0][1])/2+box[0][1])-1],
    [int((box[1][0]-box[0][0])/2+box[0][0]), int((box[1][1]-box[0][1])/2+box[0][1])-2]
  ]
  for point in snake:
    snakeGame.addstr(point[0], point[1], body)
  direction = curses.KEY_RIGHT

  while True: 

    # SNAKE MOVEMENT
    key = snakeGame.getch()
    head = snake[0]
    new_head = snake[0] #necessary because… ?
    #direction of movement
    if key == curses.KEY_UP and direction != curses.KEY_DOWN or key == curses.KEY_RIGHT and direction != curses.KEY_LEFT or key == curses.KEY_DOWN and direction != curses.KEY_UP or key == curses.KEY_LEFT and direction != curses.KEY_RIGHT:
      direction = key
    #get it actually going there
    if direction == curses.KEY_UP:
      new_head = [head[0]-1, head[1]]
    elif direction == curses.KEY_RIGHT:
      new_head = [head[0], head[1]+1]
    elif direction == curses.KEY_DOWN:
      new_head = [head[0]+1, head[1]]
    elif direction == curses.KEY_LEFT:
      new_head = [head[0], head[1]-1]
    #get your head in the game!
    snakeGame.addstr(new_head[0], new_head[1], body)
    snake.insert(0, new_head)
    #bye bye tail
    snakeGame.addstr(snake[-1][0], snake[-1][1], " ")
    snake.pop() #remove the empty elements at the end?

    # CHECK IF SNAKE DEAD
    if snake[0][0] == box[0][0] or snake[0][0] == box[1][0] or snake[0][1] == box[0][1] or snake[0][1] == box[1][1]:
      break
    
def bounds(snakeGame):
  box = [ #y, x
    [5, 10], #top left
    [30, 55] #bottom right
  ]
  textpad.rectangle(snakeGame, box[0][0], box[0][1], box[1][0], box[1][1])
  return box

def menu(snakeGame):
  snakeGame.addstr(0, 0, "hello")
  snakeGame.getch()
  
  
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
      menu(snakeGame)
    x = snakeGame.getch()
  end(snakeGame)

curses.wrapper(game)