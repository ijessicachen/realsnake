import curses


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

def rect (stdscr):
    #TEXTPAD RECTANGLE CHARACTERS
    stdscr.addch(4, 1, curses.ACS_HLINE, curses.color_pair(6))
    stdscr.addch(4, 0, curses.ACS_ULCORNER, curses.color_pair(6))
    stdscr.addch(5, 0, curses.ACS_VLINE, curses.color_pair(6))
    stdscr.addch(6, 0, curses.ACS_LLCORNER, curses.color_pair(6))
    stdscr.addch(6, 1, curses.ACS_HLINE, curses.color_pair(6))
    stdscr.addch(6, 2, curses.ACS_LRCORNER, curses.color_pair(6))
    stdscr.addch(5, 2, curses.ACS_VLINE, curses.color_pair(6))
    stdscr.addch(4, 2, curses.ACS_URCORNER, curses.color_pair(6))
    #why the rectangle sadly can't be more efficient, part one
    stdscr.addch(5, 5, curses.ACS_HLINE, curses.color_pair(6))
    stdscr.addch(5, 4, curses.ACS_VLINE, curses.color_pair(6))
    stdscr.addch(6, 5, curses.ACS_HLINE, curses.color_pair(6))
    stdscr.addch(5, 6, curses.ACS_VLINE, curses.color_pair(6))
    #part two
    stdscr.addch(4, 8, curses.ACS_HLINE, curses.color_pair(6))
    stdscr.addch(5, 7, curses.ACS_VLINE, curses.color_pair(6))
    stdscr.addch(5, 8, curses.ACS_HLINE, curses.color_pair(6))
    stdscr.addch(5, 9, curses.ACS_VLINE, curses.color_pair(6))

#menu for when gameplay ends - win or die
def endmenu (stdscr):

    #red rectangle
    #normal
    stdscr.addstr(11, 10, "You died!")
    stdscr.addstr(12, 5, "r - replay this level")
    stdscr.addstr(13, 5, "m - go to menu")
    stdscr.addstr(14, 5, "q, esc - quit")

    #gold (I mean fruit-coloured) rectangle
    #win
    


def main(stdscr):
  stdscr.nodelay(1) #animate?
  stdscr.timeout(100) #timeout is at 0.1 seconds
  x = ord('a')
  
  while x != ord('q'):
    #COLOURS
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
    
    stdscr.addstr(0, 0, "snake", curses.color_pair(21))
    stdscr.addstr(1, 0, "border", curses.color_pair(6))
    stdscr.addstr(2, 0, "fruit", curses.color_pair(227))
    
    rect(stdscr)

    endmenu(stdscr)

    x = stdscr.getch()


curses.wrapper(main)

