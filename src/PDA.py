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
        self.stack.push(topstackbaru)
        print("Awal Transition: Stack =", self.stack.get_items(), "Top =", self.stack.top())

        for symbol in input_list:
            print("Current State:", statebaru)
            print("Current Symbol:", symbol)
            if statebaru == '':
                return False

            found_transition = False
            print("Before Transition: Stack =", self.stack.get_items(), "Top =", topstackbaru)

            if statebaru in self.transition:
                print("Transition State:", statebaru)
                print("Transition Rules:", self.transition[statebaru])
                transition_dict = self.transition[statebaru]
                if symbol in transition_dict:
                    if self.stack.top() in transition_dict[symbol]:
                        next_state, push_stack = transition_dict[symbol][self.stack.top()]
                    else:
                        return False
                else:
                    return False

                found_transition = True
                top_stack = self.stack.top()
                print(top_stack)
                if push_stack == 'e':
                    self.stack.pop()  # Pop the top of the stack if the stack operation is not empty
                    print("Before Transition: Stack =", self.stack.get_items(), "Top =", topstackbaru)
                    top_stack = self.stack.top()
                    print(top_stack)
                else :
                    self.stack.pop()
                    print("Before Transition: Stack =", self.stack.get_items(), "Top =", topstackbaru)
                    self.stack.push(push_stack)  # Push symbols onto the stack in reverse order
                    top_stack = self.stack.top()
                    print(top_stack)
                
                statebaru = next_state
                
                print("After Transition: Stack =", self.stack.get_items(), "Top =", self.stack.top())
                

        # Check if the final state is an accepting state and the stack is empty
        return statebaru in self.accepting_states and self.stack.is_empty()