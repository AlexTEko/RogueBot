import os
import pickle
from user import User
		
def get_fname(uid):
	return 'users/{0}.usr'.format(uid)

def save_user(usr):
	with open(get_fname(usr.uid), 'wb') as outfile:
		pickle.dump(usr, outfile)

def new_user(uid):
	usr = User(uid)

	save_user(usr)

def get_user(uid):
	if os.path.exists(get_fname(uid)):
		usr = None

		with open(get_fname(uid), 'rb') as outfile:
			usr = pickle.load(outfile)

		return usr
	else:
		return None

def message(uid, reply, text):
	usr = get_user(uid)

	if not usr:
		reply('Что-то пошло не так. Попробуй /start')
	else:
		usr.message(reply, text)

	save_user(usr)

def setname(uid, name):
	usr = get_user(uid)
	usr.name = name
	save_user(uid)


