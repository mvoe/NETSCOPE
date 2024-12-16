import socket
from concurrent.futures import ThreadPoolExecutor, as_completed
from rich.console import Console
from datetime import datetime

console = Console()

def scan_port(target_ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.5)
            result = sock.connect_ex((target_ip, port))
            if result == 0:
                try:
                    service_name = socket.getservbyport(port, 'tcp')
                except OSError:
                    service_name = None
                return (port, 'open', service_name)
            return (port, 'closed', None)
    except Exception as e:
        console.print(f"Error scanning port {port}: {e}", style="bold red")
        return (port, 'error', None)

def port_scan(target_ip):
    try:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        console.print(f"Scanning all valid ports on [bold]{target_ip}[/bold]", style="magenta")
        console.print(f"Port Scan initiated at [bold]{current_time}[/bold]", style='magenta')

        with ThreadPoolExecutor(max_workers=100) as executor:
            futures = [executor.submit(scan_port, target_ip, port) for port in range(1, 65536)]
            for future in as_completed(futures):
                port, status, service_name = future.result()
                if status == 'open':
                    if service_name:
                        console.print(f"{port}/TCP OPEN  {service_name}", style="green")
                    else:
                        console.print(f"{port}/TCP OPEN", style="green")
                elif status == 'error':
                    console.print(f"Error scanning port {port}", style="bold red")

    except Exception as e:
        console.print(f"An unexpected error occurred: {e}", style="bold red")