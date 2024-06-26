import sqlite3

db = sqlite3.connect('employee.db')

cursor = db.cursor()

#بيرزع ايرور لو الجدول موجود    

# cursor.execute("""CREATE TABLE employees (
#           name VARCHAR(50),
#           job VARCHAR(50),
#           salary integer,
#           id integer PRIMARY KEY
# )""")
# db.commit()

def insert_emp(name, job, salary):
    cursor.execute(f"INSERT INTO employees (name, job, salary) VALUES ('{name}', '{job}', {salary})")
    db.commit()
def print_emps():
    cursor.execute("SELECT * FROM employees")
    print(cursor.fetchall())
def delete_emp(name):
    cursor.execute(f"DELETE FROM employees WHERE name = '{name}'")
    db.commit()
def update_job(name, job):
    cursor.execute(f"UPDATE employees SET job = '{job}' WHERE name = '{name}'")
    db.commit()
def update_salary(name, salary):
    cursor.execute(f"UPDATE employees SET salary = {salary} WHERE name = '{name}'")
    db.commit()
def print_emp(name):
    cursor.execute(f"SELECT * FROM employees WHERE name = '{name}'")
    print(cursor.fetchall())
def print_emp_id(id):
    cursor.execute(f"SELECT * FROM employees WHERE id = {id}")
    print(cursor.fetchall())
def delete_emp_id(id):
    cursor.execute(f"DELETE FROM employees WHERE id = {id}")
    db.commit()
def update_job_id(id, job):
    cursor.execute(f"UPDATE employees SET job = '{job}' WHERE id = {id}")
    db.commit()
def update_salary_id(id, salary):
    cursor.execute(f"UPDATE employees SET salary = {salary} WHERE id = {id}")
    db.commit()
def print_menu():
    print("1. Insert employee")
    print("2. Print all employees")
    print("3. Delete employee by name")
    print("4. Update employee job by name")
    print("5. Update employee salary by name")
    print("6. Print employee by name")
    print("7. Print employee by id")
    print("8. Delete employee by id")
    print("9. Update employee job by id")
    print("10. Update employee salary by id")
    print("11. Exit")
    print("Enter your choice:")


while True:
    print_menu()
    choice = input()
    if choice == '1':
        name = input("Enter name:")
        job = input("Enter job:")
        salary = int(input("Enter salary:"))
        insert_emp(name, job, salary)
    elif choice == '2':
        print_emps()
    elif choice == '3':
        name = input("Enter name:")
        delete_emp(name)
    elif choice == '4':
        name = input("Enter name:")
        job = input("Enter job:")
        update_job(name, job)
    elif choice == '5':
        name = input("Enter name:")
        salary = int(input("Enter salary:"))
        update_salary(name, salary)
    elif choice == '6':
        name = input("Enter name:")
        print_emp(name)
    elif choice == '7':
        id = int(input("Enter id:"))
        print_emp_id(id)
    elif choice == '8':
        id = int(input("Enter id:"))
        delete_emp_id(id)
    elif choice == '9':
        id = int(input("Enter id:"))
        job = input("Enter job:")
        update_job_id(id, job)
    elif choice == '10':
        id = int(input("Enter id:"))
        salary = int(input("Enter salary:"))
        update_salary_id(id, salary)
    elif choice == '11':
        db.close()
        break
    else:
        print("Invalid choice")