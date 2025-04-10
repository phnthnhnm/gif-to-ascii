from cli import parse_arguments
from converter import GIFToASCIIConverter


def main():
    args = parse_arguments()
    converter = GIFToASCIIConverter(args.gif_file)
    ascii_frames = converter.convert_to_ascii()
    converter.display_ascii_animation(ascii_frames)
    
    with open(args.output, 'w') as output_file:
        for frame in ascii_frames:
            output_file.write(frame + '\n\n')


if __name__ == "__main__":
    main()
