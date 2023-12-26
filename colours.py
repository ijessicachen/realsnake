# I need to revive my colours knowledge

# ISSUES
#    - for some reason there are issues
#      with 256 colours?

import curses

def main (stdscr):
    curses.start_color()
    curses.use_default_colors()
    
    stdscr.addstr(str(curses.COLORS))
    
    for i in range (0, curses.COLORS):
        curses.init_pair(i+1, i, -1)
    #try:
    #    for i in range (0, 255):
    #        stdscr.addstr(str(i), curses.color_pair(i))
    #except curses.ERR:
    #    # end of screen reached
    #    pass
    stdscr.getch()

curses.wrapper(main)

   #curses setup for colours
   # curses.start_color()
   # curses.use_default_colors()

   # for i in range(0, curses.COLORS):
   #   #initialize color pair
   #   if i == 15:
   #     curses.init_pair(i + 1, i, 1)
   #   elif i == 16:
   #     curses.init_pair(i + 1, i, 196)
   #   else:
   #     curses.init_pair(i + 1, i, -1)

