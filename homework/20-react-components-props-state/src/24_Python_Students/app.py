students = {
    "Aram": [90, 85, 100],
    "Anna": [75, 88],
    "Karen": []
}

while True:
    print("\n1 - Ավելացնել ուսանող")
    print("2 - Ավելացնել գնահատական")
    print("0 - Ելք")

    choice = input("Ընտրիր տարբերակը: ")

    # 1 — ուսանող ավելացնել
    if choice == "1":
        name = input("Ուսանողի անունը: ")

        if name in students:
            print("Ուսանողը արդեն կա")
        else:
            students[name] = []
            print("Հաջողությամբ ավելացվեց")

    # 2 — գնահատական ավելացնել
    elif choice == "2":
        name = input("Ուսանողի անունը: ")

        if name in students:
            grade = int(input("Գնահատական (0-100): "))

            if 0 <= grade <= 100:
                students[name].append(grade)
                print("Գնահատականը ավելացվեց")
            else:
                print("Սխալ գնահատական")
        else:
            print("Ուսանողը չի գտնվել")

    # 0 — դուրս գալ
    elif choice == "0":
        print("Ծրագիրը փակվում է")
        break

    else:
        print("Սխալ ընտրություն")