from flask import Flask, render_template
from cards import cards
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('/index.html')

@app.route("/examples")
def examples():
    return render_template('/examples.html')

if __name__ == "__main__":
    app.run(debug=True)
