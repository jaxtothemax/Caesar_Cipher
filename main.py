from flask import Flask, render_template, request, redirect, url_for
from app import rot

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/text', methods=['GET', 'POST'])
def text(comments=[]):
    if request.method == "GET":
        return render_template("index.html", comments=comments)
    comments.append(request.form["text_input"])
    return redirect(url_for('text'))


# New endpoint that returns the cc result and takes in a string and rot_x

@app.route('/cipher', methods=['GET'])
def cipher():
    value = request.args.get('value')
    rot_x = request.args.get('rot_x')
    return rot(value, rot_x)


if __name__ == '__main__':
    app.run(debug=True)

# js file that calls that endpoint on input.change and updates the result field

