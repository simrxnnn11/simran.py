# class Person:
#     def __init__ (self,name,age):
#         self.name = name
#         self.age = age

#     def introduction(self):
#          print(f"Hii myself {self.name} and my age is {self.age}years old.")

# person1 = Person("aman",29)
# person1.introduction()


# class student:

#     def __init__(self,name,rollno,marks):
#         self.name= name
#         self.rollno=rollno
#         self.marks=marks

#     def student_details(self):
#         print(f"name = {self.name}")
#         print(f"rollno = {self.rollno}")
#         print(f"marks = {self.marks}")

# teacher=student("simran",8,89)
# teacher.student_details()


# class bank_account:
#     def __init__(self,account_number,balance):
#         self.account_number=account_number
#         self.balance=balance

#     def bank_details(self):
#         print(f"I deposited 10,000 and withdraw 2500 so my remaining balance is {self.balance} as I had 20,000 already in my this {self.account_number} saving account ")

# me=bank_account(1024156423112,25700)
# me.bank_details()
     

# sec c
# class employee:
#     def __init__(self,name,salary):
#         self.name =  name
#         self.salary = salary

# class manager(employee)  :

#     def __init__(self,name,salary,bonus):
#         super().__init__(name,salary)
#         self.bonus=bonus

#     def calculate_total_salary(self):
#         total = self.salary + self.bonus
#         print(f"total salary for {self.name}: ${total} ")

# HR= manager("aman",50000,4000)
# HR.calculate_total_salary()

# class Employee:
#     name="aman"
#     salary=30000
# class Manager:
#     bonus=2900





