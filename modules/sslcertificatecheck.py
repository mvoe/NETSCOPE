import requests
from rich.console import Console
from rich.table import Table

console = Console()


def ssl_certificate_check(url):
    try:
        api_url = f"https://api.ssllabs.com/api/v3/analyze?host={url}"
        response = requests.get(api_url)

        if response.status_code == 200:
            ssl_info = response.json()

            if ssl_info.get('status') == 'READY':
                endpoints = ssl_info.get('endpoints', [])

                if endpoints:
                    ip_address = endpoints[0].get('ipAddress', 'Unknown')
                    server_name = endpoints[0].get('serverName', 'Unknown')
                    grade = endpoints[0].get('grade', 'Unknown')
                    status_message = endpoints[0].get('statusMessage', 'Unknown')
                    protocol = ssl_info.get('protocol', 'Unknown')

                    table = Table(title=f"SSL Certificate Information for {url}", style="cyan")
                    table.add_column("Field", style="magenta", justify="right")
                    table.add_column("Value", style="blue")

                    table.add_row("Server Name", server_name)
                    table.add_row("IP Address", ip_address)
                    table.add_row("SSL Grade", grade)
                    table.add_row("Status Message", status_message)
                    table.add_row("Protocol", protocol)

                    console.print(table)
                else:
                    console.print(f"No endpoints found for {url}.", style="bold red")
            else:
                console.print(f"Error: SSL analysis for {url} is not ready yet. Status: {ssl_info.get('status')}",
                              style="bold red")
        else:
            console.print(f"Error: Unable to fetch SSL data for {url}. Response code: {response.status_code}",
                          style="bold red")

    except requests.RequestException as e:
        console.print(f"Network error: {e}", style="bold red")
    except Exception as e:
        console.print(f"An unexpected error occurred: {e}", style="bold red")
