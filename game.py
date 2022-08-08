# REDO OF THE GAME SNAKE
# ---original version in LearnCodingInPython under L3
# ---purpose is to make the structure more intuitive and to actually 
#    complete the game

import curses
from curses import textpad
import random

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
  f = False #signal no fruits on the board
  fy, fx = 0, 0 #fruit coordinates
  points = 0 #set points to 0

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

    # REFRESH POINTS
    snakeGame.addstr(box[0][0]-1, box[0][1], chr(10023) + " = " + str(points))
    
    # SNAKE MOVEMENT
    key = snakeGame.getch()
    og = snake[0]
    new = snake[0] #? all I know is it works weirdly without

    #direction of movement
    if key == curses.KEY_UP and direction != curses.KEY_DOWN or key == curses.KEY_RIGHT and direction != curses.KEY_LEFT or key == curses.KEY_DOWN and direction != curses.KEY_UP or key == curses.KEY_LEFT and direction != curses.KEY_RIGHT:
      direction = key
    #add head in direction you go
    if direction == curses.KEY_UP:
      new = [og[0]-1, og[1]]
    elif direction == curses.KEY_RIGHT:
      new = [og[0], og[1]+1]
    elif direction == curses.KEY_DOWN:
      new = [og[0]+1, og[1]]
    elif direction == curses.KEY_LEFT:
      new = [og[0], og[1]-1]
    #get your head in the game!
    snakeGame.addstr(new[0], new[1], body)
    snake.insert(0, new)

    # IF SNAKE GETS FRUIT
    if snake[0][0] == fy and snake[0][1] == fx:
      points += 1
      f = False
    else:
      #bye bye tail 
      #moved here so the tail is ensured to be in the right spot
      snakeGame.addstr(snake[-1][0], snake[-1][1], " ")
      snake.pop() #remove the empty elements at the end?
    #no fruit on the board? add one
    if f == False:
      fy, fx = fruits(box, snake)
      snakeGame.addstr(fy, fx, chr(10023))
      f = True
    
    # CHECK IF SNAKE DEAD
    if snake[0][0] == box[0][0] or snake[0][0] == box[1][0] or snake[0][1] == box[0][1] or snake[0][1] == box[1][1]:
      return box
    
def bounds(snakeGame):
  box = [ #y, x
    [5, 10], #top left
    [20, 55] #bottom right
  ]
  textpad.rectangle(snakeGame, box[0][0], box[0][1], box[1][0], box[1][1])
  return box

def fruits(box, snake):
  count = 0 
  while count < len(snake):
    count = 0 #reset because it doesn't work
    for sc in snake:
      y = random.randrange(box[0][0]+1, box[1][0])
      x = random.randrange(box[0][1]+1, box[1][1])
      if y == sc[0] or x == sc[1]:
          break
      else:
          count += 1
  return y, x
  

def menu(snakeGame, box):
  snakeGame.addstr("You died!")
  
# run the game
def game(snakeGame): 
  curses.curs_set(0) #hide the cursor
  snakeGame.nodelay(1) #animate?
  snakeGame.timeout(100) #timeout is at 0.1 seconds

  intro(snakeGame)
  x = snakeGame.getch()
  while x != ord('q'):
    if x == ord('1') or x == ord('2'):
      menu(snakeGame, board(snakeGame))
    x = snakeGame.getch()
  end(snakeGame)

curses.wrapper(game)
