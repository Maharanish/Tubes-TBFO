from PDA import PDA

# Example usage:
print("mulai")
state_set = {'p', 'q', 'r'}
alphabet_set = {'0', '1'}
transition_rules = {
    'p': {
        '0': {'#':('p','#0'),
              '0':('p','00'),
            },
        '1': {'0':('q', ''),},
    },
    'q': {
        '1': {'0':( 'q', ''),},
        '!': {'#': ('r', ''),},
    },
}

#('#', 'p', '#0'), ('0', 'p', '00')

start_state = 'p'
symbol_stack = {'#', '0', '1'}
start_stack_symbol = '#'
accepting_states = {'r'}

print("cek1")

# Pass accepting_states as an argument when creating the PDA instance
pda = PDA(state=state_set, alphabet=alphabet_set, transition = transition_rules, startState=start_state, startStackSymbol=start_stack_symbol, symbol=symbol_stack, accepting_states=accepting_states)
print(pda.state)

print("cek2")

# Process input
input_string = ['0','1','!']
result = pda.process(input_string)
print("result:", result)