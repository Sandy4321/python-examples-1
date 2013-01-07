
  The purpose of the Python GUI application is to put the user
  in a randomly selected maze of at least sixteen rooms with 
  connections between the rooms.  There is a room with treasure,
  and if the user moves to that room, the maze is solved:  the
  user wins!  To make the game interesting, there is one room
  with a dragon.  If the user moves to the room with the dragon,
  then the user loses (game over), EXCEPT if the user has a 
  sword.  So, there is a room with a sword.  When the user moves
  to the room with the sword, the user gains the sword and keeps
  it forever after.  Initially, the user has no sword and is in
  a room where there is neither sword nor dragon.  The maze is 
  set up so that there can be some way to win.  

  On the window for the application, the user can see buttons 
  that say what directions the user can move:  north, south, 
  east, west.  The window can also show labels about whether the
  user has a sword, and other status information.  Basically, the 
  user can just click on buttons and move from room to room.

  In addition to the information of Chapter 27, there is a 
  small, working GUI program in this directory, guisample.py, 
  that you can try.  It's not very nicely done, but does illustrate  
  a few widgets and some dynamic behavior.  Your application should
  be better than this.

  RULES FOR YOUR CODE 

      (a) No function or method can be longer than 20 lines!  
          (Except for comments and docstrings, which do not count 
          for the 20 lines) 

          "Cheating" around the 20 line restriction, like using 
          semicolon, extended lines with continuation (backslash)
          or combining one-line bodies --- tricks NOT ALLOWED.

      (b) All functions/methods must be documented, to say what is the
          purpose, what are the arguments (if any), and what are
          the output(s), what are the intended goals and effects. 

      (c) The way that the program represents the game, how the 
          user location and other information is represented, should
          be described in comments or a docstring.  

  1.  Grading/Scoring criteria:

      i.   Does it work?
      ii.  Does it follow the rules (a)-(c) above?  
      iii. Does the code follow the original plan for documentation 
            on the functions/methods? 
      iv.  Originality/Features:  does your Python application go 
            beyond the bare minimum of buttons and text, say with 
            colors, other widgets and interactive behaviors? 

- Create class for all functions of the gui
- Create funtion to go north.
- Create function to go south
- Create function to east
- Create function to go west
- Create function that will only allow user to move in available directions within specified grid
- Create gui that refreshes each location using axis and will also display if sword has been claimed
- Create function to randomize sword,dragon and treasure placement.
- Create Button to exit game on win / lose
- Create function that will automatically determine a loss if user moves into dragon room without a sword. 


