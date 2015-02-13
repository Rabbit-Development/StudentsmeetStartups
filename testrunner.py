import os
from restforum import controller
from restforum.models import *
from flask.ext.mongoengine import MongoEngine
from mongoengine import connect
from StringIO import StringIO
import unittest, json, datetime

class controllerTestCase(unittest.TestCase):

	
	def setUp(self):
		controller.config['MONGODB_SETTINGS'] = {
			'db':'test_db',
		}
		User.objects.delete()
		
		db = MongoEngine(controller)
		self.controller = controller.test_client()
		self.user_info = {
			'email':'user@test.com',
			'password':'password1!@',
			'name':'nick',
			'location':'testlocation',
			'resume': (StringIO('resume contents'), 'testresume.pdf')
		}

	def tearDown(self):
		db = connect('test_db')
		db.drop_database('test_db')

	def register(self):
		return self.controller.post('/register', data=self.user_info)

	def login(self):
		return self.controller.post('/login', data=json.dumps(self.user_info), headers={'content-type':'application/json'})

	def test_user_mng(self):
		"""API: Testing User Handling"""
		# Registering user
		rv = self.controller.post('/register', data=self.user_info)
		print(rv.status_code)
		assert 200 == rv.status_code
		assert "User registered" in rv.data.decode('utf-8')
		# # Duplicate 
		# rv = self.controller.post('/register', data=json.dumps({
		# 	'email':'user@test.com',
		# 	'password':'password1!@',
		# 	'username':'nick'
		# }), headers={'content-type':'application/json'})
		# assert 400 == rv.status_code
		# # Missing email
		# rv = self.controller.post('/register', data=json.dumps({
		# 	'password':'password1!@',
		# 	'username':'nick'
		# }), headers={'content-type':'application/json'})
		# assert 400 == rv.status_code
		# # Missing password
		# rv = self.controller.post('/register', data=json.dumps({
		# 	'email':'user@test.com',
		# 	'username':'nick'
		# }), headers={'content-type':'application/json'})
		# assert 400 == rv.status_code
		# # Missing username
		# rv = self.controller.post('/register', data=json.dumps({
		# 	'email':'user@test.com',
		# 	'password':'password1!@',
		# }), headers={'content-type':'application/json'})
		# assert 400 == rv.status_code

	def test_login(self):
		"""API: Log in"""
		rv = self.register()
		assert 200 == rv.status_code
		# Correct input
		rv = self.controller.post('/login', data=json.dumps(self.user_info), headers={'content-type':'application/json'})
		assert 200 == rv.status_code
		# Missing email
		rv = self.controller.post('/login', data=json.dumps({
			'password':'password1!@',
		}), headers={'content-type':'application/json'})
		assert 400 == rv.status_code
		# Missing password
		rv = self.controller.post('/login', data=json.dumps({
			'email':'user@test.com',
		}), headers={'content-type':'application/json'})
		assert 400 == rv.status_code
		# Wrong email
		rv = self.controller.post('/login', data=json.dumps({
			'email':'wronguser@test.com',
			'password':'password1!@'
		}), headers={'content-type':'application/json'})
		assert 401 == rv.status_code
		# Wrong password
		rv = self.controller.post('/login', data=json.dumps({
			'email':'user@test.com',
			'password':'wrongpassword1!@'
		}), headers={'content-type':'application/json'})
		assert 401 == rv.status_code

	def test_logout(self):
		"""API: Log out"""
		rv = self.register()
		assert 200 == rv.status_code
		rv = self.login()
		assert 200 == rv.status_code
		rv = self.controller.get('/logout')
		assert 200 == rv.status_code

	if __name__ == '__main__':
		unittest.main()