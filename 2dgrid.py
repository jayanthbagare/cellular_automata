import random
import time
from pyray import *

width = 800
height = 600
rows,cols = 200,200
cnt = 0
incsize = int(width/rows)

grid = [[0]*cols]*rows
tmpgrid = [[0]*cols]*rows


bgcolor = (0,0,0,255)
fgcolor = (0,0,0,255)
cellColor = (255,255,255,255)

def setup_grid():
	global grid,tmpgrid
	grid = [[0 for i in range(cols)] for j in range(rows)]
	tmpgrid = [[0 for i in range(cols)] for j in range(rows)]
	grid[60][1] = 1
	# grid[3][3] = 1
	# grid[3][4] = 1
	# grid[2][3] = 1		

def update_grid():
	global grid,tmpgrid,cols,rows
	for i in range(cols):
		for j in range(rows):
			if(i!=0 and i!=cols-1 and j!=0 and j!=rows-1):
				bitString = str(grid[i-1][j])+str(grid[i][j])+str(grid[i+1][j])
				match bitString:
					case '000':
						tmpgrid[i][j+1] = 0
					case '010':
						tmpgrid[i][j+1] = 0
					case '101':
						tmpgrid[i][j+1] = 0
					case '111':
						tmpgrid[i][j+1] = 0
					case '001':
						tmpgrid[i][j+1] = 1
					case '100':
						tmpgrid[i][j+1] = 1
					case '110':
						tmpgrid[i][j+1] = 1
					case '011':
						tmpgrid[i][j+1] = 1
	localGrid = grid				
	grid = tmpgrid
	tmpgrid = localGrid

def draw_cells():
	global grid,rows,cols,fgcolor,cellColor,incsize

	for i in range(cols):
		for j in range(rows):
			if(grid[i][j] == 1):
				draw_rectangle(i*incsize,(j)*incsize,incsize,incsize,cellColor)
				draw_rectangle_lines(i*incsize,(j)*incsize,incsize,incsize,fgcolor)
			else:
				draw_rectangle_lines(i*incsize,(j)*incsize,incsize,incsize,fgcolor)

init_window(width,height,"2D Cellular Automata")
setup_grid()

while not window_should_close():
	time.sleep(0.1)
	begin_drawing()
	clear_background(bgcolor)
	update_grid()		
	draw_cells()
	end_drawing()