"""Main module for the Raspberry Pi MOTD."""

import argparse
import sys

from blessings import Terminal
from pyfiglet import Figlet


def main(argv):
    """Entry point."""
    parser = argparse.ArgumentParser(description="Raspberry Pi MOTD")
    parser.add_argument("hostname", help="The host name")
    parser.add_argument("model", help="The model name")
    parser.add_argument("-o", "--output-file")

    args = parser.parse_args(argv)

    output_file = args.output_file
    if output_file is None:
        fh = sys.stdout
    else:
        fh = open(output_file, "w")

    print(create_motd(args.hostname, args.model), file=fh)



def create_motd(hostname: str, model: str) -> str:
    """Creates the MOTD string."""
    logo = raspberry_pi_logo()
    hostname = figlet_hostname(hostname)
    model = formatted_model_name(model)

    # the rhs is the model name and hostname
    rhs = [model, *hostname]

    # combine lhs and rhs
    rhs_top = ((len(logo) - len(rhs)) // 2) + 1
    for i, line in enumerate(rhs):
        logo[i + rhs_top] += line

    return "\n".join(logo)


def raspberry_pi_logo() -> list[str]:
    """Returns an array of lines that make up the Raspberry Pi logo, including color codes."""
    t = Terminal()
    g = t.bold_green
    r = t.bold_red

    return [
        g(r"    .~~.   .~~.     "),
        g(r"   '. \ ' ' / .'    "),
        r(r"    .~ .~~~..~.     "),
        r(r"   : .~.'~'.~. :    "),
        r(r"  ~ (   ) (   ) ~   "),
        r(r" ( : '~'.~.'~' : )  "),
        r(r"  ~ .~ (   ) ~. ~   "),
        r(r"   (  : '~' :  )    "),
        r(r"    '~ .~~~. ~'     "),
        r(r"        '~'         "),
    ]


def figlet_hostname(hostname: str) -> str:
    """Returns the hostname in a formatted string."""
    f = Figlet()
    t = Terminal()

    lines = f.renderText(hostname).splitlines()
    return [t.bold_blue(line) for line in lines]


def formatted_model_name(model: str) -> str:
    """Returns the model name in a formatted string."""
    t = Terminal()
    return t.bold_white(model)


if __name__ == "__main__":
    main(sys.argv[1:])
