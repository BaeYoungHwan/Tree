from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/Color/Dong')
def hello_world():
    return render_template('test.html')

@app.route('/Color/Location')
@app.route('/Color')
def Color():
    return render_template('Color.html')

@app.route('/Plant')
def Plant():
    return render_template('Plant.html')

@app.route('/Recommend')
def Recoomend():
    return render_template('Recommend.html')

@app.route('/')
def Hi():
    return render_template('Design.html')


@app.route('/Plnat/Report')
@app.route('/Color/Report')
@app.route('/Report')
def Report():
    return render_template('Report.html')

if __name__ == '__main__':
    app.run()
