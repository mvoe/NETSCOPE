import subprocess
from rich.console import Console
from datetime import datetime

console = Console()

def performing_traceroute(target_ip):
    try:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        console.print(f"Performing traceroute to [bold]{target_ip}[/bold]", style='magenta')
        console.print(f"Traceroute initiated at [bold]{current_time}[/bold]", style='magenta')
        result = subprocess.run(['traceroute', '-w', '1', '-m', '30', target_ip], capture_output=True, text=True)
        console.print(result.stdout, style='green')
    except Exception as e:
        console.print(f"An error occurred: {e}", style="bold red")


