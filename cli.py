import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(description='Convert GIF files to animated ASCII art.')
    parser.add_argument('gif_file', type=str, help='Path to the input GIF file')
    parser.add_argument('-o', '--output', type=str, default='output.txt', help='Output file for ASCII art')
    return parser.parse_args()
