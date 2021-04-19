import numpy as np
import random as rand

class ArtificialBeeColony():

    def __init__(self, D, Lb, Ub, n, generation, ans, func):
        self.D = D
        self.Lb = Lb
        self.Ub = Ub
        self.n = n
        self.generation = generation
        self.ans = ans
        self.func = func
        self.bestFunc = 0
        self.bestFoodSourceArray = np.zeros(D)
        self.foodSourceArray = np.ones((n,D))
        self.tmpFoodSourceArray = np.ones(D)
        self.funcArray = np.ones(n)
        self.fitnessArray = np.ones(n)
        self.trialArray = np.zeros(n)
        self.pArray = np.zeros(n)
        
    def fitness(self,X):
        if(X >= 0):
            return 1/(1 + X)
        else:
            return 1 + abs(X)

    def generateNew(self,X,Xp):
        Xnew = X + rand.uniform(-1,1)*(X - Xp)
        if(Xnew < self.Lb): return self.Lb
        elif(Xnew > self.Ub): return self.Ub
        else: return Xnew

    def updateSolution(self,index):
        randVariableToChange = rand.randint(0,self.D-1)
        randPartner = index
        while(randPartner == index):
            randPartner = rand.randint(0,self.n-1)

        for j in range(self.D):
            self.tmpFoodSourceArray[j] = self.foodSourceArray[index][j]
        self.tmpFoodSourceArray[randVariableToChange] = self.generateNew(self.foodSourceArray[index][randVariableToChange], self.foodSourceArray[randPartner][randVariableToChange])
        
        if(self.ans == 0): 
            oriVal = self.funcArray[index]
            newVal = self.func(self.tmpFoodSourceArray,self.D)
        elif(self.ans == 1):
            oriVal = self.fitnessArray[index]
            newVal = self.fitness(self.func(self.tmpFoodSourceArray,self.D))

        if(newVal < oriVal):
            self.foodSourceArray[index][randVariableToChange] = self.tmpFoodSourceArray[randVariableToChange]
            self.funcArray[index] = self.func(self.tmpFoodSourceArray,self.D)
            self.fitnessArray[index] = self.fitness(self.func(self.tmpFoodSourceArray,self.D))
            self.trialArray[index] = 0
        else:
            self.trialArray[index] = self.trialArray[index] + 1
            
    def printLocalBestSolution_MAX(self):
        localBest = int(np.where(self.funcArray == self.funcArray.max())[0])
        print("Local Best Food Source:", self.foodSourceArray[localBest])
        print("local Best F(x) =",self.funcArray.max())
        if(self.funcArray.max() > self.bestFunc):
            for i in range(self.D):
                self.bestFoodSourceArray[i] = self.foodSourceArray[localBest][i]
            self.bestFunc = self.funcArray.max()
            
    def printLocalBestSolution_MIN(self):
        localBest = int(np.where(self.funcArray == self.funcArray.min())[0])
        print("Local Best Food Source:", self.foodSourceArray[localBest])
        print("local Best F(x) =",self.funcArray.min())
        if(self.funcArray.min() < self.bestFunc):
            for i in range(self.D):
                self.bestFoodSourceArray[i] = self.foodSourceArray[localBest][i]
            self.bestFunc = self.funcArray.min()
        
    def printCurrentSolution(self):
        print("==================================")
        print("foodSourceArray\n", self.foodSourceArray)
        print("funcArray\n", self.funcArray)
        print("fitnessArray\n", self.fitnessArray)
        print("trialArray\n", self.trialArray)
        print("==================================")
    
    def init(self):
        if(self.ans == 0): self.bestFunc = 100
        elif(self.ans == 1): self.bestFunc = 0
            
        for i in range(self.n):
            for j in range(self.D):
                self.foodSourceArray[i][j] = rand.uniform(self.Lb, self.Ub)
            self.funcArray[i] = self.func(self.foodSourceArray[i,:],self.D)
            self.fitnessArray[i] = self.fitness(self.funcArray[i])
            
    def doRun(self):
        self.init()
            
        for gen in range(self.generation):
            print("Generation:", gen+1)

            #Employed Bee Phase
            for i in range(self.n):
                self.updateSolution(i)

            #Onlooker Bee Phase
            for i in range(self.n):
                self.pArray[i] = self.fitnessArray[i]/self.fitnessArray.sum()
            for i in range(self.n):
                if(rand.random() < self.pArray[i]):
                    self.updateSolution(i)
            
            if(self.ans == 0): self.printLocalBestSolution_MIN()
            elif(self.ans == 1): self.printLocalBestSolution_MAX()
            
            #Scout Bee Phase
            limit = 1
            for i in range(self.n):
                if(self.trialArray[i] > limit):
                    for j in range(self.D):
                        self.foodSourceArray[i][j] = rand.uniform(self.Lb, self.Ub)
                    self.funcArray[i] = self.func(self.foodSourceArray[i,:],self.D)
                    self.fitnessArray[i] = self.fitness(self.funcArray[i])
                    self.trialArray[i] = 0

        print("============================================")
        print("Best Food Source:", self.bestFoodSourceArray)
        print("Best F(x) =", self.bestFunc)
