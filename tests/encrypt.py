from src import cubacrypt

mongo = "MongoURL"
key = cubacrypt.encrypt("Testing!", mongo)

print(key)

decrypted = cubacrypt.decrypt(key, mongo)

print(decrypted)