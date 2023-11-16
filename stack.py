
class Stack :
    def __init__(self):
        self.stack: str = ''

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, str):
        self.stack += str

    def pop(self):
        self.stack = self.stack[::-1]