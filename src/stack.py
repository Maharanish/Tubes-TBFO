
class Stack :
    def __init__(self):
        self.stack: str = ''

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, str):
        self.stack += str

    def pop(self):
        self.stack = self.stack[:-1]
    
    def top(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return ''
        
    def get_items(self):
        return self.stack

    
        