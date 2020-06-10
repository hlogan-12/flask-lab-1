from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
   "https://media2.giphy.com/media/Ibs7VZPIrzW6rIgtFV/giphy.gif?cid=ecf05e47823d8ebd7d86439769cbf7c3bf10adcc8ef1da66&rid=giphy.gif",
   "https://i.giphy.com/media/wW95fEq09hOI8/200.webp"
    ]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
