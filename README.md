ISOLATION GAME AGENT DYNAMICS![](Aspose.Words.8232b645-eb60-4c7a-bd1d-49309f4373ff.001.png)![](Aspose.Words.8232b645-eb60-4c7a-bd1d-49309f4373ff.002.png)

Isolation-Game-Agent-Dynamics

Developing and Analyzing the Computer Agent of the game of Isolation made using the various applications of Artificial Intelligence concepts of Minimax, Alpha Beta Pruning, Machine Learning (Prediction Model). Implementation of the game.

Introduction![](Aspose.Words.8232b645-eb60-4c7a-bd1d-49309f4373ff.003.png)

- The project is about the game of Isolation and its agent dynamics.
- Isolation is a deterministic, two-player game of perfect information in which the players alternate turns moving a single piece from one cell to another on a board. 
- Whenever either player occupies a cell, that cell becomes blocked for the remainder of the game. The first player with no remaining legal moves loses, and the opponent is declared the winner.
- We have built an game playing agent by implementing adversarial searching algorithms (Minimax and AlphaBeta Pruning) to beat other players.
- We have also collected data and used a prediction model to implement a game playing agent and test its effectiveness against the other two agents. 

Problem Statement![](Aspose.Words.8232b645-eb60-4c7a-bd1d-49309f4373ff.003.png)

◦Developing and Analyzing the Computer Agent of the 

game of Isolation made using the various applications of Artificial Intelligence concepts of Minimax, Alpha Beta Pruning, Machine Learning (Prediction Model). Implementation of the game.

Project Description![](Aspose.Words.8232b645-eb60-4c7a-bd1d-49309f4373ff.003.png)

◦Performance Measure :- Win, Loss ◦Environment :- nXn grid

◦Actuators :- Placing the Pieces on the desired location, 

and deriving the moves of the agent according to the position.

◦Sensor :- Board Perceived as a nXn matrix. ◦Agent Types - 1 Learning Agent.

Methodology![](Aspose.Words.8232b645-eb60-4c7a-bd1d-49309f4373ff.003.png)

- MiniMax – Created a minimax algorithm to find the optimal move, for each turn it searches the probable moves. 
- It then iterates through them and recursively solves (minimizing the user, and maximizing the computers chances) till you get a solution, then it backtracks to the initial move chosen and gives it a score(win-(1), loss-(-1)). Based on the scores it choses the next move. 
- Alpha Beta Pruning – We add alpha beta pruning to the above algorithm, if in min function(minimum <= alpha) and in max function(maximum >= beta) then it directly returns the max/min without solving further, it makes the algorithm much faster.
- It results in much faster results and the game doesn’t crash in larger board(n) sizes.
- We have included an agent made using a prediction model for a board(4x4) size to see how it fares against the above two algorithms. The model is based on the data of the computer moves in which it wins. The model predicts the computers based on the users input and the stage of the game. We use the Multi-Output Regression model to train and predict the computers move. 

Proposed Solution![](Aspose.Words.8232b645-eb60-4c7a-bd1d-49309f4373ff.003.png)

- Creating the functional UI using the pygame library for the game and optimising the algorithms has led us to the following solutions.
- The UI consists of nxn(3-8) chessboards and the user and computer piece, it also consists of a region where you input the your move and then the computer moves accordingly.  
- Testing the algorithms we have found out that for small games like Isolation the algorithms such as MiniMax and Alpha Beta Pruning work better because the environments is small and the moves are less, hence they are accurate and fast to give the optimal solution.
- Alpha Beta Pruning is better because it selects the optimal solution and it is much faster than MiniMax algorithm because it skips further processing if the required solution has already been found. The speed is much more noticeable as the board size increases.
- Predictive Models are required to ensure optimality and reduce response time in large games, hence it is better ultimately if we have enough data.

Conclusion![](Aspose.Words.8232b645-eb60-4c7a-bd1d-49309f4373ff.003.png)

- The conclusion from the following project:
- User Interface for the games make them more functional, functional and appealing.
- The AlphaBeta pruning algorithm is accurate and optimal for games like Isolation in comparison to MiniMax.
- Data required to build a correct prediction model should be substantial and varied to accurately predict moves for the game agent. The more the data the more optimal moves the computer will make.
- Analysis of the three algorithms leads us to the conclusion that Alpha Beta Pruning is most optimal algorithm for the game Isolation. Based on the accuracy of the computer agent. 
