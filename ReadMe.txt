Playing with Minimax + Alpha-Beta Pruning

Main is in connect3.py
To run from terminal: 
sh run.sh print
sh run.sh next
sh run.sh random
sh run.sh minimax
sh run.sh alphabeta

After timing both the minimax player and alpha-beta player, we can conclude that the alpha-beta player takes
significantly less time than the minimax player to decide on a move due to pruning.

Here are the results of a sample game for each game (O is Minimax or alpha-beta player, X is always random player):

MINIMAX PLAYER
4.430645942687988  seconds per minimax player move
0.14114165306091309  seconds per minimax player move
0.004352092742919922  seconds per minimax player move
0.0007200241088867188  seconds per minimax player move
O wins!
 ----   ----   ----   ----   ----   ----
|    | |    | |    | |    | |   O| |   O|
|    | |    | |    | |   X| |   X| | X X|
|    | |   X| | O X| | O X| | O X| | O X|
 ----   ----   ----   ----   ----   ----
 ----   ----   ----
|   O| |   O| |   O|
| X X| |XX X| |XX X|
|OO X| |OO X| |OOOX|
 ----   ----   ----

ALPHA-BETA PLAYER
0.5533130168914795  seconds per alpha-beta player move
0.06532955169677734  seconds per alpha-beta player move
0.009408712387084961  seconds per alpha-beta player move
O wins!
 ----   ----   ----   ----   ----   ----
|    | |    | |    | |    | |    | |    |
|    | |    | |    | | X  | | X  | |XX  |
|    | |   X| | O X| | O X| |OO X| |OO X|
 ----   ----   ----   ----   ----   ----
 ----
|    |
|XX  |
|OOOX|
 ----
