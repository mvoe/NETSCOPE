import requests
from rich.console import Console
from rich.table import Table

console = Console()

def ip_geolocation(target):
    try:
        response = requests.get(f"https://ipinfo.io/{target}/json")
        if response.status_code == 200:
            data = response.json()
            ip_address = data.get('ip', target)
            hostname = data.get('hostname', 'Unknown')
            city = data.get('city', 'Unknown')
            region = data.get('region', 'Unknown')
            country = data.get('country', 'Unknown')
            loc = data.get('loc', 'Unknown')
            org = data.get('org', 'Unknown')
            postal = data.get('postal', 'Unknown')
            timezone = data.get('timezone', 'Unknown')

            table = Table(title=f"IP Geolocation for {ip_address}", style="cyan")
            table.add_column("Field", style="magenta", justify="right")
            table.add_column("Value", style="blue")
            table.add_row("IP Address", ip_address)
            table.add_row("Hostname", hostname)
            table.add_row("City", city)
            table.add_row("Region", region)
            table.add_row("Country", country)
            table.add_row("Location (Lat, Long)", loc)
            table.add_row("Postal Code", postal)
            table.add_row("Time Zone", timezone)
            table.add_row("Organization", org)
            console.print(table)
        else:
            console.print(f"Error: Unable to fetch data for IP {target}. Response code: {response.status_code}",
                          style="bold red")
    except requests.RequestException as e:
        console.print(f"Network error: {e}", style="bold red")
    except Exception as e:
        console.print(f"An unexpected error occurred: {e}", style="bold red")
