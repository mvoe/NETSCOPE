import whois
from rich.console import Console
from datetime import datetime

console = Console()

def perform_whoislookup(target):
    try:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        console.print(f"Performing WHOIS lookup for [bold]{target}[/bold]", style='magenta')
        console.print(f"WHOIS Lookup initiated at [bold]{current_time}[/bold]", style='magenta')
        result = whois.whois(target)
        console.print(result, style='green')
    except Exception as e:
        console.print(f"An error occurred: {e}", style="bold red")