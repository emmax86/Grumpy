from datetime import datetime
from os import urandom
from hashlib import sha256
import hmac
import base64

def generate_token(user_identifier, creation_datetime, secret):
	creation_unix_timestamp = creation_datetime.strftime("%s")
	token_identifier = "{0}:{1}".format(user_identifier, creation_unix_timestamp)
	token_hmac = base64.b64encode(hmac.new(secret, token_identifier, digestmod=sha256).digest())
	token = "{0}:{1}".format(token_identifier, token_hmac)
	return token
	
def generate_secret(bits):
	if bits % 8 != 0:
		raise ValueError("Bits not divisible by 8")  # The programmer is an idiot
	else:
		num_bytes = bits / 8
		return urandom(num_bytes).encode("hex")         # The programmer is a really cool guy

def verify_token(token, user_identifier, creation_datetime, secret):
	return generate_token(user_identifier, creation_datetime, secret) == token
