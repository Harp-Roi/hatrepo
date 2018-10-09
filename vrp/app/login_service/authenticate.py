#!/usr/bin/python

import jwt

SECRET = 'my_static_secretR'
ALGORITHM = 'HS256'
USER_TABLE = 'users'


def write_token_to_user_table(user_id,user_token):
	try:
		init db
		add token
		return True
	except Exception as e:
		print("Couldn't add new user, received error: " + str(e))
		return False


def create_user(user_id, password):
	encoded_token = jwt.encode({str(user_id) : str(password)}, SECRET, ALGORITHM)

def login_user(user_id, password):
	

def get_user(user_id, user_token):
	jwt.decode(user_token, SECRET, algorithm=ALGORITHM)
	return
