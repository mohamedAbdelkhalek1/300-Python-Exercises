"""
assignment 16:

Write A Python Program to store name, address, contact in dictionary, and then update user contact number,
but user will enter his/her contact number at run time.


"""


# to store user info
# then display
# then update record with user nput
# then display
# key:value, name:xyz


user_info = {"name":"Ali","address":"DIKHAN","contact":891828932}

print("First Record")
print(user_info)
new_content = int(input("Enter new content"))
user_info.update({"contact":new_content})            
print("Updated Record")
print(user_info)
