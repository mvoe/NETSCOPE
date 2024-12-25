import dns.resolver
from rich.console import Console
from rich.table import Table

console = Console()

subdomain_list = [
    "www", "mail", "api", "ftp", "dev", "shop", "staging", "blog", "secure", "m", "vpn", "test",
    "admin", "dns", "monitor", "intranet", "webmail", "support", "portal", "files", "store", "cloud",
    "apps", "partners", "cpanel", "demo", "help", "remote", "mymail", "web", "mobile", "dashboard",
    "login", "registration", "db", "sql", "mysql", "phpmyadmin", "pgadmin", "mongo", "redis", "adminer",
    "database", "reports", "metrics", "backup", "cluster", "sequel", "query", "logs"
]

def get_subdomain(domain):
    subdomains_found = []

    for subdomain in subdomain_list:
        fqdn = f"{subdomain}.{domain}"
        try:
            dns.resolver.resolve(fqdn, "A")
            subdomains_found.append(fqdn)
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
            pass

    if subdomains_found:
        table = Table(title=f"Found Subdomains for {domain}", style="cyan")
        table.add_column("Subdomain", style="magenta", justify="right")
        for subdomain in subdomains_found:
            table.add_row(subdomain)
        console.print(table)
    else:
        console.print(f"No subdomains found for {domain}.", style="bold red")


