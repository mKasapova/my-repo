username = input()
password = input()

sign_in_pass = input()

while sign_in_pass != password:
    sign_in_pass = input()

print(f"Welcome {username}!")