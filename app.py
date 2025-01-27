"""a"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    """a"""
    return render_template('home.html')

@app.route('/about')
def about():
    """a"""
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)
