import pymongo
import base64
import random
from . import key_gen as keygen
from pymongo import MongoClient
from . import cuba_cypher

def encrypt(data=None, mongo_url=None):
	if data == None:
		return "[CubaCrypt]: No data has been sent to CubaCrypt"

	elif mongo_url == None:
		return "[CubaCrypt]: No Mongo URL has been provide to store encrypted data."

	else:
		try:
			cyphered_data = cuba_cypher.cypher(data)
			encrypted = cyphered_data.encode("ascii")
			base64_bytes = base64.b64encode(encrypted)
			encrypted_string = base64_bytes.decode("ascii")

			cluster = MongoClient(mongo_url)
			collection = cluster.CubaCrypt.data

			length = [8, 10, 12,16, 18,32]
			key = keygen.generate(random.choice(length))
			cyphered_key = cuba_cypher.cypher(key)
			collection.insert_one({ "_id": cyphered_key, "data": encrypted_string })
			return cyphered_key
		except Exception as e:
			print(f"[CubaCrypt]: Error Exception occurred in CubaCrypt:\n{e}\n\nError could've occurred due to Invalid Mongo URL or Missing Collection/DataBase, please check the documentation.")

def decrypt(key=None, mongo_url=None):
	data = key
	if data == None:
		return "[CubaCrypt]: No key has been sent."

	elif mongo_url == None:
		return "[CubaCrypt]: No Mongo URL has been provide to store encrypted data."

	else:
		try:
			cluster = MongoClient(mongo_url)
			collection = cluster.CubaCrypt.data
			if collection.count_documents({ "_id": data }) == 0:
				return "[CubaCrypt]: Invalid Key"

			for entries in collection.find( { "_id": data } ):
				data = entries['data']

				base64_bytes = data.encode("ascii")
  
				decrypted_string_bytes = base64.b64decode(base64_bytes)
				decrypted_string = decrypted_string_bytes.decode("ascii")

				decyphered_data = cuba_cypher.decypher(str(decrypted_string))
				
				return decyphered_data
		except Exception as e:
			print(f"[CubaCrypt]: Error Exception occurred in CubaCrypt:\n{e}\n\nError could've occurred due to Invalid Mongo URL or Missing Collection/DataBase, please check the documentation.")
