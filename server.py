from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    from PCCharacter import *
    pc = PCCharacter()

    app.debug = True
    app.template_folder = "templates"

    print "Open the following URL in your browser: http://localhost:5000"

    app.run()