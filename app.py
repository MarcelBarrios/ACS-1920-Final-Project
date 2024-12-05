from flask import Flask, render_template

app = Flask(__name__)

# Home route renders index.html


@app.route('/')
def home():
    return render_template('index.html')

# UXDesign route renders UXDesign.html


@app.route('/UXDesign')
def ux_design():
    return render_template('UXDesign.html')

# Contact route renders contact.html


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
