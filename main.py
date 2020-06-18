import logging

from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])

def input():
    if request.method == "POST":
        req = request.form
        host = req["host"]
        range_low = req.get("range_low")
        range_high = req.get("range_high")
        print(host, range_low, range_high)
        return redirect(request.url)
    return render_template('index.html')

# def homepage():
#     return render_template('index.html')


if __name__ == '__main__':
	app.run(debug=True)