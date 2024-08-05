import hashlib

username = input("Please choose your username: ")
password = input("Please choose a password (Your password should be at least 10 characters and should be a combination of digits, upper-case and lower-case letters, and special characters): ")

def sha1(object):
    enc_obj = object.encode("utf-8")
    hash = hashlib.sha1(enc_obj).hexdigest()
    return hash
    
def sha256(salt, object):
    enc_salt = salt.encode("utf-8")
    enc_object = object.encode("utf-8")
    hash = hashlib.sha256(enc_salt + enc_object).hexdigest()
    return hash
   
if len(password) < 10:
    print("Your password is too short. Please choose a new password. (Your password should be at least 10 characters and should be a combination of digits, upper-case and lower-case letters, and special characters.)")
else: 
    user_3 = username[:3]
    pass_3 = password[:3]
    
    pre_salt = user_3 + pass_3

    salt_long = sha1(pre_salt)
    salt = salt_long[:64]
    

    final_login=(f"{username}${salt}${sha256(salt, password)}")
    print("Congratulations! Your registration is complete! You must NOT share your password with others.")
    with open("shadow.txt", "a") as f:
        f.write(final_login + "\n")
