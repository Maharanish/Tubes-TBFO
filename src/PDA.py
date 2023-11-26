import os
from stack import Stack
from colorama import Fore, Style

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
        self.stack.push(topstackbaru)
        #print("Awal Transition: Stack =", self.stack.get_items(), "Top =", self.stack.top())
        line = 1
        for symbol in input_list:
            if symbol == '\n':
                symbol = '|'
                line+=1
            if symbol == ' ':
                symbol = '|'
            #print("Current State:", statebaru)
            #print("Current Symbol:", symbol)
            if statebaru == '':
                return False
            
            found_transition = False
            if statebaru in self.transition:
                #print("Transition State:", statebaru)
                #print("Transition Rules:", self.transition[statebaru])
                transition_dict = self.transition[statebaru]
                if symbol in transition_dict:
                    if self.stack.top() in transition_dict[symbol]:
                        next_state, push_stack = transition_dict[symbol][self.stack.top()]
                    else:
                        print(Fore.RED + "UPS! Something wrong! Invalid transition in line", line, "for symbol", symbol, "and top of stack", self.stack.top() + Style.RESET_ALL)
                        return False
                else:
                    print(Fore.RED + "UPS! Something wrong! Invalid symbol", symbol, "for state", statebaru, "in line", line, Style.RESET_ALL)
                    return False

                found_transition = True
                if push_stack == '$':
                    self.stack.pop()  # Pop the top of the stack if the stack operation is not empty
                    #print("After pop: Stack =", self.stack.get_items(), "Top =", topstackbaru)
                    top_stack = self.stack.top()
                    #print(top_stack)
                else :
                    self.stack.pop()
                    #print("after pop: Stack =", self.stack.get_items(), "Top =", topstackbaru)
                    self.stack.push(push_stack)  # Push symbols onto the stack in reverse order
                    top_stack = self.stack.top()
                    #print(top_stack)
                
                statebaru = next_state
                
                #print("After Transition: Stack =", self.stack.get_items(), "Top =", self.stack.top())
                

        # Check if the final state is an accepting state and the stack is empty
        return statebaru in self.accepting_states and self.stack.is_empty()