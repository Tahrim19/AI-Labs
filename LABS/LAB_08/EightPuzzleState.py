from SearchState import SearchState 
class EightPuzzleState(SearchState): 

    def __init__(self, currentState,action,cost): 
        self.currentState = currentState 
        self.action = action 
        self.cost = cost 
        self.string = None 
    
    def getCurrentState(self): 
        return self.currentState 
    
    def getAction(self): 
        return self.action 
    
    def getCost(self): 
        return self.cost 
    
    def stringRep(self):
        if self.string is None:
            e = ''
            for i in range(len(self.currentState)):
                for j in range(len(self.currentState[i])):
                    e += str(self.currentState[i][j])
            self.string = e
        return self.string
