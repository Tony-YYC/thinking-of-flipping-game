import numpy as np
class chessGame():
    def __init__(self,type):
        self.solutionStatus = 1
        self.solution = []
        self.type=type

    def input(self):
        self.m,self.n = map(int,input("Please input the size of your chessboard in rows,lines:").split(","))
        matrixList = []
        for i in range(0,self.m):
            rowList = input("Please input line " + str(i+1) + " split by , :").split(",")
            rowList = list(map(int,rowList))
            matrixList.append(rowList)
        #print(matrixList)
        self.M = np.matrix(matrixList)

    def columnMatch(self):
        for j in range(0,self.n):
            sign = self.M[0,j] / self.M[0,0]
            for p in range(0,self.m):
                if self.M[p,j] / self.M[p,0] == sign:
                    continue;
                else:
                    self.solutionStatus = 0
                    break
            if(self.solutionStatus == 1) and (sign == -1):
                operation = "c" + str(j+1)
                self.solution.append(operation)
    
    def rowMatch(self):
        if self.solutionStatus:
            for i in range(0,self.m):
                if self.M[i,0] == -self.type:
                    operation = "r" + str(i+1)
                    #print(operation)
                    self.solution.append(operation)

    def output(self):
        if self.solutionStatus:
            print(self.solution)
        else:
            print("NOANSWER")

type = int(input("Please choose type of the game.\nTo reach All black input -1, All white 1:"))
c = chessGame(type)
c.input()
c.columnMatch()
c.rowMatch()
c.output()