import os
from stack import Stack

class PDA:
    def __init__(self, state, alphabet, transition, startState, startStackSymbol, symbol) -> None:
        self.state: list[str] = state
        self.alphabet: list[str] = alphabet
        self.transition = transition
        self.startState: str = startState
        self.startStackSymbol: str = startStackSymbol
        self.symbol: list[str] = symbol
        self.stack = Stack()
        self.currentState: str = startState

    def process(self, input: str) -> bool:
        for i in input:
            if i in self.alphabet:
                self.currentState = self.transition[self.currentState][i]
            else:
                return False
        return True