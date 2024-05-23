# VJScript Font Generation

This project creates a custom font for the VJScript writing system, positioning vowels above consonants using OpenType features. The font is generated from an open-source base font, DejaVu Sans.

## About VJScript

VJScript was created by Vijay Kiran Kethanaboyina, a Computer Science student at UC Berkeley. You can learn more about VJScript on his [website](https://www.vkethana.com/vjscript/).

## Prerequisites

- **Docker**: Docker is required to run the font generation script. Follow the instructions below to install Docker.

### Installing Docker

#### On macOS

1. Install Docker Desktop from the [Docker website](https://www.docker.com/products/docker-desktop).

#### On Linux

1. Install Docker using your package manager. For Debian-based distributions (like Ubuntu), use:
    ```bash
    sudo apt-get install docker.io
    ```

2. For Red Hat-based distributions (like Fedora), use:
    ```bash
    sudo dnf install docker
    ```

#### On Windows

1. Install Docker Desktop from the [Docker website](https://www.docker.com/products/docker-desktop).

## Project Setup

1. **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Download the DejaVu Sans Font**:
    - Download the DejaVu Sans font from [DejaVu Fonts](https://dejavu-fonts.github.io/).
    - Place the `DejaVuSans.ttf` file in the project directory.

3. **Build the Docker image**:
    ```bash
    docker build -t vjscript-font .
    ```

4. **Run the Docker container**:
    ```bash
    docker run --rm -v $(pwd):/app vjscript-font
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

