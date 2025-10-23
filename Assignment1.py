print('Welcome to Grade Registry Program ')

student = {} # a dictionary made to store students name and avr GPA

while True:
    answer = input('Do you want to add a student(yes/no):')
    if answer == "yes":
        name = input("enter students name:")
        gpas = [] #Created an empty list to store gpa's

        print("Enter GPA values for the student's courses. Type -1 to stop.")
        while True:
            gpa_input = input('Enter GPAs: ')
            if gpa_input == '-1':
                break
            gpa = float(gpa_input)
            gpas.append(gpa)#adding gpa's to the current list of gpas 
            
        if gpas: 
                average = sum(gpas) / len(gpas) #the sum/the number of gpa
        else:
                average = 0.0

        student[name] = average 

    elif answer == "no":
        print("This is the list of students in the system, and their corresponding accumulative GPA:")
        for name, average in student.items():
             print(f"{name} {average:.2f}" )
        break
    else:
         print('invalid input')
