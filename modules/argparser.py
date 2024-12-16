import argparse

class ArgumentParser:

    @staticmethod
    def get_parser():
        parser = argparse.ArgumentParser(
            description="NetScope - Network Analysis Tool",
            formatter_class = argparse.RawTextHelpFormatter
        )

        parser.add_argument(
            '-v', '--version',
            action='version',
            version='NetScope 1.0',
            help='Show the version of the program and exit'
        )

        parser.add_argument(
            '-o', '--options',
            action='store_true',
            help='Display the menu options'
        )

        parser.add_argument(
            '-p', '--portscan',
            type=str,
            help= (
                "Perform a comprehensive port scan on the specified target. This will scan all valid ports (from 1 to 65535) on the given IP address or domain name. "
                "For example, use: 'python3 netscope.py -p <target>' to initiate the scan. The scan will check for open ports and attempt to identify the associated services. "
                "The results will be displayed with port numbers and service names, if available."
            )
        )

        parser.add_argument(
            '-t', '--traceroute',
            type=str,
            help="Perform traceroute to the specified IP address or hostname"
        )

        parser.add_argument(
            '-ping',
            type=str,
            help="Hostname or IP address to ping"
        )

        parser.add_argument(
            '-dns', '--dnslookup',
            type=str,
            help="Perform DNS lookup for the given hostname or IP address"
        )
        parser.add_argument(
            '-who', '--whois',
            type=str,
            help="Perform WHOIS lookup for the given hostname or IP address"
        )

        return parser