import json
import pickle

file = open("temp.txt",'w+')
data = {
    "name": "John Doe",
    "userid": "johndoe123",
    "password": "12345678"
}

#using json module

print(f"Original data: {data}")
print(f"Type of original data: {type(data)}")
print()

#encrypting the data
""" enc_data=json.dumps(data)
print(f"Encrypted data: {enc_data}")
print(f"Type of encrypted data: {type(enc_data)}")
print() """

#decrypting the data
""" dec_data=json.loads(enc_data)
print(f"Decrypted data: {dec_data}")
print(f"Type of decrypted data: {type(dec_data)}")
file.close() """ 

#encrypting and decrypting using file handling
""" enc_data=json.dumps(data)
file.write(enc_data)
file.seek(0)
r=file.read()
print(f"Encrypted data: {r}") 

original_data=json.loads(enc_data)
print(f"Decrypted data: {original_data}")
print(f"Type of decrypted data: {type(original_data)}")

file.close() """

#Using pickle module

#encrypting the data
enc_data=pickle.dumps(data)
print(f"Encrypted data: {enc_data}")
print(f"Type of encrypted data: {type(enc_data)}")
print()

#decrypting the data
dec_data=pickle.loads(enc_data)
print(f"Decrypted data: {dec_data}")
print(f"Type of decrypted data: {type(dec_data)}")
