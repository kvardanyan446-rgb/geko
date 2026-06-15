store = {
     "surname" : "Vardanyan",
     "name" : "Karen",
     "age" : 20
   
}
print(store["surname"], store["name"], store["age"])

store2 = {
      "surname" : "Vardanyan",
      "name" : "Karen",
      "age" : 20     
}
print(store2)

store3 = {
    "ashxatavardz" : 5000,
    "orer" : 7
}
total = store3["ashxatavardz"] * store3["orer"]
print(total)

parol = {
    "password" : "123abcdf"
}
if len(parol["password"]) == 8:
    print("password uni 8 nish")
else:
    print("8 nish che")

user = {
          "admin": "123abcdf"
}

username = input(" username: ")
password = input(" password: ")

if username in user and user[username] == password:
    print("mutqy hajoxvec")
else:
        print("sxal mutq")

price = int(input("giny: "))

if price > 10000:
    price = price - price * 10 / 100

print(price)



wins = int(input())
draws = int(input())

total = wins * 3 + draws * 1

print(total)

km = int(input())
liters_per_100km = int(input())

fuel = (km * liters_per_100km) / 100

print(fuel)

price = int(input())
quantity = int(input())

total = price * quantity

print(total)

tasks = [
    "Python",
    "React",
    "Sport",
    "Read",
    "Sleep"
]

for task in tasks:
    print(task)

    sales = [12000, 15000, 8000, 22000]

total = sum(sales)

print(total)