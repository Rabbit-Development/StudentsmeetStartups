import datetime
from flask import url_for
from restforum import db
from passlib.apps import custom_app_context as pwd_context

class User(db.Document):
    name = db.StringField(required=True)
    email = db.StringField(required=True, unique=True)
    password = db.StringField(required=True)
    location = db.StringField(required=True)
    description = db.StringField(required=True)
    resume_filename = db.StringField(required=True)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3

    def verify_password(self, password):
        return pwd_context.verify(password, self.password)

    def hash_password(self, password):
        return pwd_context.encrypt(password)