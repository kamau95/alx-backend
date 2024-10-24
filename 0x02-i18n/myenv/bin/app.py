from flask import Flask
app = Flask(__name__)
@app.route('/')
def page():
  return "hio ndio mzazi"
