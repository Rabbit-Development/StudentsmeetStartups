import os
from flask import Flask, render_template, make_response
from flask.ext import assets
from flask.ext.mongoengine import MongoEngine
from flask.ext.login import LoginManager

controller = Flask(__name__)
controller.config.from_pyfile('config.cfg')
db = MongoEngine(controller)
login_manager = LoginManager()
login_manager.init_app(controller)


controller.config['SECRET_KEY'] = os.urandom(128)
controller.config['UPLOAD_FOLDER'] = '/resumes'

ALLOWED_EXTENSIONS = set(['pdf'])


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
        'angular-scrollto/angular-scrollto.js',
        #filters='jsmin',
        output='studentsmeetstartups-script.js'
    )
)

env.register(
    'studentsmeetstartups-style',
    assets.Bundle(
        'bootstrap/dist/css/bootstrap.min.css',
        'home.css',
        #filters='cssmin',
        output='studentsmeetstartups-style.css'
    )
)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1] in ALLOWED_EXTENSIONS

def fileupload(file):
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return filename

@controller.route("/")
def index():
    return render_template('signup-template.html')

@controller.route("/browse")
def browse():
    return make_response('Browsing')

@login_manager.user_loader
def load_user(userid):
    return User.objects.filter(id=userid).first()

from restforum.models import User
from restforum import api

if __name__ == '__main__':
    controller.run()