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

#     def process(self, input_list: list[str]) -> bool:
#         statebaru = self.startState
#         topstackbaru = self.startStackSymbol

#         for symbol in input_list:
#             print("Current State:", statebaru)
#             print("Current Symbol:", symbol)
            
#             if statebaru == '':
#                 return False

#             found_transition = False

#             if statebaru in self.transition:
#                 transition_dict = self.transition[statebaru]
#                 if symbol in transition_dict:
#                     transition_tuple = transition_dict[symbol]
#                 elif '' in transition_dict:
#                     transition_tuple = transition_dict['']
#                 else:
#                     return False


#         # Check if the final state is an accepting state and the stack is empty
#         return statebaru in self.accepting_states and self.stack.is_empty()


    # def process(self, input_list: list[str]) -> bool:
    #     statebaru = self.startState
    #     topstackbaru = self.startStackSymbol

    #     for symbol in input_list:
    #         print("Current State:", statebaru)
    #         print("Current Symbol:", symbol)

    #         if statebaru == '':
    #             return False

    #         found_transition = False
    #         for transition_state, transition_rules in self.transition.items():
    #             print("Transition State:", transition_state)
    #             print("Transition Rules:", transition_rules)

    #             if transition_state == statebaru and (symbol in transition_rules or '' in transition_rules) and topstackbaru in transition_rules.values():
    #                 found_transition = True

    #                 # Assume that there's only one matching transition rule for simplicity
    #                 transition = next(iter(transition_rules.values()))

    #                 statebaru = transition[0]
    #                 topstackbaru = transition[1]

    #                 if transition[1] != '':
    #                     self.stack.pop()

    #                 for stack_symbol in transition[1][::-1]:
    #                     self.stack.push(stack_symbol)

    #                 break

    #         if not found_transition:
    #             return False

    #     return statebaru in self.accepting_states and self.stack.is_empty()


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
                elif '' in transition_dict:
                    #top_stack, next_state, push_stack = transition_dict['']
                    if self.stack.top() in transition_dict['']:
                        next_state, push_stack = transition_dict[symbol][self.stack.top()]
                else:
                    return False
                
                

                found_transition = True
                top_stack = self.stack.top()
                print(top_stack)
                if push_stack == '':
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
                
            # if push_stack != '':
            #     topstackbaru = push_stack
            #     if not self.stack.is_empty():  # Check if the stack is not empty
            #         self.stack.pop()  # Pop the top of the stack if the stack operation is not empty
            #         top_stack = self.stack.top()  # Use the top method to get the new top element
            #     else:
            #         # Handle the case when push_stack is empty
            #         top_stack = None  # or raise an exception, return a special value, etc.


    
                

        # Check if the final state is an accepting state and the stack is empty
        return statebaru in self.accepting_states and self.stack.is_empty()
    
    
    
    
    # def process(self, input_list: list[str]) -> bool:
    #     statebaru = self.startState
    #     topstackbaru = self.startStackSymbol
    #     self.stack.push(topstackbaru)
    #     print("Awal Transition: Stack =", self.stack.get_items(), "Top =", self.stack.top())

    #     for symbol in input_list:
    #         print("Current State:", statebaru)
    #         print("Current Symbol:", symbol)
    #         if statebaru == '':
    #             return False

    #         found_transition = False

    #         if statebaru in self.transition:
    #             print("Transition State:", statebaru)
    #             print("Transition Rules:", self.transition[statebaru])
    #             transition_dict = self.transition[statebaru]
    #             if symbol in transition_dict:
    #                 top_stack, next_state, push_stack = transition_dict[symbol]
    #             elif '' in transition_dict:
    #                 top_stack, next_state, push_stack = transition_dict['']
    #             else:
    #                 return False

    #             found_transition = True
    #             print("Before Transition: Stack =", self.stack.get_items(), "Top =", topstackbaru)

    #             if push_stack == '':
    #                 if not self.stack.is_empty():
    #                     topstackbaru = self.stack.pop()  # Pop the top of the stack if the stack operation is not empty
    #                 else:
    #                     # Handle the case when the stack is empty, you may want to return False or handle it appropriately
    #                     return False
    #             else:
    #                 self.stack.push(push_stack)  # Push symbols onto the stack
    #                 topstackbaru = push_stack

    #             statebaru = next_state
    #             print("After Transition: Stack =", self.stack.get_items(), "Top =", topstackbaru)

    #         # Check if the final state is an accepting state and the stack is empty
    #         return statebaru in self.accepting_states and self.stack.is_empty()
