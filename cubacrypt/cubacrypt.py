import base64
import random
from .key_gen import generate
from pymongo import MongoClient
from .cuba_cypher import cypher, decypher

def encrypt(data=None, mongo_url=None):
	if data == None:
		return None

	elif mongo_url == None:
		raise RuntimeError(f"Mising DataBase, Collection, or MongoURL.")

	else:
		try:
			cyphered_data = cypher(data)
			encrypted = cyphered_data.encode("ascii")
			base64_bytes = base64.b64encode(encrypted)
			encrypted_string = base64_bytes.decode("ascii")

			cluster = MongoClient(mongo_url)
			collection = cluster.CubaCrypt.data

			length = [8, 10, 12, 16, 18, 20]
			key = generate(random.choice(length))
			cyphered_key = cypher(key)
			collection.insert_one({ "_id": cyphered_key, "data": encrypted_string })
			return cyphered_key
		except Exception as e:
			raise RuntimeError(f"Mising DataBase, Collection, or MongoURL.")

def decrypt(key=None, mongo_url=None):
	data = key
	if data == None:
		return None

	elif mongo_url == None:
		return None

	else:
		try:
			cluster = MongoClient(mongo_url)
			collection = cluster.CubaCrypt.data
			if collection.count_documents({ "_id": data }) == 0:
				return None

			for entries in collection.find( { "_id": data } ):
				data = entries['data']

				base64_bytes = data.encode("ascii")
  
				decrypted_string_bytes = base64.b64decode(base64_bytes)
				decrypted_string = decrypted_string_bytes.decode("ascii")

				decyphered_data = decypher(str(decrypted_string))
				
				return decyphered_data
		except Exception as e:
			raise RuntimeError(f"Mising DataBase, Collection, or MongoURL.")
