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

    # Create a new window to display ASCII art
    ascii_window = tk.Toplevel(root)
    ascii_window.title("ASCII Art Viewer")
    ascii_window.geometry("800x600")

    text_widget = tk.Text(ascii_window, wrap="none", font=("Courier", 8))
    text_widget.pack(expand=True, fill="both")

    def animate(index=0):
        if index < len(ascii_frames):
            text_widget.config(state="normal")
            text_widget.delete("1.0", "end")
            text_widget.insert("end", ascii_frames[index])
            text_widget.config(state="disabled")
            ascii_window.after(100, animate, index + 1)
        else:
            ascii_window.after(100, animate, 0)  # Loop back to the first frame

    animate()

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
