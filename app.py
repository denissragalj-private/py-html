from flask import Flask

# 1. korak - kreiranje web aplikacije

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Dobro došli u Flask web aplikaciju.</h1>'  # ovo ne želimo ovako raditi

@app.route('/about-us')
def about_us():
    return '<h2>About us u Flask web aplikaciju.</h2>'  # ovo ne želimo ovako raditi


if __name__ == '__main__':
    app.run(debug=True)