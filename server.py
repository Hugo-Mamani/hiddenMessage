from flask import Flask

app = Flask(__name__)

@app.route('/')
def root():
    return "hidden messages"

app.run(port=2317, debug=True)
