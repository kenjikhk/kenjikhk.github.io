from typing import Text
from flask import Flask, render_template
from werkzeug.exceptions import RequestURITooLarge
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('mainpage.html')
Text

@app.route('/fizzbuzz/<int:upto>')
def fizzbuzz(upto):
    l = []

    
    for n in range(1,upto+1):

        if n % 3 == 0 and n % 5 == 0:
            l.append("fizzbuzz")
        
        elif n % 3 == 0:
            l.append("fizz")
        
        elif n % 5 == 0:
            l.append("buzz")
        else:
            l.append(n)
    
    return render_template('fizzbuzz.html',l=l)
