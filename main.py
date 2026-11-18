
def calculate_total(marks):
    return sum(marks)


def calculate_average(marks):
    return calculate_total(marks) / len(marks)


def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"


def calculate_result(marks):
    if all(mark >= 35 for mark in marks):
        return "PASS"
    return "FAIL"


def display_student_result(name, usn, marks):
    total = calculate_total(marks)
    average = calculate_average(marks)
    grade = calculate_grade(average)
    result = calculate_result(marks)

    print("\n------ STUDENT RESULT ------")
    print("Student Name:", name)
    print("USN:", usn)
    print("Total Marks:", total)
    print("Average Marks:", format(average, ".2f"))
    print("Grade:", grade)
    print("Result:", result)


def main():
    print("STUDENT GRADE MANAGEMENT SYSTEM")

    name = input("Enter Student Name: ")
    usn = input("Enter USN: ")

    subjects = ["Python", "Java", "DBMS", "OS", "Networking"]
    marks = []

    print("\nEnter marks for 5 subjects:")

    for subject in subjects:
        while True:
            try:
                mark = float(input(subject + ": "))

                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Enter marks between 0 and 100.")

            except ValueError:
                print("Please enter a valid number.")

    display_student_result(name, usn, marks)


if __name__ == "__main__":
    main()
