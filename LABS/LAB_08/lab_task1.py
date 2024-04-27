from node import Node
from EightPuzzleProblem import EightPuzzleProblem
from breadthFirstSearchStrategy import BreadthFirstSearchStrategy

class Search(object):
    def __init__(self, searchProblem, searchStrategy):
        self.searchProblem = searchProblem
        self.searchStrategy = searchStrategy
        self.nodesExpanded = 0  # Counter to track the number of nodes expanded

    def solveProblem(self):
        node = Node(self.searchProblem.initialState(), None, 0, 0, '')
        self.searchStrategy.addNode(node)

        duplicateMap = {}
        duplicateMap[node.state.stringRep()] = node.state.stringRep()
        result = None
        while not self.searchStrategy.isEmpty():
            self.nodesExpanded += 1  # Increment the counter for each node expanded
            currentNode = self.searchStrategy.removeNode()
            if self.searchProblem.isGoal(currentNode.state):
                result = currentNode
                break
            nextMoves = self.searchProblem.succesorFunction(currentNode.state)
            for nextState in nextMoves:
                if nextState.stringRep() not in duplicateMap:
                    newNode = Node(nextState, currentNode, currentNode.depth + 1,
                                   currentNode.cost + nextState.cost, nextState.action)
                    self.searchStrategy.addNode(newNode)
                    duplicateMap[newNode.state.stringRep()] = newNode.state.stringRep()
        return result

    def printResult(self, result):
        if result.parentNode is None:
            print("Game Starts")
            print("Initial State : %s" % result.state.getCurrentState())
            return
        self.printResult(result.parentNode)
        print("Perform the following action %s, New State is %s, cost is %d" % (result.action, result.state.getCurrentState(), result.cost))

    def getNodesExpanded(self):
        return self.nodesExpanded
