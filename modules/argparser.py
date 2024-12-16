import argparse

class ArgumentParser:

    @staticmethod
    def get_parser():
        parser = argparse.ArgumentParser(
            description="NetScope - Network Analysis Tool",
            formatter_class = argparse.RawTextHelpFormatter
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