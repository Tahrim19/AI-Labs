class Node(object):
    def __init__(self, state, parentNode=None, depth=0, cost=0, action=''):
        self.state = state
        self.parentNode = parentNode
        self.depth = depth
        self.cost = cost
        self.action = action

    def __str__(self):
        return self.state + "-- " + self.action + "-- " + str(self.cost)
