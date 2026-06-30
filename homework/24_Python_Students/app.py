students = {
    "Aram": [90, 85, 100],
    "Anna": [75, 88],
    "Karen": []
}

while True:
    print("\n1 - Ավելացնել ուսանող")
    print("2 - Ավելացնել գնահատական")
    print("3 - bolor tvyalnery")
    print("4 - Վիճակագրություն")
    print("0 - Ելք")

    choice = input("Ընտրիր տարբերակը: ")

   
    if choice == "1":
        name = input("Ուսանողի անունը: ") 
        if name in students:
            print("Ուսանողը արդեն կա")
        else:
            students[name] = []
            print("Հաջողությամբ ավելացվեց")

  
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

    elif choice == "3":
     for student, grades in students.items():
        print(student, grades)
    
    elif choice == "4":
     total_students = len(students)

     total_sum = 0
     total_count = 0
     excellent = 0
     no_grades = 0

     for grades in students.values():
        if grades:
            average = sum(grades) / len(grades)

            if average > 90:
                excellent += 1

            total_sum += sum(grades)
            total_count += len(grades)
        else:
            no_grades += 1

     if total_count > 0:
        group_average = total_sum / total_count
     else:
        group_average = 0

     print("Ընդհանուր ուսանողներ:", total_students)
     print("Խմբի միջին գնահատականը:", round(group_average, 1))
     print("Գերազանցիկներ:", excellent)
     print("Ուսանողներ առանց գնահատականի:", no_grades)
     print("elq") 