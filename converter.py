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
        frame = frame.convert("L")
        aspect_ratio = frame.height / frame.width
        new_height = int(aspect_ratio * width * 0.55)
        frame = frame.resize((width, new_height))
        
        pixels = frame.getdata()
        ascii_str = ''.join(['@' if pixel < 128 else ' ' for pixel in pixels])
        return ascii_str

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
