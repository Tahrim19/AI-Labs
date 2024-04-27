from SearchStrategy import SearchStrategy
from queue import Queue

class BreadthFirstSearchStrategy(SearchStrategy):
    def __init__(self):
        self.queue = Queue()

    def isEmpty(self):
        return self.queue.empty()

    def addNode(self, node):
        return self.queue.put(node)

    def removeNode(self):
        return self.queue.get()
