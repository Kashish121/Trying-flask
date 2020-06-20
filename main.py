import logging

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')

def homepage():
    return render_template('index.html')

@app.route('/input', methods=["POST"])

def input():
    if request.method == "POST":
        # val = request.form["val"]
        host = request.form["host"]
        range_low = request.form["range_low"]
        range_high = request.form["range_high"]
        # host = "localhost"
        # range_low = "43"
        # range_high = "66"
        return render_template('index.html', host=host, range_low=range_low, range_high=range_high)
        # return redirect(url_for('input'))
        # return '%s %s %s' %(host, range_low, range_high)
    return render_template('index.html')


if __name__ == '__main__':
	app.run(debug=True)