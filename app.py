from flask import Flask , render_template, request
import nltk
import string
from nltk import FreqDist

nltk.download('punkt')
app = Flask(__name__)

@app.route("/")
def index():
     return render_template('userinput.html')

@app.route('/nlpoutput' , methods = ['post'])
def calculate():
    paragraph = request.form.get('paragraph')
    punct  = string.punctuation
    chars= len(paragraph)
    sentlist = nltk.sent_tokenize(paragraph)
    sent = len(sentlist)
    clean_word = [word for word in nltk.word_tokenize(paragraph) if word not in punct]
    words = len(clean_word)
    freq = FreqDist(clean_word)
    return render_template('calculate.html' , predict = f'The number of words is {words}. The words are {clean_word}. The number of sentences are {sent}. The sentences are {sentlist}. The number of characters are {chars}. Frequency distribution of Words is {freq.items()}')

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)