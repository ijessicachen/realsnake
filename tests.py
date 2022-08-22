import curses

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
    stdscr.addstr(1, 0, "border", curses.color_pair(18))
    stdscr.addstr(2, 0, "fruit", curses.color_pair(227))

    x = stdscr.getch()

    #TEXTPAD RECTANGLE CHARACTERS
    stdscr.addch(4, 1, curses.ACS_HLINE, curses.color_pair(18))
    stdscr.addch(4, 0, curses.ACS_ULCORNER, curses.color_pair(18))
    stdscr.addch(5, 0, curses.ACS_VLINE, curses.color_pair(18))
    stdscr.addch(6, 0, curses.ACS_LLCORNER, curses.color_pair(18))
    stdscr.addch(6, 1, curses.ACS_HLINE, curses.color_pair(18))
    stdscr.addch(6, 2, curses.ACS_LRCORNER, curses.color_pair(18))
    stdscr.addch(5, 2, curses.ACS_VLINE, curses.color_pair(18))
    stdscr.addch(4, 2, curses.ACS_URCORNER, curses.color_pair(18))
    #why the rectangle sadly can't be more efficient, part one
    stdscr.addch(5, 5, curses.ACS_HLINE, curses.color_pair(18))
    stdscr.addch(5, 4, curses.ACS_VLINE, curses.color_pair(18))
    stdscr.addch(6, 5, curses.ACS_HLINE, curses.color_pair(18))
    stdscr.addch(5, 6, curses.ACS_VLINE, curses.color_pair(18))
    #part two
    stdscr.addch(4, 8, curses.ACS_HLINE, curses.color_pair(18))
    stdscr.addch(5, 7, curses.ACS_VLINE, curses.color_pair(18))
    stdscr.addch(5, 8, curses.ACS_HLINE, curses.color_pair(18))
    stdscr.addch(5, 9, curses.ACS_VLINE, curses.color_pair(18))

curses.wrapper(main)

