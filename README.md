# Tic-Tac-Toe-AI
Tic-Tac-Toe is a two player board game. Players take turn to mark the spaces in 3x3 grid with O's and X's. The player who succeeds in placing three of their marks in horizontal, vertical, or diagonal row is the winner.

In this project, players will play against an AI bot created using <b>minmax</b> algorithm. AI bot is slow in the start as it goes through the entire game tree and chooses the best move. As the game progresses, the number of moves decrease and so does the size of game tree dreduces. So, the bot speeds up. 

Also, this AI bot would never lose. 

-> runner.py : This contains the implementation of the minmax algorithm for the game.
-> tictactoe.py : This contains the front end of the game made using pygame. (Taken from Harvard CS50 class). 
-> test.py : Used this to test different scenarios. 
