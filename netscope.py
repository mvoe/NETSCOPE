from textwrap import dedent
from rich.console import Console
from modules.header import print_logo, print_separator, display_menu
from modules.argparser import ArgumentParser
from modules.portscan import port_scan
from  modules.traceroute import performing_traceroute
from modules.ping import ping_test
from modules.dnslookup import dns_lookup
from modules.whois_lookup import perform_whoislookup
from modules.reverseDNSLookUp import reverse_dns_lookup
from modules.ipgeolocation import ip_geolocation
from modules.sslcertificatecheck import ssl_certificate_check
from modules.subdomainscanning import get_subdomain


console = Console()

def main():
    parser = ArgumentParser.get_parser()
    args = parser.parse_args()

    if args.options:
        display_menu()
    elif args.portscan:
        port_scan(args.portscan)
    elif args.traceroute:
        performing_traceroute(args.traceroute)
    elif args.ping:
        ping_test(args.ping)
    elif args.dnslookup:
        dns_lookup(args.dnslookup)
    elif args.whois:
      perform_whoislookup(args.whois)
    elif args.reversedns:
      reverse_dns_lookup(args.reversedns)
    elif args.ipgeolocation:
      ip_geolocation(args.ipgeolocation)
    elif args.sslcheck:
        ssl_certificate_check(args.sslcheck)
    elif args.subdomainscan:
        get_subdomain(args.subdomainscan)
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
