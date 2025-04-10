# gif-to-ascii

This project converts GIF files into animated ASCII art. It provides both a command-line interface (CLI) and a graphical user interface (GUI) for users to interact with the tool. The ASCII art can be displayed in the terminal or saved to a text file.

## Features

- Convert GIFs to animated ASCII art.
- Display ASCII art in the terminal or a GUI window.
- Save ASCII art to a text file.

## Requirements

- Python 3.6 or higher
- Required Python libraries: `Pillow`

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/phnthnhnm/gif-to-ascii.git
   cd gif-to-ascii
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Command-Line Interface (CLI)

To convert a GIF to ASCII art and display it in the terminal:

```bash
python main.py <path_to_gif>
```

To save the ASCII art to a text file:

```bash
python main.py <path_to_gif> -o <output_file>
```

### Graphical User Interface (GUI)

1. Run the following command to open the GUI:

   ```bash
   python main.py -gui
   ```

2. Use the "Browse" button to select a GIF file.
3. Click "Display ASCII" to view the animated ASCII art in a new window.
4. Click "Save ASCII" to save the ASCII art to a text file.

## How to Contribute

1. Fork the repository.
2. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature-name
   ```
3. Make your changes and commit them:
   ```bash
   git commit -m "Description of changes"
   ```
4. Push your changes to your fork:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request on the main repository.
