from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def Home():
    return render_template('Home.html')

@app.route('/Plant')
def Color():
    return render_template('Color.html')

@app.route('/Color')
@app.route('/Color/Dong')
def Plant1():
    return render_template('Dong.html')

@app.route('/Plnat/Report')
@app.route('/Color/Report')
@app.route('/Report')
def Report():
    return render_template('Report.html')

if __name__ == '__main__':
    app.run()
