from flask import Flask, request, jsonify, render_template
app = Flask(__name__)

# A welcome message to test our server
@app.route('/')
def index():
    return render_template('indexProduction.html')