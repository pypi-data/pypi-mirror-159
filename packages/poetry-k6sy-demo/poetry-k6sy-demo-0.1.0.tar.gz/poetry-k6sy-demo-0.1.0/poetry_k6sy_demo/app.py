from flask import Flask

app = Flask(__name__)
    
@app.route('/', methods=['GET'])
def HomePage():
    return "<h1>Flask with Poetry Demonstration</h1>"

