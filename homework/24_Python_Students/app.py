students = {
    "Aram" : [90, 85, 100],
    "Anna" : [75, 88],
    "Karen" : [] 
    }
while True:
    print("\n1 - avelacnel usanox ")
    print("2 - avelacnel gnahatakan ")
    print("0 - durs gal ")

    choice = input("yntrit tarberakneric : ")

    if choice == "1":
        name = input("usanoxi anuny : ")

        if name in students:
            print("arden ka")
        else:
            students[name] = []
            print("avelacvec ")

    elif choice == "2":
        name = input("usanoxi anuny : ")

        if name in students:
            grade = int(input("gnahatakany tvyal miavornerov (0-100): "))

            if 0 <= grade <= 100:
                students[name].append(grade)
                print("avelacvec gnahatakany ")
            else:
                print("sxal gnahatakan ")
        else:
            print("usanox chi gtnvel")
if choice == "1":
    ...

elif choice == "2":
    ...

elif choice == "3":
    for name, grades in students.items():

        if len(grades) > 0:
            avg = sum(grades) / len(grades)
            print(name, "->", grades, "-> միջին:", round(avg, 2))
        else:
            print(name, "->", grades, "-> միջին: N/A")

elif choice == "0":
    print("cragiry pakvum e")
else:
    print("sxal yntrutyun")