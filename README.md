# VJScript Translator

This project is a VJScript Translator that uses Flask for the backend and a simple HTML/JavaScript frontend to provide real-time translation of English text into VJScript. The translation is based on phonetic mapping using the CMU Pronouncing Dictionary from the NLTK library.

## Features

- Real-time translation of English text into VJScript
- Phonetic mapping using the CMU Pronouncing Dictionary
- Simple and self-contained application

## Getting Started

### Prerequisites

- Python 3.x
- Replit account (optional, but recommended for easy setup)

### Installation

1. **Clone the repository** or download the files.

    ```bash
    git clone https://github.com/yourusername/vjscript-translator.git
    cd vjscript-translator
    ```

2. **Install the required Python libraries**.

    ```bash
    pip install flask flask-cors nltk
    ```

3. **Download the CMU Pronouncing Dictionary**.

    ```python
    import nltk
    nltk.download('cmudict')
    ```

### Running the Application

#### Locally

1. **Run the Flask server**.

    ```bash
    python main.py
    ```

2. **Open your web browser** and go to `http://127.0.0.1:5000`.

#### On Replit

1. **Create a new Replit project** and select "Import from GitHub".

2. **Paste the URL of your repository**.

3. **Ensure the main file is named `main.py`**.

4. **Create an `index.html` file** in the root directory and paste the contents of the `index.html` provided.

5. **Add a `.replit` file** in the root directory with the following content to specify the entry point for the project:

    ```plaintext
    run = "python main.py"
    ```

6. **Click the "Run" button** in Replit.

7. **Open the webview** to interact with the application.

### Project Structure
vjscript-translator/
│
├── index.html # Frontend HTML file
├── main.py # Backend Flask server
├── README.md # Project documentation
└── .replit # Replit configuration file


### How It Works

1. The **Flask server** handles POST requests to the `/translate` endpoint.
2. It uses the **NLTK CMU Pronouncing Dictionary** to get phonetic transcriptions.
3. The server **maps phonemes** correctly without hardcoding special cases.
4. It **formats the text** in the VJScript style and returns the translated text.
5. The **HTML and JavaScript** frontend includes a textarea for input and a div for output.
6. JavaScript **listens for input events** on the textarea and sends the text to the Flask server.
7. The server's response is displayed in the output div, **updating in real-time** as you type.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Acknowledgments

- The CMU Pronouncing Dictionary used for phonetic transcription.
- Inspiration for VJScript from [VJScript by Vijay Kiran Kethanaboyina](https://www.vkethana.com/vjscript/).

## Contact

For any inquiries or feedback, please contact [dbgray](x.com/dbgray).
