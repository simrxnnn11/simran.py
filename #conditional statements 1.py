#conditional statements 1
amount = int(input("enter the amount: "))
year = int(input("enter the number of year: "))
interest=0
if (year<10):
    interest=12 
if (year>=10):
    interest=18

total_interest_value=(amount*interest)/100
EMI=(amount+ total_interest_value)/12*year
print(EMI)