
class Stack :
    def __init__(self):
        self.symbol = []

    def is_empty(self):
        return len(self.symbol) == 0

    def push(self, stacksymbol):
        self.symbol.append(stacksymbol)

    def pop(self):
        if not self.is_empty():
            return self.symbol.pop()
        else:
            print("Stack is empty")