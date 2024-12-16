import subprocess
from rich.console import Console
from datetime import datetime

console = Console()

def ping_test(target):
    try:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        console.print(f"Performing ping test to [bold]{target}[/bold]", style='magenta')
        console.print(f"Ping initiated at [bold]{current_time}[/bold]", style='magenta')

        result = subprocess.run(['ping', '-c', '4', target], capture_output=True, text=True)

        console.print(result.stdout, style='green')
    except Exception as e:
        console.print(f"An error occurred: {e}", style="bold red")
