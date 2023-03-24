# Employee Module

import mysql.conector as s
con=s.connect(host="localhost", user="admin",passward="", database ="Payroll")
if con.is_connected()==False:
    print("Database not connected")
else:
    cur=con.cursor()

def Add_New_Employee():
    emp_code=int(input("Enter the Employee Code : "))
    emp_name=input("Enter the Employee Name : ")
    emp_ph=int(input("Enter the Employee Phone No. : "))
    emp_dept=input("Enter the Department of Employee  : ")
    emp_date_of_join=int(input("Enter the Employee Date of Joining in(YYYY-MM-DD) format : "))
    emp_add=input("Enter the Employee Address : ")
    cur.execute("insert into Employee values(%s,%s,%s,%s,%s,%s)",(emp_code, emp_name, emp_ph, emp_dept, emp_date_of_join, emp_add))
    con.commit()

def Display_Employee():
    cur.execute("select*from Employee")
    a=cur.fetchall()
    if a==None:
        print("No record found!")
    else:
        print(tabulate(data,headers=['emp_code','emp_name', 'emp_ph', 'emp_dept', 'emp_date_of_join', 'emp_add'],tablefnt='psql'))

def Search_Employee():
    x=int(input("Enter the employee code of employee to be searched : "))
    cur.execute("select * from Employee where emp_code=%s",(x,))
    a=cur.fetchone()
    if a==None:
        print("Record Not found")
    else:
        print(a) 

def Delete_Employee():
    y=int(input("Enter the employee code of the employee to be delted : "))
    cur.execute("select * from Employee where emp_code=%s",(y,) )
    a=cur.fetchone()
    if a==None:
        print("Record Not Found")
    else:
        print(tabulate(data,headers=['emp_code','emp_name', 'emp_ph', 'emp_dept', 'emp_date_of_join', 'emp_add'],tablefnt='psql'))
        print(a)
        c=input("Do you want to delete this record y/n:")
        if c=="y" or c=="Y":
            cur.execute("Delete from Employee where emp_code=%s",(y,))
            con.commit()
            print("Record Deleted Successfully.")
        else:
            print("Task Aborted!")    
 
 def Modify_Employee():
     p=int(input("Enter the employee code to be Modified : "))
     cur.execute("select * from Employee where pat_id=%s",(p,))
     a=cur.fetchone()
     if a==None:
         print("Record not found")
     else:
         print(tabulate(data,headers=['emp_code','emp_name', 'emp_ph', 'emp_dept', 'emp_date_of_join', 'emp_add'],tablefnt='psql'))
         print(a)
         P=input("Do you want to modify this record y/n:")
        if P=="y" or P=="Y":
            name=input("Enter the New Employee Name or press enter to skip:")
            if name=="":
                pass
            else:
                cur.execute("update Employee set emp_name=%s where emp_code=%s",(name,p))
            phone=int(input("Enter new employee no. or press enter to skip : "))
            if phone=="":
                pass
            else:
                cur.execute("update Employee set emp_ph=%s where emp_code=%s",(phone,p))
            Dept=input("Enter Employee new Department or press enter to skip : ")
            if Dept=="":
                pass
            else:
                cur.execute("update Employee set emp_dept=%s where emp_code=%s",(Dept,p))
            doj =int(input("Enter Employee new date of joining in(YYYY-MM-DD or press enter to skip:"))
            if doj=="":
                pass
            else:
                cur.execute("update Employee set emp_date_of_join=%s where emp_code=%s",(doj,p))
            address=input("Enter the new address of the employee")
            if address=="":
                pass
            else:
                cur.execute("update Employee set emp_add=%s where emp_code=%s",(address,p))
            
        else:
            print("Task Aborted!")

# Attendance Module

import mysql.connector as s
from tabulate import tabulate

import mysql.conector as s
con=s.connect(host="localhost", user="admin",passward="", database ="Payroll")
if con.is_connected()==False:
    print("Database not conected")
else:
    cur=con.cursor()

