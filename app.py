# dep
from flask import Flask

# Create new flask instance
app = Flask(__name__)

# root
@app.route('/')
def hello_world():
    return 'Hello world'

    
