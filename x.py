import time
import curses

stdscr = curses.initscr()

stdscr.addstr(20,20, "Hello")
stdscr.refresh()

time.sleep(1)

stdscr.addstr(20,20, "World! (curses)")
stdscr.refresh()