def Add_Employee_Attendance():
    emp_code=int(input("Enter the employee code : "))
    Day = input("Type the number of days of this month : ")
    Month = input("Type today's Month in Number.")
    Year = input("Type today's Years : ")
    g=int(input("Enter the no. of days employee was present : "))
    h=int(input("Enter the no. of days employee was absent : "))
    cur.execute("insert into patient values(%s,%s,%s,%s,%s,%s)",(emp_code, Day, Month, Year, p, a))
    con.commit()

def Display_Employee_Attendance():
    cur.execute("select*hhhfrom Attendance")
    a=cur.fetchall()
    if a==None:
        print("No record found!")
    else:
        print(tabulate(data,headers=['emp_code','Day', 'Month', 'Year', 'year', 'g','h',],tablefnt='psql')) 

def Search_Employee_Attandance():
    x=int(input("Enter the employee code of employee to be searched : "))
    cur.execute("select * from Employee where emp_code=%s",(x,))
    a=cur.fetchone()
    if a==None:
        print("Record Not found")
    else:
        print(a)  

def Delete_Employee_Attendance():
    y=int(input("Enter the employee code of the employee to be delted : "))
    cur.execute("select * from Employee where emp_code=%s",(y,) )
    a=cur.fetchone()
    if a==None:
        print("Record Not Found")
    else:
        print(tabulate(data,headers=['emp_code','Day', 'Month', 'Year', 'g', 'h'],tablefnt='psql'))
        print(a)
        c=input("Do you want to delete this record y/n:")
        if c=="y" or c=="Y":
            cur.execute("Delete from Employee where emp_code=%s",(y,))
            con.commit()
            print("Record Deleted Successfully.")
        else:
            print("Task Aborted!")  

def Modify_Employee_Attendance():

    p=int(input("Enter the employee code to be Modified : "))
    cur.execute("select * from Employee where pat_id=%s",(p,))
    a=cur.fetchone()
    if a==None:
        print("Record not found")
    else:
        print(tabulate(data,headers=['emp_code','Day', 'Month', 'Year', 'g', 'h'],tablefnt='psql'))
        print(a)
        P=input("Do you want to modify this record y/n:")
        if P=="y" or P=="Y":
            Day=int(input("Enter new Day or press enter to skip : "))
            if Day=="":
                pass
            else:
                cur.execute("update Attendance set Day=%s where emp_code=%s",(Day,p))
            Month=input("Enter Employee new Month or press enter to skip : ")
            if Month=="":
                pass
            else:
                cur.execute("update Employee set Month=%s where emp_code=%s",(Month,p))
            Year=int(input("Enter Employee new Year or press enter to skip:"))
            if Year=="":
                pass
            else:
                cur.execute("update Employee set Year=%s where emp_code=%s",(Year,p))
            g=input("Enter the days of month in which of the employee was present : ")
            if g=="":
                pass
            else:
                cur.execute("update Employee set g=%s where emp_code=%s",(g,p))
            g=input("Enter the days of month in which of the employee was present : ")
            if h=="":
                pass
            else:
                cur.execute("update Employee set h=%s where emp_code=%s",(h,p))
        else:
            print("Task Aborted!") 

# Payroll Module

import mysql.connector as s
from tabulate import tabulate

import mysql.conector as s
con=s.connect(host="localhost", user="admin",passward="", database ="Payroll")
if con.is_connected()==False:
    print("Database not conected")
else:
    cur=con.cursor()

def Add_payroll_list():

    emp_code=int(input("Enter the employee code : "))
    emp_name=input("Enter the employee name : ")
    emp_dept=input("Enter the department of the employee : ")
    salary_from=int(input("Enter the date (Salary from) in YYYY_DD_MM format : "))
    salary_to=int(input("Enter the date (Salary to) in YYYY_DD_MM format : "))
    cur.execute("insert into payroll values(%s,%s,%s,%s,%s,%s)",(emp_code, emp_name, emp_dept, salary_from, salary_to ))
    con.commit()

