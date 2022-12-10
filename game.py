#112003133 Isolation Game (Computer Agent using Min-Max Algorithm with Alpha Beta Pruning)
import pandas as pd
from sklearn import model_selection
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import multioutput
from sklearn.multioutput import MultiOutputRegressor
from sklearn.svm import SVR

class Isolation():
    def __init__(self,size) -> None:
        self.size = size
        self.b = []
        self.u = [0,0]
        self.c = [self.size-1,self.size-1]
        self.u1 = [0,0]
        df = pd.read_csv("Data4x4.csv")
        train1 = df.drop(['CX','CY'],axis=1)
        test1 = df[['CX','CY']] 

        X_train1, X_test1, y_train1, y_test1 = train_test_split(train1, test1, test_size=1, random_state=4)

        self.regr2 = MultiOutputRegressor(SVR())
        self.regr2.fit(X_train1.values,y_train1)
        for i in range(self.size):
            self.b.append([])
            for j in range(self.size):
                if (i == 0 and j == 0) or (i == self.size-2 and j == self.size-2):
                    self.b[i].append('X')
                else:    
                    self.b[i].append('X')

    def game_end(self,m):
        if m == 0:
            moves = [[self.u[0]+1,self.u[1]+2],[self.u[0]-1,self.u[1]+2],[self.u[0]+1,self.u[1]-2],[self.u[0]-1,self.u[1]-2],
                    [self.u[0]+2,self.u[1]+1],[self.u[0]+2,self.u[1]-1],[self.u[0]-2,self.u[1]+1],[self.u[0]-2,self.u[1]-1]]
        else:
            moves = [[self.c[0]+1,self.c[1]+2],[self.c[0]-1,self.c[1]+2],[self.c[0]+1,self.c[1]-2],[self.c[0]-1,self.c[1]-2],
                    [self.c[0]+2,self.c[1]+1],[self.c[0]+2,self.c[1]-1],[self.c[0]-2,self.c[1]+1],[self.c[0]-2,self.c[1]-1]]
        end = True
        for i in moves:
            if i[0] >= 0 and i[1] >= 0 and i[0] <= self.size-1 and i[1] <= self.size-1:
                if self.b[i[1]][i[0]] == 'X':
                    end = False
                    return -1
        
        if end == True:
            if m == 0:    
                #print("Computer Wins")
                return 1
            else:
                #print("User Wins")
                return 0

    def valid_move(self,nm,m):
        if m == 0:
            moves = [[self.u[0]+1,self.u[1]+2],[self.u[0]-1,self.u[1]+2],[self.u[0]+1,self.u[1]-2],[self.u[0]-1,self.u[1]-2],
                    [self.u[0]+2,self.u[1]+1],[self.u[0]+2,self.u[1]-1],[self.u[0]-2,self.u[1]+1],[self.u[0]-2,self.u[1]-1]]
        else:
            moves = [[self.c[0]+1,self.c[1]+2],[self.c[0]-1,self.c[1]+2],[self.c[0]+1,self.c[1]-2],[self.c[0]-1,self.c[1]-2],
                    [self.c[0]+2,self.c[1]+1],[self.c[0]+2,self.c[1]-1],[self.c[0]-2,self.c[1]+1],[self.c[0]-2,self.c[1]-1]]
        if nm in moves and self.b[nm[1]][nm[0]] == 'X':
            if m == 0 and nm != self.c:
                return True
        return False

    def game(self):
        pass
    
    def max(self, alpha, beta):

        # Possible values for maxv are:
        # -1 - loss
        # 1  - win

        # We're initially setting it to -2 as worse than the worst case:
        maxv = -2

        px = None
        py = None
        moves = [[self.c[0]+1,self.c[1]+2],[self.c[0]-1,self.c[1]+2],[self.c[0]+1,self.c[1]-2],[self.c[0]-1,self.c[1]-2],
                 [self.c[0]+2,self.c[1]+1],[self.c[0]+2,self.c[1]-1],[self.c[0]-2,self.c[1]+1],[self.c[0]-2,self.c[1]-1]]
        result = self.game_end(1)
        # If the game came to an end, the function needs to return
        # the evaluation function of the end. That can be:
        # -1 - loss
        # 1  - win
        if result == 0:
            return (-1, 0, 0)
        elif result == 1:
            return (1, 0, 0)
        for i in moves:
                if i[0] >= 0 and i[1] >= 0 and i[0] <= self.size-1 and i[1] <= self.size-1 and self.b[i[1]][i[0]] == 'X':
                    # That's one branch of the game tree.
                    self.b[i[1]][i[0]] = 1
                    self.c = [i[0],i[1]]
                    (m, min_i, min_j) = self.min(alpha,beta)
                    # Fixing the maxv value if needed
                    if m > maxv:
                        maxv = m
                        px = i[0]
                        py = i[1]
                    self.b[i[1]][i[0]] = 'X'

                    if maxv >= beta:
                        return (maxv, px, py)

                    if maxv > alpha:
                        alpha = maxv
        return (maxv, px, py)


    
    def first_move(self, alpha, beta):

        # Possible values for maxv are:
        # -1 - loss
        # 1  - win

        # We're initially setting it to -2 as worse than the worst case:
        maxv = -2

        px = None
        py = None
        # If the game came to an end, the function needs to return
        # the evaluation function of the end. That can be:
        # -1 - loss
        # 1  - win
        for i in range(self.size):
            for j in range(self.size):
                if self.b[j][i] == 'X':
                    # That's one branch of the game tree.
                    self.b[j][i] = 1
                    self.c = [i,j]
                    (m, min_i, min_j) = self.min(alpha,beta)
                    # Fixing the maxv value if needed
                    if m > maxv:
                        maxv = m
                        px = i
                        py = j
                    self.b[j][i] = 'X'

                    if maxv >= beta:
                        return (maxv, px, py)

                    if maxv > alpha:
                        alpha = maxv
        return (maxv, px, py)


    def min(self, alpha, beta):

        # Possible values for minv are:
        # -1 - win
        # 1  - loss

        # We're initially setting it to 2 as worse than the worst case:
        minv = 2

        qx = None
        qy = None

        moves = [[self.u[0]+1,self.u[1]+2],[self.u[0]-1,self.u[1]+2],[self.u[0]+1,self.u[1]-2],[self.u[0]-1,self.u[1]-2],
                    [self.u[0]+2,self.u[1]+1],[self.u[0]+2,self.u[1]-1],[self.u[0]-2,self.u[1]+1],[self.u[0]-2,self.u[1]-1]]
        result = self.game_end(0)

        if result == 0:
            return (-1, 0, 0)
        elif result == 1:
            return (1, 0, 0)
        
        for i in moves:
                if i[0] >= 0 and i[1] >= 0 and i[0] <= self.size-1 and i[1] <= self.size-1 and self.b[i[1]][i[0]] == 'X':
                    self.b[i[1]][i[0]] = 0
                    self.u = [i[0],i[1]]
                    (m, max_i, max_j) = self.max(alpha,beta)
                    if m < minv:
                        minv = m
                        qx = i[0]
                        qy = i[1]
                    self.b[i[1]][i[0]] = 'X'
                    self.u = self.u1
                    if minv <= alpha:
                        return (minv, qx, qy)

                    if minv < beta:
                        beta = minv

        return (minv, qx, qy)
    

    def max_w(self):

        # Possible values for maxv are:
        # -1 - loss
        # 1  - win

        # We're initially setting it to -2 as worse than the worst case:
        maxv = -2

        px = None
        py = None
        moves = [[self.c[0]+1,self.c[1]+2],[self.c[0]-1,self.c[1]+2],[self.c[0]+1,self.c[1]-2],[self.c[0]-1,self.c[1]-2],
                 [self.c[0]+2,self.c[1]+1],[self.c[0]+2,self.c[1]-1],[self.c[0]-2,self.c[1]+1],[self.c[0]-2,self.c[1]-1]]
        result = self.game_end(1)
        # If the game came to an end, the function needs to return
        # the evaluation function of the end. That can be:
        # -1 - loss
        # 1  - win
        if result == 0:
            return (-1, 0, 0)
        elif result == 1:
            return (1, 0, 0)
        for i in moves:
                if i[0] >= 0 and i[1] >= 0 and i[0] <= self.size-1 and i[1] <= self.size-1 and self.b[i[1]][i[0]] == 'X':
                    # That's one branch of the game tree.
                    self.b[i[1]][i[0]] = 1
                    self.c = [i[0],i[1]]
                    (m, min_i, min_j) = self.min_w()
                    # Fixing the maxv value if needed
                    if m > maxv:
                        maxv = m
                        px = i[0]
                        py = i[1]
                    self.b[i[1]][i[0]] = 'X'

        return (maxv, px, py)

    

    def min_w(self):

        # Possible values for minv are:
        # -1 - win
        # 1  - loss

        # We're initially setting it to 2 as worse than the worst case:
        minv = 2

        qx = None
        qy = None

        moves = [[self.u[0]+1,self.u[1]+2],[self.u[0]-1,self.u[1]+2],[self.u[0]+1,self.u[1]-2],[self.u[0]-1,self.u[1]-2],
                    [self.u[0]+2,self.u[1]+1],[self.u[0]+2,self.u[1]-1],[self.u[0]-2,self.u[1]+1],[self.u[0]-2,self.u[1]-1]]
        result = self.game_end(0)

        if result == 0:
            return (-1, 0, 0)
        elif result == 1:
            return (1, 0, 0)
        
        for i in moves:
                if i[0] >= 0 and i[1] >= 0 and i[0] <= self.size-1 and i[1] <= self.size-1 and self.b[i[1]][i[0]] == 'X':
                    self.b[i[1]][i[0]] = 0
                    self.u = [i[0],i[1]]
                    (m, max_i, max_j) = self.max_w()
                    if m < minv:
                        minv = m
                        qx = i[0]
                        qy = i[1]
                    self.b[i[1]][i[0]] = 'X'
                    self.u = self.u1

        return (minv, qx, qy)
    
    def first_move_w(self):

        # Possible values for maxv are:
        # -1 - loss
        # 1  - win

        # We're initially setting it to -2 as worse than the worst case:
        maxv = -2

        px = None
        py = None
        # If the game came to an end, the function needs to return
        # the evaluation function of the end. That can be:
        # -1 - loss
        # 1  - win
        for i in range(self.size):
            for j in range(self.size):
                if self.b[j][i] == 'X':
                    # That's one branch of the game tree.
                    self.b[j][i] = 1
                    self.c = [i,j]
                    (m, min_i, min_j) = self.min_w()
                    # Fixing the maxv value if needed
                    if m > maxv:
                        maxv = m
                        px = i
                        py = j
                    self.b[j][i] = 'X'
        return (maxv, px, py)

    def display(self):
        for i in range(self.size):
            for j in range(self.size):
                print('{}|'.format(self.b[i][j]), end=" ")
            print()
        print()

    def predict(self,a1,a2,s):
        Xn1 = [[a1,a2,s]]
        moves = [[self.c[0]+1,self.c[1]+2],[self.c[0]-1,self.c[1]+2],[self.c[0]+1,self.c[1]-2],[self.c[0]-1,self.c[1]-2],
                [self.c[0]+2,self.c[1]+1],[self.c[0]+2,self.c[1]-1],[self.c[0]-2,self.c[1]+1],[self.c[0]-2,self.c[1]-1]]
        m1 = []
        for j in moves:
            if j[0] >= 0 and j[1] >= 0 and j[0] <= self.size-1 and j[1] <= self.size-1 and self.b[j[1]][j[0]] == 'X':
                m1.append([j[0],j[1]])
        pred = self.regr2.predict(Xn1)
        mov = [pred[0][0],pred[0][1]]
        l = []
        for i in m1:
            l.append(abs(i[0]-mov[0])+abs(i[1]-mov[1]))
        #print(m1[l.index(min(l))])
        return m1[l.index(min(l))]

    
    def predict_fm(self,a1,a2,s):
        Xn1 = [[a1,a2,s]]
        pred = self.regr2.predict(Xn1)
        return [round(pred[0][0]),round(pred[0][1])]

    def gameplay(self):
        m = 0
        a3 = 1
        n1 = 0
        while self.game_end(m) == -1:
            if m == 0:
                self.display()
                if a3 == 1:
                    pass
                else:
                    print("Computer's Position :",[self.c[0]+1,self.c[1]+1])
                    print("Current Position :", [self.u[0]+1,self.u[1]+1])

                a1 = int(input("Enter x coordinate of your move User : ")) - 1
                a2 = int(input("Enter y coordinate of your move User : ")) - 1
                if self.valid_move([a1,a2],m) == False and a3 == 0:
                    while self.valid_move([a1,a2],m) == False:
                        print("Enter Valid Move")
                        a1 = int(input("Enter x coordinate of your move User : ")) - 1
                        a2 = int(input("Enter y coordinate of your move User : ")) - 1
                self.b[a2][a1] = 0
                self.u = [a1,a2]
                self.u1 = self.u
            elif m == 1:
                if a3 == 1:
                    a3 = 0
                    (m1, b1, b2) = self.first_move_w()
                else:
                    (m1, b1, b2) = self.max_w()
                self.b[b2][b1] = 1
                self.c = [b1,b2]
            if m == 0:
                m = 1
            else:
                m = 0
            n1 += 1
        if m == 0:
            print("Computer Wins")
        elif m == 1:
            print("User Wins")        
        print("End")




