from typing import Text
from flask import Flask, render_template
from werkzeug.exceptions import RequestURITooLarge
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('words.html')
Text

@app.route("/anagrams/<word>")

def anagrams(word):
    word = word.upper()
    f = open('words.txt')
    words = f.read().splitlines()

    anagrams = []

    for w in words:
        if sorted(w) == sorted(word):
            anagrams.append(w)

    return render_template('words.html', word_list=anagrams)
