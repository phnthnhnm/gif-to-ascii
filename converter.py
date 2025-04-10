from PIL import Image


class GIFToASCIIConverter:
    def __init__(self, gif_path):
        self.gif_path = gif_path
        self.frames = self.load_gif_frames()

    def load_gif_frames(self):
        frames = []
        with Image.open(self.gif_path) as img:
            for frame in range(img.n_frames):
                img.seek(frame)
                frames.append(img.copy())
        return frames

    def convert_frame_to_ascii(self, frame, width=100):
        frame = frame.convert("L")  # Convert to grayscale
        aspect_ratio = frame.height / frame.width
        new_height = int(aspect_ratio * width * 0.55)  # Adjust height based on aspect ratio
        frame = frame.resize((width, new_height))

        pixels = frame.getdata()
        ASCII_CHARS = "@%#*+=-:. "
        scale_factor = 256 // len(ASCII_CHARS)  # Calculate scale factor for mapping
        ascii_str = ''.join([ASCII_CHARS[min(pixel // scale_factor, len(ASCII_CHARS) - 1)] for pixel in pixels])  # Map pixels to ASCII
        ascii_lines = [ascii_str[i:i + width] for i in range(0, len(ascii_str), width)]  # Wrap lines
        return '\n'.join(ascii_lines)

    def convert_to_ascii(self):
        ascii_frames = []
        for frame in self.frames:
            ascii_frame = self.convert_frame_to_ascii(frame)
            ascii_frames.append(ascii_frame)
        return ascii_frames

    def display_ascii_animation(self, ascii_frames, delay=0.1):
        import os
        import time
        for frame in ascii_frames:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(frame)
            time.sleep(delay)
