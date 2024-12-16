import socket
from rich.console import Console
from datetime import datetime

console = Console()

def dns_lookup(hostname):
    try:
        # Check if the input is an IP address or a hostname
        if hostname.replace('.', '').isdigit():
            # Perform reverse DNS lookup
            domain = socket.gethostbyaddr(hostname)
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            console.print(f"Reverse DNS lookup for IP [bold]{hostname}[/bold]: {domain[0]}", style="bold magenta")
            console.print(f"DNS Lookup initiated at [bold]{current_time}[/bold]", style='magenta')

        else:
            # Perform normal DNS lookup
            ip_addresses = socket.gethostbyname_ex(hostname)[2]
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            console.print(f"DNS lookup for hostname {hostname}:", style='bold magenta')
            console.print(f"Scan initiated at [bold]{current_time}[/bold]", style='magenta')

            for ip in ip_addresses:
                console.print(f"  - {ip}", style="bold magenta")
    except socket.herror as e:
        console.print(f"Unable to resolve the host: {e}", style="bold red")
    except socket.gaierror as e:
        console.print(f"Invalid hostname or IP address: {e}", style="bold red")
    except Exception as e:
        console.print(f"An unexpected error occurred: {e}", style="bold red")