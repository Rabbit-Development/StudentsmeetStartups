from restforum import controller, login_manager as lm
from restforum.models import *
from flask import request, abort, make_response, g
from flask.ext.login import login_user, login_required, current_user, logout_user
from mongoengine.errors import ValidationError
import json, datetime

@controller.before_request
def before_request():
	g.user = current_user

@controller.route("/login", methods = ['POST'])
def login():
	email = request.json.get('email')
	password = request.json.get('password')
	if email != None and password != None:
		print('Have required data!')
		print('email:' + email)
		print('password' + password)
		print('Finds user...')
		user = User.objects.filter(email=email).first()
		if user is not None:
			print('Found user!')
			print('Verifies password...')
			if user.verify_password(password):
				print('Password verified!')
				print('Logging in user...')
				loggedin = login_user(user)
				print('User logged in!')
				return make_response("logged in")
			else :
				print('Wrong password aborting...')
				abort(401)
		else:
			print('Did not find user...')
			abort(401)
	else:
		print('Missing data...')
		abort(400)

@controller.route("/register", methods = ['POST'])
def register():
	print('Starting request for creating a new user...')
	name = request.form['name']
	email = request.form['email']
	password = request.form['password']
	location = request.form['location']
	description = request.form['description']
	if email == None or password == None or name == None or location == None and 'resume' in request.files:
		print('Missing required data!')
		print('Aborting request!')
		return abort(400)
	else:
		print('Have required data!')
		print('Checking for duplicates...')
		if User.objects.filter(email=email).first() is None:
			print('No duplicates!')
			print('Creating new user...')
			user = User(email=email,
				name=name,
				location=location,
				description=description,
				resume_filename=fileUpload(request.files['resume'])
				)
			pwd = user.hash_password(password)
			user.password = pwd
			user.save()
			print('User created!')
			return make_response("User registered")
		else: 
			print('Tried to create an allready existing user!')
			print('Aborting request!')
			return abort(400)

@controller.route("/logout", methods=['GET'])
@login_required
def logout():
    logout_user()
    return make_response("logged out")