from cli import parse_arguments
from converter import GIFToASCIIConverter


def main():
    args = parse_arguments()
    converter = GIFToASCIIConverter(args.gif_file)
    ascii_frames = converter.convert_to_ascii()
    converter.display_ascii_animation(ascii_frames)


if __name__ == "__main__":
    main()
