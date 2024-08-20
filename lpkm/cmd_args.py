import argparse


parser = argparse.ArgumentParser(
    prog="lpkm",
    description="LFS Package Manager",
)
subparser = parser.add_subparsers(dest="command")


# Sub Commands
install_command = subparser.add_parser("source-install", help="INSTAL HELP")


# "install" sub command
install_command.add_argument(
    "...", nargs="*", help='"lpkm source-install foo1 foo2 foo3"'
)
install_command.add_argument("-v", "--verbose", help="verbose", action="store_true")


parser.add_argument("-v", "--verbose", action="store_true")
parser.add_argument("--version", action="store_true")


args = parser.parse_args()
