from flask import Flask

# 1. korak - kreiranje Flask web aplikacije
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Dobro dosli u Flask web demo aplikaciju.</h1>'


@app.route('/about-us')
def about_us():
    return '<h2>About us u Flask web demo aplikaciji.</h2>'


@app.route('/hello/<name>')
def hello (name):
    return f'Pozdrav, {name}!'


@app.route('/sqrt/<int:number>')
def sqrt (number):
    return f'Kvadrat {number} je {number ** 2}!'



if __name__ == '__main__':
    app.run(debug=True)
