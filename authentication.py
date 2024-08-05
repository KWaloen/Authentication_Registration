import hashlib

username = input("Please input your username: ")
entered_password = input("Please provide your password: ")
    
def sha256(salt, object):
    enc_salt = salt.encode("utf-8")
    enc_object = object.encode("utf-8")
    hash = hashlib.sha256(enc_salt + enc_object).hexdigest()
    return hash

with open("shadow.txt") as f:
    lines = f.readlines()

dicts = {}

for shadow in lines:
    shadow_split = shadow.split("$")
    stored_username = shadow_split[0]
    stored_salt = shadow_split[1]
    dicts[stored_username] = stored_salt

dicts_hash = {}

for text in lines:
    text_split = text.split("$")
    stored_user = text_split[0]
    stored_hash = text_split[2]
    dicts_hash[stored_user] = stored_hash
    
def find_user_salt_and_hash(username, dicts, dicts_hash):
    if username not in dicts.keys():
        return "The provided username and password do not match. Please try again."
    elif username in dicts.keys():
        clean_hash = dicts_hash[username].split()
        cleaner_hash = "".join(clean_hash)
        return dicts[username], cleaner_hash 

def challenge(username, entered_password):
    stored_user_salt = find_user_salt_and_hash(username, dicts, dicts_hash)[0]
    stored_user_hash = find_user_salt_and_hash(username, dicts, dicts_hash)[1]
    calculated_hash = sha256(stored_user_salt, entered_password)
    if stored_user_hash == calculated_hash:
        return "You are successfully logged in!"
    else:
        return "The provided username and password do not match. Please try again."

print(challenge(username, entered_password))
    

