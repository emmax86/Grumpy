from grumpy import *
from datetime import datetime

for i in xrange(1000):
	secret = generate_secret(128)
	identifier = "User{0}".format(i)
	creation_time = datetime.now()
	token = generate_token(identifier, creation_time, secret)
	print token
	token_split = token.split(":")
	identifier = token_split[0]
	creation_time = datetime.fromtimestamp(int(token_split[1]))
	assert verify_token(token, identifier, creation_time, secret)