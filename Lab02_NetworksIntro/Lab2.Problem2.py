# LANGTON'S ANT
# turmites

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from numpy import linalg as la
import math
import pycxsimulator as pycx
from pylab import *


'''
The rules are simple. During each time step, 
- the ant checks the color of the cell is it on. 
    - If it is black, the ant turns to the right, changes the cell to white, and moves forward one space. 
    - If the cell is white, the ant turns left, changes the cell to black, and moves forward.
'''
# 
# %matplotlib qt
    

class langton:
    antmarker = {0:'^', 1:'>', 2:'v', 3:'<'}
    
    def __init__(self, size = 11, length = 100, play = False, pos = None):
        self.size = size
        self.length = length
        self.config = np.zeros([size, size])
        self.play = play
        
        if pos == None: 
            center = int(size)/2
            center = int(center)
            self.ant = [center, center,0]
        else: 
            self.ant = [pos[0], pos[1], 0]
        
        
    def run(self, play = False):
        self.play = play
        print("running Langton's Ant")
        
        if self.play == False:
            self.output()
        
    def next(self):
        #checks the current color
        color = self.config[self.ant[0],self.ant[1]]
        
        if color > 0:
            # black
            self.ant[2] = (self.ant[2] + 1) % 4
            #changes the cell to white
            self.config[self.ant[0],self.ant[1]] = 0
            # moves forward
            self.move()
        else :
            # black
            self.ant[2] = (self.ant[2] - 1) % 4
            #changes the cell to block
            self.config[self.ant[0],self.ant[1]] = 1
            # moves forward
            self.move()
        
    '''    
    def display(self):
        # do nothing
        return False
        fig, ax = plt.subplot()
        
        for x in range(self.length):
        
    def animate(x):
        '''
            
            
    
    def output(self):
        for x in range(self.length):
            self.next()
        
        # show the end result
        plt.imshow(self.config, cmap = cm.binary)
        plt.show()
        print("shown")
        
    def move(self):
        # take a look at the ant object
        # move it one space forward in accordance with its direction
        # what do I want to do about boundaries
        
        # if it is even move up or down
        # if it is odd move left or right
        # lets have it loop around (so basically modulus i think? )
        if self.ant[2]%2 == 0:
            self.ant[0] = ((1 - self.ant[2]) + self.ant[0])%self.size
        else:
            self.ant[1] = ((2 - self.ant[2]) + self.ant[1])%self.size
        # loop it back aro
    
    def mod_center(self, center_matrix):
        center = int(self.size)/2
        center = int(center)
        
        cell = [center - 1, center - 1]
        
        for row in range(3):
            for col in range(3):
                self.config[cell[0]+row][cell[1] + col] = center_matrix[row][col]
                print(center_matrix[row][col])
        
            
class langtonant:
    def __init__(self, size, time):
        ant1 = langton(size = size, length = time)
        ant1.run()
        
        
    
# Problem 1

# Problem 2
''' 
Problem 2B) How many possible initial states/configurations are there for an 11×11 grid of Langton’s Ant (assuming a single ant)? You can work this out by figuring out how many possible configurations of black and white cells there are, and how many possible ways there are to place and orient the ant. How plausible is it to characterize the phase space network for such a system?
'''

langton2 = langton()

# how many possible configurations of black and white cells?
cells = 11 * 11
grid_states = 2**cells
# although some might be considered functionally equivalent
print("Grid States: {}".format(grid_states))

# in each of those states, the ant can be in any position, therefore, 
# phase_space = cells**grid_states
# print("Phase Space: {}".format(phase_space))
# basically impossibly many

# Problem 2C
'''
Problem 2C) Next, expand your grid size (to at least 50×50) and set the center 3x3 cells to an arbitrary configuration of black and white cells (you can choose one or assign it randomly). Simulate Langton’s ant using these conditions with a longer duration of your choice. What happens to the ant dynamics as time goes on? (Note that if you choose a very large grid and/or long time, it may take a few minutes to run this simulation.)
'''

langton2c = langton(size = 50, length = 20)
# arbitrary configuration of black and white cells

center_matrix = [
    [0,1,1],
    [1,0,0],
    [0,1,0]
    ]
langton2c.mod_center(center_matrix)

langton2c.run()


        
        
'''
# first iteration of langton's ant
n = 20 # grid size
# direction (0N, 1E, 2S, 3W)
ant = [5,5,0] # the initial position in the front
i = 500

config = np.zeros([n, n])

def move():
    # take a look at the ant object
    # move it one space forward in accordance with its direction
    # what do I want to do about boundaries
    
    # if it is even move up or down
    # if it is odd move left or right
    # lets have it loop around (so basically modulus i think? )
    if ant[2]%2 == 0:
        ant[0] = ((1 - ant[2]) + ant[0])%n
    else:
        ant[1] = ((2 - ant[2]) + ant[1])%n
    # loop it back aro
        


plt.imshow(config, cmap = cm.binary)
antmarker = {0:'^', 1:'>', 2:'v', 3:'<'}
plt.scatter(ant[1], ant[0], s=100, c='red', marker=antmarker[ant[2]])
plt.show()

plt.clf()

for image in range(i):
    
    #checks the current color
    color = config[ant[0],ant[1]]
    
    if color > 0:
        # black
        ant[2] = (ant[2] + 1) % 4
        #changes the cell to white
        config[ant[0],ant[1]] = 0
        # moves forward
        move()
    else :
        # black
        ant[2] = (ant[2] - 1) % 4
        #changes the cell to block
        config[ant[0],ant[1]] = 1
        # moves forward
        move()
        
    imshow(config, cmap = cm.binary)
    antmarker = {0:'^', 1:'>', 2:'v', 3:'<'}
    scatter(ant[1], ant[0], s=100, c='red', marker=antmarker[ant[2]])
    show()
    plt.pause(0.000001) 
    if image != (i-1):
        clf()

'''
