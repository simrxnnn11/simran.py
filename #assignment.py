# TO GET EVEN AND ODD NUMBERS
 #start=1
#while(start<=10):
 #   if(start%2==0):
  #      print(start)
   #     start+=1

# odd numbers
#start=1
 #while(start<=15):
   ##   print(start)
     #  start+=1


# STUDENT GRADES
#marks=int(input("enter the marks= "))
#if marks>=90 and marks<=100:
 #   print("grade=A")
#elif marks>=80 and marks<=89:
 #   print("grade=B")
#elif marks>=70 and marks<=79:
 #   print("grade=C")
#elif marks>=60 and marks<=69:
 #   print("grade=D")
#else :
 #   print("grade=F")    



# LARGEST NUMBER
#number1=int(input("enter the first number= "))
#number2=int(input("enter the second number= "))
#number3=int(input("enter the third number= "))
#if number1>number2 and number1>number3:
#    print("number1 is largest number")
#elif number2>number3 and number2>number1:
#    print("number2 is largest number")
#elif number3>number1 and number3>number2:
#   print("number3 is largest number")
#else:
#   print("all are equals")



# LEAP YEAR CHECKER
#year=int(input("enter the year= "))
#if year%4==0 and year%100!=0:
#    print("it is a leap year")
#else:
#    print("it is not a leap year")



# VOTING ELIGIBILITY
#Age=int(input("enter the age= "))
#if Age>18:
#    print("they are eligible to vote")
#elif Age<18:
#    print("they are not eligible to vote")
#else:
#    print("not found")



# POSITIVE , NEGATIVE OR ZERO
#number=int(input("enter the number= "))
#if number>0:
#   print("it is a positive number")
##   print("it is a negative number")
#elif number==0:
#   print("it is a zero")
#else:
#   print("not found")



#PASSWORD VALIDATOR
#password=input("enter the password= ")
#if password == "simran123":
#    print("Acess granted")
#else:
#    print("Acess denied")



# BILL CALCULATOR
#unit=int(input("enter the number of units consumed= "))
#if unit>=0 and unit<=100:
#    print("bill amount= unit*5")
#elif unit>=101 and unit<=300:
#    print("bill amount= unit*8")
#elif unit>=300:
#    print("bill amount = ", "unit*10")
#else: 
#print("error")


#CHECK THE NUMBER IS IN RANGE OR NOT
#number=int(input("enter the number= "))
#if number>=10 and number<=50:
#    print("number is in given range")
#else:
#    print("number is not in given range")



#TRIANGLE TYPE CHECKER
side1=int(input("enter the length of side1= "))
side2=int(input("enter the length od side2= "))
side3=int(input("enter the length of side3= "))
if side1==side2==side3:
    print("it is an equlaterlal tiangle")
elif side1==side2 and side1!=side3:
    print("it is an isosceles triangle")
elif side1!=side2!=side3:
    print("it is an scalene triangle")
else:
    print("error")