#x1 = Isolation(4)
#x1.gameplay()




























"""
print("Welcome to the Isolation Game!!")
b = int(input("Enter size(n) of the board (nXn) : "))
a = Isolation(b)
m = 0
a3 = 1
while a.game_end(m) == -1:
    if m == 0:
        a.display()
        if a3 == 1:
            pass
        else:
            print("Computer's Position :",a.c)
            print("Current Position :", a.u)
            
        a1 = int(input("Enter x coordinate of your move User : "))
        a2 = int(input("Enter y coordinate of your move User : "))
        if a.valid_move([a1,a2],m) == False and a3 == 0:
            while a.valid_move([a1,a2],m) == False:
                print("Enter Valid Move")
                a1 = int(input("Enter x coordinate of your move User : "))
                a2 = int(input("Enter y coordinate of your move User : "))
        a.b[a2][a1] = 0
        a.u = [a1,a2]
        a.u1 = a.u
    elif m == 1:
        if a3 == 1:
            a3 = 0
            (m1, b1, b2) = a.first_move(-2,2)
        else:
            (m1, b1, b2) = a.max(-2, 2)
        a.b[b2][b1] = 1
        a.c = [b1,b2]
    if m == 0:
        m = 1
    else:
        m = 0
if m == 0:
    print("Computer Wins")
elif m == 1:
    print("User Wins")        
print("End")
"""
