# VJScript Font Generation

This project creates a custom font for the VJScript writing system, positioning vowels above consonants using OpenType features. The font is generated from an open-source base font, DejaVu Sans.

## About VJScript

VJScript was created by Vijay Kiran Kethanaboyina, a Computer Science student at UC Berkeley. You can learn more about VJScript on his [website](https://www.vkethana.com/vjscript/).

## Prerequisites

- **FontForge**: FontForge is required to run the font generation script. Follow the instructions below to install FontForge.

### Installing FontForge

#### On macOS

1. Install Homebrew if you don't have it already:
    ```bash
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    ```

2. Install FontForge using Homebrew:
    ```bash
    brew install fontforge
    ```

#### On Linux

1. Install FontForge using your package manager. For Debian-based distributions (like Ubuntu), use:
    ```bash
    sudo apt-get install fontforge
    ```

2. For Red Hat-based distributions (like Fedora), use:
    ```bash
    sudo dnf install fontforge
    ```

#### On Windows

1. Download the FontForge installer from the [FontForge website](https://fontforge.org/en-US/downloads/windows/).

2. Run the installer and follow the instructions to install FontForge.

### Installing Python and FontForge-Python Bindings

1. Ensure you have Python installed. You can download it from the [Python website](https://www.python.org/).

2. Install the FontForge Python bindings:
    ```bash
    sudo apt-get install python3-fontforge
    ```

## Project Setup

1. **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Download the DejaVu Sans Font**:
    - Download the DejaVu Sans font from [DejaVu Fonts](https://dejavu-fonts.github.io/).
    - Place the `DejaVuSans.ttf` file in the project directory.

3. **Run the FontForge script**:
    ```bash
    python create_vjscript_font.py
    ```

## Script Explanation

The provided script `create_vjscript_font.py` does the following:

1. Loads the DejaVu Sans font.
2. Adds anchor points to consonants and vowels.
3. Defines OpenType features to position vowels above consonants.
4. Generates a new font file `VJScript.otf`.

## Usage

After running the script, the generated font file `VJScript.otf` can be used in your projects. Here’s how you can use it in a web page:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VJScript Font Example</title>
    <style>
        @font-face {
            font-family: 'VJScript';
            src: url('VJScript.otf') format('opentype');
        }

        body {
            font-family: 'VJScript', sans-serif;
        }
    </style>
</head>
<body>
    <h1>VJScript Font Example</h1>
    <p>Type your text here to see it in VJScript.</p>
</body>
</html>

