'''
Solves the problem described in the README
'''

from Tkinter import *
from random import randrange
import tkMessageBox # for message boxes to display to user


class demoFrame(Frame):
  '''
    Define a Python class for building a frame
  '''
  # need to initialize items in the class that Tkobject will call
  def __init__(self,master, maze, rows, cols, start_pos, dragon, sword, treasure, maze_name):
    '''
      Constructor of this class needs the root window
      object that Tk() creates:  the parameter "master" 
    '''
    self.root = master
    self.setDefaults()
    self.setCoords(maze, dragon, sword, treasure)
    self.maze_name = maze_name #populate the maze name on the gui

    #set number of rows for selected maze
    self.rows = rows
    self.cols = cols
     
    Frame.__init__(self,master)  # call superclass constructor first
    # (these next method calls are "magic", found by searching
    #  on 'tkinter frame' with a search engine)
    self.pack_propagate(0)  # turn off dynamic frame sizing
    self.pack(padx=10,pady=10)  # this puts the frame onto the window
    self.config(width=500,height=300)  # set frame width and height in pixels
    self.config(background="lightgreen",relief=RAISED)
    # (end of magic)
    self.widgets = []  # right now, there are no buttons or labels
    self.state = start_pos     # start with "state" equal zero
    self.buildWidgets()  # first time call to build all widgets
  
  def setCoords(self, maze, dragon, sword, treasure):
    self.maze = maze
    #set cooridinates to assigned value of dragon
    self.dragon = dragon
    #set cooridinates to assigned value of sword
    self.sword = sword
    #set cooridinates to assigned value of treasure
    self.treasure = treasure
  
  def setDefaults(self): #Sets Default values for Dragon and Sword to be false    
    self.slayedDragon = False 
    #dragon hasnt been slayed 
    self.hasSword = False
    #havent found sword
    
  def buildWidgets(self):
    '''
      This method creates widgets customized to the current state, 
      which is an integer in range(6).  When state is greater than
      zero, there is a "go left" button;  when state is less than
      five, there is a "go right" button.  Plus there is a label
      showing the current state.  

      Buttons are bound to the methods that will do the appropriate
      action when they are clicked.  

      An exit button is always present, to allow quitting. 
    '''
     
    inventory = 'None' # inventory begins empty
    if self.hasSword: inventory = 'Sword' # if user enters room with sword, inventory becomes sword

    showState = Label(self,text="Location: {0},{1} Difficulty: {2} Inventory: {3}".format(self.state[1], self.state[0], self.maze_name, inventory)) #label refreshing location, difficulty of maze, and current inventory
    showState.pack(side="bottom") # places label at bottom of GUI
    self.widgets.append(showState)

    R = self.state[0] # sets the current row location to R for readability
    C = self.state[1] # same for current column
     
    #Determines directions available by checking the surrounding rooms then creates the buttons
    self.buildNorth(C, R)
    self.buildEast(C, R)
    self.buildBottom(C, R)
    self.buildWest(C, R)
     
  def buildNorth(self, C, R):   #builds the North Button 
    if (R > 0): #if position is greater than 0 ( cant go further north if position already at northern most 'y' positon) 
      TOPWALL = self.maze[R - 1][C][0] # Determines if there is a top wall by checking if the room to the north has a bottom wall
      if not TOPWALL: # determins whether current position has wall above
        northButton = Button(self, text="North") #button named north
        northButton.bind("<Button-1>", self.goNorth)
        northButton.pack(side="top") # places button on top of gui
        self.widgets.append(northButton)
         
  def buildEast(self, C, R): #builds east button    
    if (C < self.cols - 1):# Subtracts 1 from the total number of columns so cannot go further east than maximum columns in maze
      RIGHTWALL = self.maze[R][C][1]
      if not RIGHTWALL: #self.maze[R][C][1]: # if there is not a right wall to prevent moving east
        eastButton = Button(self,text="East")#button named east
        eastButton.bind("<Button-1>",self.goEast) 
        eastButton.pack(side="right") #places button on right side of gui
        self.widgets.append(eastButton)  
         
  def buildBottom(self, C, R): #builds south button 
    if (R < self.rows - 1):  #Subtracts 1 from the total number of rows so cannot go further south than maximum rows in maze
      BOTTOMWALL = self.maze[R][C][0] # Determines if there is a bottom wall
      if not BOTTOMWALL: # if current room has no bottom wall
        southButton = Button(self, text="South") #button named south
        southButton.bind("<Button-1>", self.goSouth)
        southButton.pack(side="bottom")#button placed on bottom of GUI
        self.widgets.append(southButton)           
    
  def buildWest(self, C, R): #builds west button
    if (C > 0): #if position is greater than 0 ( cant go further west if position already at western most 'x' positon)
      LEFTWALL = self.maze[R][C - 1][1] # Subtract 1 from the column to check if the room to the left has a right wall
      if not LEFTWALL: # if current room has no left wall
        westButton = Button(self, text="West") #button named west
        westButton.bind("<Button-1>", self.goWest)
        westButton.pack(side="left") #places button on left of GUI
        self.widgets.append(westButton)           
  
  def clearWidgets(self):
    '''
      Take back any widgets we put on the frame, so it is clean for rebuilding.
    '''
    for widget in self.widgets:
      widget.destroy()
    self.widgets = []   # now there are no widgets in frame

  def quit(self,mouseEvent=False):
    import sys
    sys.exit(0)   # this forces immediate quit of entire application
  
  def checkArea(self): #for every move checks area for items (dragon,sword,treasue)
    if (self.state == self.dragon): #if current position is same as dragons postion
      if (self.hasSword and self.slayedDragon == False): #if you have the sword and havent killed the dragon yet...
        reason = 'You killed the dragon!' #prompt in message box
        self.slayedDragon = True #dragon is now slayed 
        tkMessageBox.showwarning("GOOD JOB!", reason) #displays message box congratulating player
      elif (self.slayedDragon == True):
        #Do nothing if you have already killed the dragon
        pass      
      else:
        tkMessageBox.showwarning("Exiting", "Fought The Dragon without the Sword! You Lose!") #lose game
        self.quit() #exit program
    elif (self.state == self.sword and self.hasSword == False): 
      # if current location has the sword and you dont have the sword yet (havent visited that location
      tkMessageBox.showwarning("Nice!", " You found a Sword!") # you now found the sword
      self.hasSword = True # self state becomes true for remainer of game
    elif (self.state == self.treasure): # if you moved into a space with the treasure
      tkMessageBox.showwarning("Exiting", "Found Treasure You Win!")
      self.quit()#exits program you win !

  def goWest(self,mouseEvent): 
    #increments location one position to the left increments the state value and redraw the frame.
    self.state[1] -= 1
    self.checkArea()
    self.clearWidgets()
    self.buildWidgets()

  def goNorth(self, mouseEvent):
    #increments location one position up aka to the north increments the state value and redraw the frame.
    self.state[0] -= 1
    self.checkArea()
    self.clearWidgets()
    self.buildWidgets()


  def goSouth(self, mouseEvent):
    #increments location one position down aka to the south increments the state value and redraw the frame.
    self.state[0] += 1 
    self.checkArea()
    self.clearWidgets()
    self.buildWidgets()


  def goEast(self,mouseEvent):
    #increments location one position to the right increments the state value and redraw the frame.
    self.state[1] += 1
    self.checkArea()
    self.clearWidgets()
    self.buildWidgets()

