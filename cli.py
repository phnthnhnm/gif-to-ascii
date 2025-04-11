import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Convert GIF files to animated ASCII art."
    )
    parser.add_argument(
        "gif_file", type=str, nargs="?", help="Path to the input GIF file"
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        default="output.txt",
        help="Output file for ASCII art",
    )
    parser.add_argument(
        "-gui", action="store_true", help="Launch the GUI for the application"
    )
    args = parser.parse_args()
    if not args.gui and not args.gif_file:
        parser.error(
            "the following arguments are required unless -gui is specified: gif_file"
        )
    return args
