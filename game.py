# REDO OF THE GAME SNAKE
# ---original version in LearnCodingInPython under L3
# ---purpose is to make the structure more intuitive and to actually 
#    complete the game

'''
TO DO
- find a way to change speeds (this will help for 
  minesweeper too
- make it so when you die you press r to replay or m to 
  go back to the menu
- screen size warning
- make an easy difficulty (easier to test that way)
'''

import curses
import random

# change curses.textpad.rectangle so I can add colour
def rectangle(win, uly, ulx, lry, lrx, col):
  #manually creating vline and hline since I can't add colour for
  #those functions either
  for x in range(uly+1, lry): #vline
    win.addch(x, ulx, curses.ACS_VLINE, col)
    win.addch(x, lrx, curses.ACS_VLINE, col)
  for x in range(ulx+1, lrx): #hline 
    win.addch(uly, x, curses.ACS_HLINE, col)
    win.addch(lry, x, curses.ACS_HLINE, col)              
  #corners
  win.addch(uly, ulx, curses.ACS_ULCORNER, col)                         
  win.addch(uly, lrx, curses.ACS_URCORNER, col)                         
  win.addch(lry, lrx, curses.ACS_LRCORNER, col)                 
  win.addch(lry, ulx, curses.ACS_LLCORNER, col)
  
# literally just taken from my Minesweeper but
def colours():
    #curses setup for colours
    curses.start_color()
    curses.use_default_colors()

    for i in range(0, curses.COLORS):
      #initialize color pair
      if i == 15:
        curses.init_pair(i + 1, i, 1)
      elif i == 16:
        curses.init_pair(i + 1, i, 196)
      else:
        curses.init_pair(i + 1, i, -1)
    #return colors in a dictionary type
    return{
      "fruit": curses.color_pair(227),
      "border": curses.color_pair(6),
      "snake": curses.color_pair(34),
      "dead": curses.color_pair(2)
    }

def intro(snakeGame):
  # check if the screen size is big enough
  if (curses.COLS < 65 or curses.LINES < 26):
    x = [
      "hey",
      "your screen size is currently (x, y) (" + str(curses.COLS) + ", " + str(curses.LINES) +")",
      "it should be at least (x, y) (65, 26)",
      "Sorry for the inconvenience, ",
      "but please adjust the screen size."
    ]
    for r in x: # what does this do?
      for s in range(len(r)):
        snakeGame.addstr(x.index(r), s, x[x.index(r)][s])
        snakeGame.getch()
    curses.endwin()
    #FIND WAY TO KICK FROM THIS POINT
  else:
    # cool typing effect / show one at a time
    snakeGame.clear()
    x = "Hello! Welcome to SNAKE"
    for r in range(1, len(x)+1):
      snakeGame.addstr(1, r, x[r-1])
      snakeGame.getch()
    x = [
      "Please select your game mode",
      "'select this' 'name of type' (x, y, speed)",
      "",
      "",
      "",
      "",
      "",
      "your screen size is currently (maxX, maxY)",
      "(" + str(curses.COLS) + ", " + str(curses.LINES) +")",
      "the size must stay at least (x, y)",
      "(65, 26)", 
      "",
      "press 'q' or 'esc' while not in-game to quit"
      #AND THEN MAKE IT SO YOU WILL GET KICKED IN THE BEGINNING IF YOUR
      #SCREEN IS NOT AT LEAST THAT SIZE
    ]
    for r in range(len(x)):
      snakeGame.addstr(2+r, 1, x[r])
      snakeGame.getch()

    # actual options
    x = [
      "1 standard (45, 15, standard speed)",
      "2 easy (30, 10, slow speed)",
      "3 adaptable (maxX-20, maxY-10, standard speed)",
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

# game,
def board(snakeGame, mode): 
  snakeGame.erase()
  col = colours() #set up colours?
  box = bounds(snakeGame, mode) #make game boundaries
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
    snakeGame.addstr(point[0], point[1], body, col["snake"])
  direction = curses.KEY_RIGHT

  while True: 

    # REFRESH POINTS
    snakeGame.addstr(box[0][0]-1, box[0][1], chr(10023) + " = " + str(points), col["snake"])
    snakeGame.addstr(box[0][0]-1, box[0][1], chr(10023), col["fruit"])
    
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
    snakeGame.addstr(new[0], new[1], body, col["snake"])
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
      snakeGame.addstr(fy, fx, chr(10023), col["fruit"])
      f = True
    
    # CHECK IF SNAKE DEAD
    if snake[0][0] == box[0][0] or snake[0][0] == box[1][0] or snake[0][1] == box[0][1] or snake[0][1] == box[1][1]:
      return box

    #ADD A WAY TO WIN GAME
    
def bounds(snakeGame, mode):
  col = colours()
  box = [ #y, x
    [5, 10], #top left
    [20, 55] #bottom right
  ]
  if mode == '2':
      box[1][0] = 15
      box[1][1] = 40
  elif mode == '3':
      box[1][0] = curses.LINES-5
      box[1][1] = curses.COLS-10
  rectangle(snakeGame, box[0][0], box[0][1], box[1][0], box[1][1], col["border"])
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
  

''' add actual info here '''
def menu(snakeGame, box):
  col = colours()
  frame = [
    [int((box[1][0]-box[0][0])/2+box[0][0])-4, int((box[1][1]-box[0][1])/2+box[0][1])-15],
    [int((box[1][0]-box[0][0])/2+box[0][0])+6, int((box[1][1]-box[0][1])/2+box[0][1])+15],
  ]
  rectangle(snakeGame, frame[0][0], frame[0][1], frame[1][0], frame[1][1], col["dead"])
  snakeGame.addstr("You died!")
  
# run the game
def game(snakeGame): 
  curses.curs_set(0) #hide the cursor
  snakeGame.nodelay(1) #animate?
  snakeGame.timeout(100) #timeout is at 0.1 seconds

  intro(snakeGame)
  x = snakeGame.getch()
  while x != ord('q') and x != 27:
    if x == ord('1') or x == ord('2') or x == ord('3'):
      menu(snakeGame, board(snakeGame, chr(x)))
    x = snakeGame.getch()
  end(snakeGame)

curses.wrapper(game)
