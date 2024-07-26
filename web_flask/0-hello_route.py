# web_flask/0-hello_route.py
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/')
def hello():
    """Displays 'Hello HBNB!'"""
    return 'Hello HBNB!'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
    
