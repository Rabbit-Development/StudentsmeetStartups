import os
from flask import Flask, render_template
from flask.ext import assets

controller = Flask(__name__)
env = assets.Environment(controller)

# Tell flask-assets where to look for our javascript and css files.
env.load_path = [
    os.path.join(os.path.dirname(__file__), 'css'),
    os.path.join(os.path.dirname(__file__), 'javascript'),
    os.path.join(os.path.dirname(__file__), 'bower_components')
]

env.register(
    'studentsmeetstartups-script',
    assets.Bundle(
        'jquery/dist/jquery.js',
        'angular/angular.js',
        'angular-ui-router/release/angular-ui-router.min.js',
        'angular-bootstrap/ui-bootstrap-tpls.min.js',
        'studentsmeetstartups.js',
        'angular-ui-select/dist/select.js',
        'angular-sanitize/angular-sanitize.js',
        #filters='jsmin',
        output='studentsmeetstartups-script.js'
    )
)

env.register(
    'studentsmeetstartups-style',
    assets.Bundle(
        'bootstrap/dist/css/bootstrap.min.css',
        'index.css',
        'whitebuble.css',
        #filters='cssmin',
        output='studentsmeetstartups-style.css'
    )
)

@controller.route("/")
def index():
    return render_template('index.html')

if __name__ == '__main__':
    controller.run(debug=True)