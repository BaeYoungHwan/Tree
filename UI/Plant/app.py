from flask import Flask, render_template, send_file

app = Flask(__name__)

@app.route('/A')
def SendA():
    return send_file('templates/Map_gu.html')

@app.route('/')
def Home():
    return render_template('HomePage.html')

@app.route('/Plant')
def Plant():
    return render_template('index.html')

@app.route('/Dong')
def Dong():
    return render_template('Dong.html')


@app.route('/Menut')
def Menu():
    return render_template('Plant.html')

@app.route('/Menur')
def Menu1():
    return render_template('Dongr.html')

@app.route('/ii')
def inner():
    return render_template('inner.html')


if __name__ == '__main__':
    app.run()