def Display_payroll_list():

    cur.execute("select * from payroll")
    a=cur.fetchall()
    if a==None:
        print("No record found!")
    else:
        print(tabulate(data,headers=['emp_code','emp_name', 'emp_ph', 'emp_dept', 'emp_date_of_join', 'emp_add'],tablefnt='psql'))
        

def Search_payroll_list():

    n=input("Enter the employee code to be searched : ")
    cur.execute("select * from payroll where emp_code=%s",(n,))
    a=cur.fetchone()
    if a==None:
        print("Record Not found!")
    else :
        print(a)

def Delete_payroll_list():

    m=int(input("Enter the Employee code of the employee to be deleted : "))
    cur.execute("select * from payroll where emp_code=%s",(m,) )
    a=cur.fetchone()
        print(a)
        c=input("Do you want to delete this record y/n : ")
        if c=="y" or c=="Y":
            cur.execute("Delete from payroll where emp_code=%s",(m,))
            con.commit()
            print("Record Deleted Successfully.")
        else:
            print("Task Aborted!")

def Modify_payroll_list():

    p=int(input("Enter the employee code of the employee the modified : "))
    cur.execute("select * from payroll where emp_code=%s",(p,))
    a=cur.fetchone()
    if a==None:
        print("Record not found!")
    else:
        print(a)
        abc=input("Do you want to modify this record y/n : ")
        if abc=="y" or abc=="Y":
            name=input("Enter the New Employee Name or press enter to skip:")
            if name=="":
                pass
            else:
                cur.execute("update payroll set emp_name=%s where emp_code=%s",(name,p))
            department=int(input("Enter new employee department or press enter to skip : "))
            if department=="":
                pass
            else:
                cur.execute("update payroll set emp_dept=%s where emp_code=%s",(department,p))
            salary_from=input("Enter Employee salary from or press enter to skip : ")
            if salary_from=="":
                pass
            else:
                cur.execute("update payroll set salary_from=%s where emp_code=%s",(salary_from,p))
            salary_to =int(input("Enter Employee salary till or press enter to skip : ")
            if salary_to=="":
                pass
            else:
                cur.execute("update payroll set salary_to=%s where emp_code=%s",(salary_to,p))
            
        else:
            print("Task Aborted!")

# Salary Module
import mysql.connector as s
from tabulate import tabulate

import mysql.connector as s
con=s.connect(host="localhost", user="admin", passwd="123456789", database="Hospital")
if con.is_connected()==False:
    print("Error in Database Connecting")
else:
    cur=con.cursor()



def Display_Salary():

    cur.execute("select * from Salary")
    a=cur.fetchall()
    if a==None:
        print("No record found!")
    else:
        print(tabulate(data,headers=['emp_code','emp_name', 'emp_ph', 'emp_dept', 'emp_date_of_join', 'emp_add'],tablefnt='psql'))

def Search_Salary():

    n=input("Enter the employee code to be searched : ")
    cur.execute("select * from Salary where emp_code=%s",(n,))
    a=cur.fetchone()
    if a==None:
        print("Record Not found!")
    else :
        print(a)

def Delete_Salary():

    m=int(input("Enter the Employee code of the employee to be deleted : "))
    cur.execute("select * from Salary where emp_code=%s",(m,) )
    a=cur.fetchone()
        print(a)
        c=input("Do you want to delete this record y/n : ")
        if c=="y" or c=="Y":
            cur.execute("Delete from payroll where emp_code=%s",(m,))
            con.commit()
            print("Record Deleted Successfully.")
        else:
            print("Task Aborted!")

def Modify_Salary():

    p=int(input("Enter the employee code of the employee the modified : "))
    cur.execute("select * from payroll where emp_code=%s",(p,))
    a=cur.fetchone()
    if a==None:
        print("Record not found!")
    else:
        print(a)
        abc=input("Do you want to modify this record y/n : ")
        if abc=="y" or abc=="Y":
            name=input("Enter the New Employee Name or press enter to skip : ")
            if name=="":
                pass
            else:
                cur.execute("update Salary set emp_name=%s where emp_code=%s",(name,p))
            year=int(input("Enter new year or press enter to skip : "))
            if year=="":
                pass
            else:
                cur.execute("update Salary set y=%s where emp_code=%s",(department],p))
            salary_from=input("Enter Employee salary from or press enter to skip : ")
            if salary_from=="":
                pass
            else:
                cur.execute("update payroll set salary_from=%s where emp_code=%s",(salary_from,p))
            salary_to=int(input("Enter Employee salary till or press enter to skip : ")
            if salary_to=="":
                pass
            else:
                cur.execute("update payroll set salary_to=%s where emp_code=%s",(salary_to,p))
            
        else:
            print("Task Aborted!")

# Allowance Module

import mysql.connector as s
from tabulate import tabulate

import mysql.connector as s
con=s.connect(host="localhost", user="admin", passwd="123456789", database="Hospital")
if con.is_connected()==False:
    print("Error in Database Connecting")
else:
    cur=con.cursor()

def Add_Allowance():

    emp_code=int(input("Enter the employee code : "))
    emp_name=input("Enter the name of the employee : ")
    a=input("Enter the First allowance : ")
    b=input("Enter the Second allowance : ")
    c=input("Enter the Third allowance : ")
    cur.execute("insert into appointments values(%s,%s,%s,%s,%s)",(emp_code, emp_name, a, b, app_type))
    con.commit()


def Display_Allowance():
    
    cur.execute("select * from Allowance")
    a=cur.fetchall()
    if a==None:
        print("No record found!")
    else:
        print(tabulate(data,headers=['emp_code','emp_name', 'emp_ph', 'emp_dept', 'emp_date_of_join', 'emp_add'],tablefnt='psql'))

def Search_Allowance():

    n=input("Enter the employee code whose Allowance to be searched : ")
    cur.execute("select * from Allowance where emp_code=%s",(n,))
    a=cur.fetchone()
    if a==None:
        print("Record Not found!")
    else :
        print(a)

def Delete_Allowance():

    m=int(input("Enter the Employee code of the employee whose Allowance to be deleted : "))
    cur.execute("select * from Allowance where emp_code=%s",(m,) )
    a=cur.fetchone()
        print(a)
        c=input("Do you want to delete this record y/n : ")
        if c=="y" or c=="Y":
            cur.execute("Delete from Allowance where emp_code=%s",(m,))
            con.commit()
            print("Record Deleted Successfully.")
        else:
            print("Task Aborted!")

def Modify_Allowance():

    p=int(input("Enter the employee code of the employee the modified : "))
    cur.execute("select * from Allowance where emp_code=%s",(p,))
    a=cur.fetchone()
    if a==None:
        print("Record not found!")
    else:
        print(a)
        abc=input("Do you want to modify this record y/n : ")
        if abc=="y" or abc=="Y":
            name=input("Enter the New Employee Name or press enter to skip : ")
            if name=="":
                pass
            else:
                cur.execute("update Allowance set emp_name=%s where emp_code=%s",(name,p))
            FA=int(input("Enter First Allowance or press enter to skip : "))
            if FA=="":
                pass
            else:
                cur.execute("update Allowance set FA=%s where emp_code=%s",(FA,p))
            SA=input("Enter the Second Allowance from or press enter to skip : ")
            if SA=="":
                pass
            else:
                cur.execute("update Allowance set SA=%s where emp_code=%s",(SA,p))
            TA =int(input("Enter the Third Allowance or press enter to skip : ")
            if TA=="":
                pass
            else:
                cur.execute("update Allowance set salary_to=%s where emp_code=%s",(TA,p))
            
        else:
            print("Task Aborted!")

# Menu Driven Programme

import Employee as e
import Attendence as a
import Payroll as p
import Salary as s
import Allowance as x

print("*"*142)
print("                                                 ......PAYROLL MANAGEMENT SYSTEM.......                ")
print("*"*142)

while True:
    print("1. Employee Menu")
    print("2. Attendance Menu")
    print("3. Payroll Menu")
    print("4. Sallary Menu")
    print("5. Allowance menu")
    print("6. Quit")
    
ch=int(input("Enter your choice : "))
if ch==1:
    print("#"*142)
    print("                                                 ......Employee Menu.......                          ")
    print("#"*142)
    while True :
        print("1.Add New Employee")
        print("2.Display Employee Details")
        print("3.Search Employee Details")
        print("4.Delete Employee Details")
        print("5.Modify Employee Details")
        print("6.Return to Main menu")
        s=int(input("Enter your choice : "))
        if s==1:
            a.Add_New_Employee()
        elif s==2:
            a.Display_Employee()
        elif s==3:
            a.Search_Employee()
        elif s==4:
            a.Delete_Employee()
        elif s==5:
            a.Modify_Employee()
        elif s==6:
            break
        else :
            print("Enter The Correct Choice!")
            continue
        print("="*142)
    pass

if ch==2:
    print("#"*142)
    print("                                                 ......Employee Menu.......                          ")
    print("#"*142)
    while True :
        print("1.Add New Employee Attendance")
        print("2.Display Employee Attendance")
        print("3.Search Employee Attendance")
        print("4.Delete Employee Attendance")
        print("5.Modify Employee Attendance")
        print("6.Return to Main menu")
        s=int(input("Enter your choice : "))
        if s==1:
            a.Add_Employee_Attendance()
        elif s==2:
            a.Display_Employee_Attendance()
        elif s==3:
            a.Search_Employee_Attandance()
        elif s==4:
            a.Delete_Employee_Attendance()
        elif s==5:
            a.Modify_Employee_Attendance()
        elif s==6:
            break
        else :
            print("Enter The Correct Choice!")
            continue
        print("="*142)
    pass
elif ch==3:
    print("#"*142)
    print("                                                 ......Payroll Menu.......                          ")
    print("#"*142)
    while True :
        print("1.Add New Payroll List")
        print("2.Display Payroll List Details")
        print("3.Search Payroll List Details")
        print("4.Delete Payroll List Details")
        print("5.Modify Payroll List Details")
        print("6.Return to Main menu")
        s=int(input("Enter your choice : "))
        if s==1:
            p.Add_payroll_list()
        elif s==2:
            p.Display_payroll_list()
        elif s==3:
            p.Search_payroll_list
        elif s==4:
            p.Delete_payroll_list()
        elif s==5:
            p.Modify_payroll_list()
        elif s==6:
            break
        else :
            print("Enter The Correct Choice!")
            continue
        print("="*142)
    pass

elif ch==4:
    print("~"*142)
    print("                                                 ......Salary Menu.......                          ")
    print("~"*142)
    while True :
        print("1.Add New Salary List")
        print("2.Display Salary List")
        print("3.Search Salary List")
        print("4.Delete Salary List")
        print("5.Modify Salary List")
        print("6.Return to Main menu")
        s=int(input("Enter your choice : "))
        if s==1:
            s.Add_Salary()
        elif s==2:
            s.Display_Salary()
        elif s==3:
            s.Search_Salary()
        elif s==4:
            Delete_Salary()
        elif s==5:
            s.Modify_Salary()
        elif s==6:
            break
        else :
            print("Enter The Correct Choice!")
            continue
        print("="*142)
    pass

elif ch==5:
    print("#"*142)
    print("                                                 ......Allowane Menu.......                          ")
    print("~"*142)
    while True :
        print("1.Add Allowance List")
        print("2.Display Allowance List")
        print("3.Search Allowance List")
        print("4.Delete Allowance List")
        print("5.Modify Allowance List")
        print("6.Return to Main menu")
        s=int(input("Enter your choice : "))
        if s==1:
            x.Add_Allowance()
        elif s==2:
            x.Display_Allowance()
        elif s==3:
            x.Search_Allowance()
        elif s==4:
            x.Delete_Allowance()
        elif s==5:
            x.Modify_Allowance()
        elif s==6:
            break
        else :
            print("Enter The Correct Choice!")
            continue
        print("="*142)
    pass
elif ch==6:
    break
else:
    print("Enter The Correct Choice!")
print("#*"*142)
print("                                                 ......Programme End.......                          ")
