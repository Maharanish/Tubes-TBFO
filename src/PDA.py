import os
from stack import Stack

class PDA:
    def __init__(self, state, alphabet, transition, startState, startStackSymbol, symbol, accepting_states) -> None:
        self.state: list[str] = state
        self.alphabet: list[str] = alphabet
        self.transition = transition
        self.startState: str = startState
        self.startStackSymbol: str = startStackSymbol
        self.symbol: list[str] = symbol
        self.stack = Stack()
        self.currentState: str = startState
        self.accepting_states = accepting_states

    def process(self, input_list: list[str]) -> bool:
        statebaru = self.startState
        topstackbaru = self.startStackSymbol

        for symbol in input_list:
            if statebaru == '':
                return False

            found_transition = False
            for transition in self.transition:
                if transition[0] == statebaru and (transition[1] == symbol or transition[1] == '') and transition[3] == topstackbaru:
                    found_transition = True
                    statebaru = transition[2]
                    topstackbaru = transition[4]

                    if transition[3] != '':
                        self.stack.pop()  # Pop the top of the stack if the stack symbol is not empty

                    for stack_symbol in transition[4][::-1]:
                        self.stack.push(symbol)  # Push symbols onto the stack in reverse order
                        
                    break

            if not found_transition:
                return False

        # Check if the final state is an accepting state and the stack is empty
        return statebaru in self.accepting_states and self.stack.is_empty()