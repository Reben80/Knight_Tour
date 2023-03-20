## Knight's Tour using Warnsdorf's rule with Pygame Visualization

This is a Python code that finds the Knight's Tour on a chessboard of size $ n \times n$ , using Warnsdorf's rule, and visualizes the result using the Pygame library. The code is written in Python 3 and can be executed on any platform.
How it works

The [Knight's Tour](https://en.wikipedia.org/wiki/Knight%27s_tour) is a mathematical problem that involves finding a sequence of moves for a knight on a chessboard, such that the knight visits every square exactly once.

The code defines the following functions:
-  ```is_valid_move(board, x, y)```: checks if a move to position (x, y) on the board is valid, i.e., if the position is inside the board and has not been visited yet.
- ```count_valid_moves(board, x, y)```: counts the number of valid moves that canbe made from position (x, y) on the board.
- ```knights_tour(board, x, y, move_count)```: a recursive function that finds the Knight's Tour starting from position (x, y) on the board, with the current move count equal to move_count.
- ```find_knights_tour(board_size)```: initializes the board and starts the recursive search for the Knight's Tour, returning the resulting board if found, or None otherwise.
- ```draw_board(screen, board, cell_size)```: draws the chessboard and the knight's moves on the Pygame screen.

The main function ```main()``` initializes the Pygame screen and runs the visualization loop until the user closes the window.
Requirements

To run this code, you need the following packages:

    Pygame
    NumPy

You can install them using pip:

```pip install pygame numpy```

How to use

To run the code, simply execute the script. The default board size is $10 \times 10$, but you can change this by modifying the board_size variable in the code.

If a Knight's Tour is found, the Pygame visualization window will display the solution. If not, the console will print "No Knight's Tour found."
License

This code is released under the MIT License.
