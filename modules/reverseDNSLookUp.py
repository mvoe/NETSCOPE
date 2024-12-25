import socket
from rich.console import Console
from datetime import datetime

console = Console()


def reverse_dns_lookup(hostname):
    try:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if hostname.replace('.', '').isdigit():
            domain = socket.gethostbyaddr(hostname)
            console.print(f"\n[bold magenta]Reverse DNS Lookup[/bold magenta]")
            console.print(f"  [bold]IP Address:[/bold] {hostname}")
            console.print(f"  [bold]Hostname:[/bold] {domain[0]}")
            console.print(f"  [bold]Lookup Time:[/bold] {current_time}\n", style="cyan")
        else:
            ip_addresses = socket.gethostbyname_ex(hostname)[2]
            console.print(f"\n[bold magenta]DNS Lookup[/bold magenta]")
            console.print(f"  [bold]Hostname:[/bold] {hostname}")
            console.print(f"  [bold]IP Addresses:[/bold]")
            for ip in ip_addresses:
                console.print(f"    - {ip}", style="cyan")
            console.print(f"  [bold]Lookup Time:[/bold] {current_time}\n", style="cyan")
    except socket.herror as e:
        console.print(f"[bold red]Error:[/bold] Unable to resolve the host - {e}")
    except socket.gaierror as e:
        console.print(f"[bold red]Error:[/bold] Invalid hostname or IP address - {e}")
    except Exception as e:
        console.print(f"[bold red]Error:[/bold] An unexpected error occurred - {e}")
