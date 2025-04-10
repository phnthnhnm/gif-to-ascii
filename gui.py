import tkinter as tk
from tkinter import filedialog, messagebox
from converter import GIFToASCIIConverter

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("GIF files", "*.gif")])
    if file_path:
        gif_path.set(file_path)

def save_ascii():
    if not gif_path.get():
        messagebox.showerror("Error", "Please select a GIF file first.")
        return

    converter = GIFToASCIIConverter(gif_path.get())
    ascii_frames = converter.convert_to_ascii()

    output_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if output_path:
        with open(output_path, 'w') as output_file:
            for frame in ascii_frames:
                output_file.write(frame + '\n\n')
        messagebox.showinfo("Success", f"ASCII art saved to {output_path}")

def display_ascii():
    if not gif_path.get():
        messagebox.showerror("Error", "Please select a GIF file first.")
        return

    converter = GIFToASCIIConverter(gif_path.get())
    ascii_frames = converter.convert_to_ascii()
    converter.display_ascii_animation(ascii_frames)

# Create the main window
root = tk.Tk()
root.title("GIF to ASCII Converter")

# Variables
gif_path = tk.StringVar()

# Layout
tk.Label(root, text="GIF File:").grid(row=0, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=gif_path, width=40).grid(row=0, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=open_file).grid(row=0, column=2, padx=10, pady=10)

tk.Button(root, text="Display ASCII", command=display_ascii).grid(row=1, column=0, columnspan=2, pady=10)
tk.Button(root, text="Save ASCII", command=save_ascii).grid(row=1, column=2, pady=10)

# Run the application
root.mainloop()
