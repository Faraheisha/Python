c=int(input("Enter chemistry number "))
m=int(input("Enter math number "))
p=int(input("Enter Physics number "))
b=int(input("Enter biology number "))
total=c+m+p+b
if total > 300:
  print("A+ grade")
elif total > 200 and total < 300:
  print("A grade")
elif total > 100 and total < 200:
  print("B grade")
else:
  print("Fail")




