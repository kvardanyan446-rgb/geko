import json

user_login = input("Login: ")
user_password = input("Password: ")

new_user = {
    "login": user_login,
    "password": user_password
}


try:
    with open("data.json", "r") as file:
        data = json.load(file)
except:
    data = []


data.append(new_user)


with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

print("Saved")