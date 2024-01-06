"""
assignment 82:

Write A Python Program To Check Whether Username Is Encrypted Form Or Not

"""

# import random
# import string

# all_chars = list(string.ascii_letters + string.digits + string.punctuation + " ")

# key = all_chars.copy()
# random.shuffle(key)

# # Encrypy
# user_name = input("Enter User Name : ")
# cipher_text = ""
# for l in user_name:
#     index = all_chars.index(l)
#     cipher_text += key[index]

# print(f"User Name Encryption : {cipher_text}")


# # decrypy
# cipher_text = input("Enter The Text To decrypt")
# plain_text = ""
# for l in cipher_text:
#     index = key.index(l)
#     plain_text += all_chars[index]

# print(f"decryption text : {plain_text}") 


# import re

# def is_encrypted_username(username):
#     pattern = r'^[A-Za-z0-9@_]+$'
#     match = re.match(pattern, username)
#     return match is not None

# # Example usage
# username = input("Enter the username: ")
# if is_encrypted_username(username):
#     print("The username is in encrypted form.")
# else:
#     print("The username is not in encrypted form.")