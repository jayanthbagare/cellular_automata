import random
import time
from pyray import *

width = 600
height = 600
grid = [0] * 10
tmpGrid = [0] * 10

def setup_grid():
	global grid
	for i in range(10):
		ran = random.random()
		if(ran > 0.5):
			grid[i] = 1
		else:
			grid[i] = 0

def update_grid():
	global grid
	global tmpGrid
	for i in range(10):
		if(i-1 != -1 and i+1 != 10):
			bitString = str(grid[i-1])+str(grid[i])+str(grid[i+1])
			match bitString:
				case '000':
					tmpGrid[i] = 0
				case '001':
					tmpGrid[i] = 1
				case '010':
					tmpGrid[i] = 1
				case '100':
					tmpGrid[i] = 1
				case '110':
					tmpGrid[i] = 0
				case '011':
					tmpGrid[i] = 1
				case '101':
					tmpGrid[i] = 0
				case '111':
					tmpGrid[i] = 0
	grid = tmpGrid

def draw_cells():
	for i in range(10):
		if(grid[i] == 1):
			draw_rectangle(i*60,0,60,60,(255,255,255,255))
		else:
			draw_rectangle_lines(i*60,0,60,60,(255,255,255,255))

init_window(width,height,"Cellular Automata in 1D")
setup_grid()

while not window_should_close():
	time.sleep(0.5)
	update_grid()
	begin_drawing()
	clear_background((66, 75, 84))
	draw_cells()
	end_drawing()
close_window()

