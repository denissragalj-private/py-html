from flask import Flask

# 1. korak - kreiranje Flask web aplikacije
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Dobro dosli u Flask web demo aplikaciju.</h1>'


@app.route('/about-us')               # prikaz u web pregledniku na adresi http://127.0.0.1:5000/about-us   i daje: About us u Flask web demo aplikaciji.
def about_us():
    return '<h2>About us u Flask web demo aplikaciji.</h2>'


@app.route('/hello/<name>')           # prikaz u web pregledniku na adresi http://127.0.0.1:5000/hello/Denis   i daje: Pozdrav, Denis!
def hello (name):
    return f'Pozdrav, {name}!'


@app.route('/sqrt/<int:number>')      # prikaz u web pregledniku na adresi  http://127.0.0.1:5000/sqrt/2   i daje ispis: Kvadrat 2 je 4!
def sqrt (number):
    return f'Kvadrat {number} je {number ** 2}!'



if __name__ == '__main__':
    app.run(debug=True)
