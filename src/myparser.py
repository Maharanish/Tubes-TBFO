from PDA import PDA

def parse_pda_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

        state = lines[0].split()
        alphabet = lines[1].split()
        stack_symbol = lines[2].split()
        start_state = lines[3].strip()
        start_stack_symbol = lines[4].strip()
        accepting_states = lines[5].split()

        transition = {}

        for line in lines[7:]:
            parts = line.split()
            current_state, input_symbol, top_stack, next_state, push_stack = parts
            if current_state not in transition:
                transition[current_state] = {}
            if input_symbol not in transition[current_state]:
                transition[current_state][input_symbol] = {}
            if top_stack not in transition[current_state][input_symbol]:
                transition[current_state][input_symbol][top_stack] = (next_state, push_stack)

        return state, alphabet, transition, start_state, start_stack_symbol, stack_symbol, accepting_states


