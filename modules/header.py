from rich.console import Console
from rich.text import Text

console = Console()

class ColorStyle:
    GREEN = "green"
    RED = "red"
    MAGENTA = "magenta"
    WHITE = "white"
    CYAN = "cyan"

def print_logo():
    max_width = 68
    ascii_art = [
        r"    _   __     __  _____                     ",
        r"   / | / /__  / /_/ ___/_________  ____  ___ ",
        r"  /  |/ / _ \/ __/\__ \/ ___/ __ \/ __ \/ _ \ ",
        r" / /|  /  __/ /_ ___/ / /__/ /_/ / /_/ /  __/",
        r"/_/ |_/\___/\__//____/\___/\____/ .___/\___/ ",
        r"                   [v1.0]      /_/           "
    ]
    for line in ascii_art:
        centered_line = line.center(max_width)
        console.print(Text(centered_line, style=ColorStyle.MAGENTA))

def print_separator():
    line_length = 74
    separator = Text("=" * line_length, style=ColorStyle.CYAN)
    console.print(separator)

def print_menu_option(number, text, style_number=ColorStyle.CYAN, style_text=ColorStyle.MAGENTA):
    number_text = Text(f"[{number:>2}]", style=style_number)
    text_line = Text(f"   {text}", style=style_text)
    return number_text + text_line

def display_menu():
    menu_options = {
        1: 'Port Scan',
        2: 'Traceroute',
        3: 'DNS Lookup',
        4: 'Ping',
        5: 'WHOIS Lookup',
        6: 'Reverse DNS Lookup',
        7: 'IP Geolocation',
        8: 'SSL Certificate Check',
        9: 'Subdomain Scanning'
    }

    half = len(menu_options) // 2
    for i in range(1, half + 1):
        left_line = print_menu_option(i, menu_options[i])
        right_line = print_menu_option(i + half, menu_options[i + half]) if i + half in menu_options else Text("")

        console.print(left_line, end=" " * (40 - len(left_line.plain)))
        console.print(right_line)

    if len(menu_options) % 2 == 1:
        last_key = len(menu_options)
        last_line = print_menu_option(
            last_key, menu_options[last_key],
            style_number=ColorStyle.MAGENTA,
            style_text=ColorStyle.CYAN
        )
        console.print(last_line)
