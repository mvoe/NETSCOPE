from textwrap import dedent
from rich.console import Console
from rich.text import Text
from modules.header import print_logo, print_separator, print_menu_option
from modules.argparser import ArgumentParser


console = Console()

def main():
    parser = ArgumentParser.get_parser()
    args = parser.parse_args()

    if args.options:
        print_menu_option()
    else:
        print_logo()
        print_separator()
        console.print(
            dedent(
                """\nTo view all available features, please use one of the following commands: [bold]python3 netscope.py -h[/bold] or [bold]python3 netscope.py --help[/bold].\n"""
            ),
            style="magenta"
        )
        print_separator()
if __name__ == "__main__":
    main()
