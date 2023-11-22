from PDA import PDA
from myparser import parse_pda_file

# Example usage:
print("mulai")
#state_set = {'p', 'q', 'r'}
#alphabet_set = {'0', '1'}
#transition_rules = {
#    'p': {
#        '0': {'#':('p','#0'),
#              '0':('p','00'),
#            },
#        '1': {'0':('q', ''),},
#        '!': {'#': ('r', ''),},
#    },
#    'q': {
#       '1': {'0':( 'q', ''),},
#        '!': {'#': ('r', ''),},
#    },
#}



#start_state = 'p'
#symbol_stack = {'#', '0', '1'}
#start_stack_symbol = '#'
#accepting_states = {'r'}

file_path = input()
with open(file_path, 'r', encoding='utf-8') as file:
    # your code here
    state, alphabet, transition, start_state, start_stack_symbol, stack_symbol, accepting_states = parse_pda_file(file_path)

    # Create an instance of PDA
pda = PDA(state, alphabet, transition, start_state, start_stack_symbol, stack_symbol, accepting_states)

    # Example: Print the parsed information
print("State:", state)
print("Alphabet:", alphabet)
print("Transition:", transition)
print("Start State:", start_state)
print("Start Stack Symbol:", start_stack_symbol)
print("Stack Symbol:", stack_symbol)
print("Accepting States:", accepting_states)

print("cek2")

# Process input
# Specify the path to your HTML file
html_file_path = input("")

try:
    with open(html_file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()
except FileNotFoundError:
    print(f"Error: File not found at {html_file_path}")
    exit(1)
except UnicodeDecodeError as e:
    print(f"Error decoding file: {e}")
    exit(1)

result = pda.process(html_content)
print("result:", result)