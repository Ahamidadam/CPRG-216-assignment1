print('Welcome to the Grade Registry Program')

student = {}  # a dictionary made to store student names and average GPAs

while True:
    answer = input('Would you like to add a new student? y(yes),n(no)\n')
    if answer == "yes" or answer == "yEs" or answer == "YEs" or answer == "Yes":
        name = input("Enter the student's name:\n")
        gpas = []  # empty list to store GPA values

        print('Enter student GPA for each subject. Enter -1 to stop entering GPA.')
        while True:
            gpa_input = input('')
            if gpa_input == '-1':
                break
            gpa = float(gpa_input)
            gpas.append(gpa)

        if gpas:
            average = sum(gpas) / len(gpas)
        else:
            average = 0.0

        student[name] = average

    elif answer == "no" or answer == "n":
        print("This is the list of students in the system, and their corresponding accumulative GPA")
        for name, average in student.items():
            # remove unnecessary trailing zeros to match the assignment exactly
            formatted_avg = ('%.2f' % average).rstrip('0').rstrip('.') # Removes 0. Removes . when output is 0
            print(f"{name} {formatted_avg}")
        break

    else:
        print('Incorrect Input, please enter y(yes)/n(no).')