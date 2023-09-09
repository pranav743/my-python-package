from colorama import Fore, Style, init
import random

init(autoreset=True)  

def print_green(message):
    formatted_message = f"{Fore.GREEN}{message}{Style.RESET_ALL}"
    print(formatted_message)

def print_red(message):
    formatted_message = f"{Fore.RED}{message}{Style.RESET_ALL}"
    print(formatted_message)

def print_blue(message):
    formatted_message = f"{Fore.BLUE}{message}{Style.RESET_ALL}"
    print(formatted_message)

def print_yellow(message):
    formatted_message = f"{Fore.YELLOW}{message}{Style.RESET_ALL}"
    print(formatted_message)

def print_magenta(message):
    formatted_message = f"{Fore.MAGENTA}{message}{Style.RESET_ALL}"
    print(formatted_message)

def print_cyan(message):
    formatted_message = f"{Fore.CYAN}{message}{Style.RESET_ALL}"
    print(formatted_message)

def printr(*args, **kwargs):
    color_codes = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
    
    random_color = random.choice(color_codes)

    formatted_message = f"{random_color}{' '.join(map(str, args))}{Style.RESET_ALL}"

    print(formatted_message, **kwargs)


def print_list(input_list, sep="\n", end = ""):

    try:
        if not isinstance(input_list, list):
            raise ValueError("Argument must be a 'list'")
        
        formatted_output = sep.join(map(str, input_list))
        printr(formatted_output, end=end )

    except ValueError as ve:
        printr(ve)