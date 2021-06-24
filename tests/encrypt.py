from src import cubacrypt

mongo = "mongodb+srv://Benitz:4mWMn7ety6HrIRIx@numix.dksdu.mongodb.net/CubaCrypt?retryWrites=true&w=majority"
key = cubacrypt.encrypt("Testing!", mongo)

print(key)

decrypted = cubacrypt.decrypt(key, mongo)

print(decrypted)