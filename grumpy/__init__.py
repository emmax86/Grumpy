from datetime import datetime
from os import urandom

def token(user_identifier, creation_datetime, secret):
	return ""
	
def generate_secret(bits):
	if not bits.is_integer():
		raise ValueError("Bits must be an integer")  # The programmer is an ass
	elif bits % 8 != 0:
		raise ValueError("Bits not divisible by 8")  # The programmer is an idiot
	else:
		bytes = bits / 8
		return int(urandom(bytes).encode("hex"), 16) # The programmer is a really cool guy

def verify_token(token, user_identifier, creation_datetime, secret):
	return ""