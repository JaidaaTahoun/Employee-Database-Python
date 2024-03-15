def UploadTextData(file_path): #define function

    employees = [] #storing employee data in a list
    with open(file_path, 'r') as file:
        for line in file:
            data = line.strip().split(', ')
            last_name, first_name, departments, salary = data
            departments = departments.split('-')
            employee = {
                'last_name': last_name,
                'first_name': first_name,
                'departments': departments,
                'salary': int(salary)
            }
            employees.append(employee)
    return employees

def PrintData(employees):

    print('\nData:')
    for employee in employees:
        departments_str = ' and '.join(employee['departments'])
        print(f"Employee: {employee['first_name']} {employee['last_name']}, Departments: {departments_str}, Salary: ${employee['salary']}")

def CreateStatsFile(employees):

    department_employees = {}
    average_salary_departments = {}
    highest_salary = {"salary": 0, "employee":''}


    for employee in employees:
        for department in employee['departments']:
            if department in department_employees:
                department_employees[department].append(f"{employee['first_name']} {employee['last_name']}")
            else:
                department_employees[department] = [f"{employee['first_name']} {employee['last_name']}"]
        if employee['salary'] > highest_salary['salary']:
            highest_salary =  {"salary": employee['salary'], "employee": employee['first_name']+" "+employee['last_name']}

    for department, employee_list in department_employees.items():
        average_salary = sum([employee['salary'] for employee in employees if department in employee['departments']]) / len(employee_list)
        average_salary_departments[department] = round(average_salary, 2)


    with open('stats.txt', 'w') as stats_file:
        stats_file.write("Employees by department:\n")
        for department, employee_list in department_employees.items():
            stats_file.write(department)
            stats_file.write("\n-"+'\n-'.join(employee_list)+"\n")

            stats_file.write('\n')

        stats_file.write(f"Employee with highest salary: {highest_salary['employee']} with salary: {highest_salary['salary']:.1f}\n")
        stats_file.write("\nAverage salaries by department:\n")
        for department, employee_list in department_employees.items():
            stats_file.write(f"{department} ${average_salary_departments[department]:.2f}\n")

def main():
    employees = []

    while True:
        if not employees:
            print("Welcome to the Employee Database.")

        print("Please choose one of the following options:")
        print("1. Upload text data")
        print("2. View data")
        print("3. Download statistics")
        print("4. Print statistics file")
        print("5. Exit the program")

        choice = input()

        if choice == '1': #option 1: program asks for name of the file, file should include info about employess and then program reads data from the file and stores it
            file_path = input("Please enter the name of the file to be uploaded:")
            employees = UploadTextData(file_path)
        elif choice == '2': #option 2: program shows data about empluyess uploaded and the program is going to display the employees names, departements, and salaries.
            if not employees:
                print("Please upload data first.\n")
            else:
                PrintData(employees)
        elif choice == '3': #option 3: program calculate stats about employees, figures out which employee works in what dept, calculates avg salary in each dept and finds employee w/ highest salary and then saves info in file
            if not employees:
                print("Please upload data first.\n")
            else:
                CreateStatsFile(employees)
        elif choice == '4': #option 4: Allows u to see contents of file which contains employee stats
            try:
                with open('stats.txt', 'r') as stats_file:
                    print("\nStatistics file contained:\n" + stats_file.read() + "\n")
            except FileNotFoundError:
                print("Statistics file not found. Please download statistics first.\n")
        elif choice == '5': #option 5: exit program
            print("Thank you for using the Employee Database Program!")
            break
        else: #Invalid option
            print("Invalid choice. Please enter a valid option.\n")

createFile = open("sample1.txt", 'w') #test case 1 to test program
createFile.write("Mouse, Mickey, Accounting-Sales, 89000\n");
createFile.write("Mouse, Minne, Marketing-Engineering-Technology, 67280\n");
createFile.write("Duck, Donald, Sales, 76282\n");
createFile.write("Duck, Daisy, Accounting, 81262\n");
createFile.write("Builder, Bob, Marketing-Sales, 125211\n");
createFile.write("Bunny, Bugs, Marketing, 55161\n");
createFile.write("Brown, Charlie, Sales-Engineering, 65111\n");
createFile.write("Mouse, Jerry, Marketing, 61651\n");
createFile.close()

createFile = open("sample2.txt", "w") #test case 2 to test program
createFile.write("Panther, Pink, Sales, 67611\n")
createFile.write("Duck, Daffy, Human Resources-Technology-Marketing, 98171\n")
createFile.write("Pooh, Winnie, Accounting, 51511\n")
createFile.write("Doo, Scooby, Marketing-Human Resources-Sales, 127321\n")
createFile.write("Flinstone, Fred, Human Resources, 76176\n")
createFile.write("Bear, Yogi, Accounting-Technology, 128212\n")
createFile.write("Runner, Road, Sales-Engineering, 90910\n")
createFile.write("Dog, Pluto, Engineering-Sales-Accounting, 67671\n")
createFile.close()

createFile = open("sample3.txt", "w") #test case 3 to test program
createFile.write("Mouse, Mickey, Accounting-Sales, 89000\n");
createFile.write("Mouse, Minne, Marketing-Engineering-Technology, 67280\n");
createFile.write("Duck, Donald, Sales, 76282\n");
createFile.write("Duck, Daisy, Accounting, 81262\n");
createFile.write("Builder, Bob, Marketing-Sales, 125211\n");
createFile.write("Bunny, Bugs, Marketing, 55161\n");
createFile.write("Brown, Charlie, Sales-Engineering, 65111\n");
createFile.write("Mouse, Jerry, Marketing, 61651\n");
createFile.write("Panther, Pink, Sales, 67611\n")
createFile.write("Duck, Daffy, Human Resources-Technology-Marketing, 98171\n")
createFile.write("Pooh, Winnie, Accounting, 51511\n")
createFile.write("Doo, Scooby, Marketing-Human Resources-Sales, 127321\n")
createFile.write("Flinstone, Fred, Human Resources, 76176\n")
createFile.write("Bear, Yogi, Accounting-Technology, 128212\n")
createFile.write("Runner, Road, Sales-Engineering, 90910\n")
createFile.write("Dog, Pluto, Engineering-Sales-Accounting, 67671\n")
createFile.close()
main()