#-----( main program starts here )---------------------------------------------

def randomize(rows,cols):
  return [randrange(cols), randrange(rows)]

easy = [[[False, True], [False, False], [True, False], [True, True]], [[False, True], [False, True], [False, False], [False, True]], [[False, True], [False, True], [False, True], [False, True]], [[True, False], [True, False], [True, True], [True, True]]]

medium = [[[False, False], [True, False], [True, True], [False, False], [False, True]], [[False, True], [False, False], [False, True], [False, True], [False, True]], [[True, False], [True, True], [True, False], [True, True], [False, True]], [[False, True], [False, False], [True, False], [False, True], [False, True]], [[True, False], [True, False], [True, True], [True, False], [True, True]]]

hard = [[[False, False], [True, True], [False, False], [True, True], [False, False], [False, True]], [[False, False], [True, False], [True, True], [False, False], [True, True], [False, True]], [[False, True], [False, False], [True, False], [True, False], [True, True], [False, True]], [[False, True], [True, True], [False, False], [True, False], [False, True], [False, True]], [[True, False], [False, True], [False, True], [False, True], [False, True], [False, True]], [[True, False], [True, False], [True, True], [True, False], [True, False], [True, True]]]

mazes = [easy, medium, hard] # assigns each maze a name
maze = randrange(len(mazes)) #'randomly' chooses a maze to load

#names of each maze
if maze == 0:
  maze_name = 'Easy'
elif maze == 1:
  maze_name = 'Medium'
elif maze == 2:
  maze_name = 'Hard'

#the number of rows and columns in each maze  
rows = len(mazes[maze])
cols = len(mazes[maze][0])

#randomizes the start postion,dragon,sword, and treasure position
start = randomize(rows,cols)
dragon_pos = randomize(rows,cols)
sword_pos = randomize(rows,cols)
treasure_pos = randomize(rows,cols)

#ensures that start location and no items can be in the same location
if (dragon_pos == sword_pos or dragon_pos == treasure_pos or dragon_pos==start):
  dragon_pos = randomize(rows,cols)
elif (sword_pos == treasure_pos or sword_pos==start):
  sword_pos = randomize(rows,cols)
elif (start == treasure_pos):
  treasure_pos = randomize(rows,cols)
  
#print "Level: %s\nStart: %s\nDragon: %s\nSword: %s\nTreasure: %s" % (maze_name, start, dragon_pos, sword_pos, treasure_pos)
#used for debugging

root = Tk()
Tkobject = demoFrame(root, mazes[maze], rows, cols, start, dragon_pos, sword_pos, treasure_pos, maze_name)
Tkobject.mainloop()
