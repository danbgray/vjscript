from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import nltk
from nltk.corpus import cmudict

app = Flask(__name__)
CORS(app)

# Ensure you have downloaded the cmudict corpus
nltk.download('cmudict')

# Load the CMU Pronouncing Dictionary
cmu_dict = cmudict.dict()

# Define the VJScript mapping for vowels and consonants
vowel_mapping = {
    'IY': 'EE', 'IH': 'I', 'EY': 'EI', 'EH': 'E', 'AE': 'AE', 'AA': 'AW',
    'AO': 'OA', 'OW': 'OW', 'UH': 'Ø', 'UW': 'O', 'AH': 'U', 'AY': 'AI',
    'AW': 'OW', 'OY': 'OY', 'ER': 'ER'
}

consonant_mapping = {
    'K': 'K', 'G': 'G', 'NG': 'NG', 'CH': 'CH', 'JH': 'J', 'T': 'T',
    'TH': 'TH', 'D': 'D', 'N': 'N', 'P': 'P', 'B': 'B', 'F': 'F',
    'M': 'M', 'Y': 'Y', 'R': 'R', 'L': 'L', 'V': 'V', 'S': 'S',
    'Z': 'Z', 'SH': 'SH', 'ZH': 'ZH'
}

def get_phonetic_transcription(word):
    """ Get the ARPAbet phonetic transcription of a word. """
    word = word.lower()
    if word in cmu_dict:
        return cmu_dict[word][0]  # Return the first pronunciation variant
    else:
        # Fallback if the word is not found
        return list(word)

def map_phoneme(phoneme):
    """ Map ARPAbet phonemes to VJScript phonemes """
    phoneme = phoneme.strip("012")  # Remove any stress markers like 0, 1, 2
    if phoneme in vowel_mapping:
        return vowel_mapping[phoneme]
    for consonant in consonant_mapping:
        if phoneme.startswith(consonant):
            return consonant_mapping[consonant]
    return phoneme

def format_vjscript(word):
    """ Format the word into VJScript style """
    phonetic_word = get_phonetic_transcription(word)
    mapped_word = [map_phoneme(p) for p in phonetic_word]

    result = ''
    current_consonant = ''
    current_vowel = ''

    for char in mapped_word:
        if char in consonant_mapping.values():
            if current_consonant:
                result += wrap_consonant(current_consonant, current_vowel)
            current_consonant = char
            current_vowel = ''
        elif char in vowel_mapping.values():
            if current_consonant:
                current_vowel = char
            else:
                result += char  # Initial vowel, just add to result
        else:
            result += char  # Non-alphabetical character, just add to result

    if current_consonant:
        result += wrap_consonant(current_consonant, current_vowel)

    return result

def wrap_consonant(consonant, vowel):
    """ Wrap consonant and vowel in HTML for VJScript styling """
    wrapped = f'<span class="consonant">{consonant}'
    if vowel:
        wrapped += f'<span class="vowel">{vowel}</span>'
    wrapped += '</span>'
    return wrapped

def translate_text(text):
    """ Translate a text to VJScript style """
    words = text.split()
    translated_words = [format_vjscript(word) for word in words]
    return ' '.join(translated_words)

@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()
    text = data.get('text', '')
    translated_text = translate_text(text)
    return jsonify({ 'translated_text': translated_text })

if __name__ == "__main__":
    app.run(debug=True)
