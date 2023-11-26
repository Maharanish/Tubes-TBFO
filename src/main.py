from PDA import PDA
from myparser import parse_pda_file
import time
import sys
from colorama import Fore, Style

def print_colored_ascii_art():
    art = """Hiii! Welcome to HTML Parser by Semoga Hoki AAMIIN!:D⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⣤⣤⣄⣀⡀⠀⠀⠀⠀⠀⣴⡟⠉⠀⠀⠀⠀⠙⢻⣆⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⠾⠛⠋⠉⠉⠉⠉⠙⠻⢷⣤⡀⠀⠀⣼⠏⠀⠀⠀⠀⠀⠀⠀⣿⡆
    ⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⡄⣼⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡇
    ⠀⠀⠀⠀⠀⠀⠀⢀⣿⠃⠀⠀⠀⠀⠀⠀⠀⣀⣰⣶⡆⠀⠀⠘⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⠁
    ⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⢰⣿⡖⠒⠈⠉⠀⠀⠉⠀⠀⠀⢠⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠇⠀
    ⠀⠀⠀⠀⠀⠀⠀⠘⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣞⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠏⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢹⣷⣄⡀⠀⠀⠀⠀⠀⠀⣀⣠⠴⠚⠁⠈⢧⡀⠀⠀⠀⠀⠀⢀⣴⡿⠋⠀⠀⠀
    ⠀⠀⠀⠀⠀⢀⣴⠟⢫⠿⠉⠛⠒⠒⠒⠛⠉⠉⠀⢀⠤⢄⠀⡐⢷⠀⠀⠀⣠⣴⠿⠋⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⢠⣿⢫⠀⠀⢰⣃⣀⣇⣀⣀⣀⣀⣀⣀⣀⣉⣀⣀⣀⣀⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⢠⡿⠁⡈⠀⣠⠏⠀⠰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠡⠀⠙⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⢠⣿⠃⡐⠁⣰⠃⠀⡰⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠡⡀⠘⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⣼⡟⠊⠀⢠⣏⠤⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠢⣸⣷⠀⠀⠀⠀⠀⠀⠀⠀
    ⢠⣿⠀⠀⠀⣼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡇⠀⠀⠀⠀⠀⠀⠀
    ⢸⡟⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀
    ⢸⣇⠀⠀⠀⠸⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⠃⠀⠀⠀⠀⠀⠀⠀
    ⠘⣿⠀⠀⠀⠀⠹⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠏⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⢻⣧⠀⠀⠀⠀⢸⠳⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⢻⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠻⣧⣀⠀⠀⣸⡆⠀⡝⠓⠦⣤⣀⣀⡀⠀⠀⠀⣀⣀⣤⠴⠚⢹⠀⣸⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠈⠛⠛⠛⢻⣧⠜⠀⠀⠀⠀⠀⠈⠉⢹⣏⠉⠉⠀⠀⠀⠀⠀⢣⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢻⣦⠀⠀⠀⠀⠀⠀⠀⣾⣿⡀⠀⠀⠀⠀⠀⢠⣾⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⣄⡀⠀⠀⠀⣴⡟⢻⣷⣀⠀⣀⣠⣴⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠿⠿⠟⠋⠀⠀⠙⠛⠿⠟⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """

    colored_art = ""
    colors = [Fore.LIGHTYELLOW_EX, Fore.RED, Fore.YELLOW, Fore.BLUE, Fore.YELLOW, Fore.CYAN, Fore.GREEN]
    color_index = 0

    for char in art:
        if char == '\n':
            colored_art += char
        elif char == ' ':
            colored_art += char
        else:
            colored_art += colors[color_index % len(colors)] + char + Style.RESET_ALL
            color_index += 1

    print(colored_art)

# Call the function to print the colored ASCII art
print_colored_ascii_art()


print("Please input your PDA rules's path directory below!")
file_path = input()
print()
print("Thank you!")
print()
with open(file_path, 'r', encoding='utf-8') as file:
    state, alphabet, transition, start_state, start_stack_symbol, stack_symbol, accepting_states = parse_pda_file(file_path)
pda = PDA(state, alphabet, transition, start_state, start_stack_symbol, stack_symbol, accepting_states)
print("Let's see your PDA's data!")
#print("State:", state)
#print("Alphabet:", alphabet)
#print("Transition:", transition)
print("Start State:", start_state)
print("Start Stack Symbol:", start_stack_symbol)
#print("Stack Symbol:", stack_symbol)
print("Accepting States:", accepting_states)

print()
print("Please input your HTML file's path directory below!")
html_file_path = input("")
print()
print("Thank you!")
print()
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

print("──────────────────────── ⋆⋅☆⋅⋆ ────────────────────────")
if result == True:
    print(f"{Fore.YELLOW}  OKAY! GOOD JOB! YOUR HTML FILE HAS CORRECT SYNTAX :) {Style.RESET_ALL}")
else:
    print(f"{Fore.YELLOW}<----------YOUR HTML FILE HAS SYNTAX ERROR :(----------->{Style.RESET_ALL}")
print("──────────────────────── ⋆⋅☆⋅⋆ ────────────────────────")
