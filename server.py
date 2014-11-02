from flask import Flask
from flask.ext.mako import MakoTemplates
from flask.ext.mako import render_template
from flask import request
app = Flask(__name__)
mako = MakoTemplates(app)

from PCCharacter import *
pc = PCCharacter()

@app.route('/')
def index():
    global pc


    data = {
        'classes': pc.get_class_types(),
        'races': pc.get_race_types()
    }
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.debug = True
    app.template_folder = "templates"

    print "Open the following URL in your browser: http://localhost:5000"

    app.run()