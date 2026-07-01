num1 =int(input("Enter 1st number: "))
num2 =int(input("Enter 2nd number: "))
#print (type(num1))
#print (type(num2))

choice = input("enter your choice of operation: ( option + - * / ) ")

if choice == '+' :
  sum = (num1) + (num2)
  print ("Sum of num1 and num2 is: ", sum)

elif choice == '-' :
  sub = (num1) - (num2)
  print ("Subtraction of num1 and num2 is: ", sub)

elif choice == '*' :
  mul = (num1) * (num2)
  print ("Multiplication of num1 and num2 is: ", mul)

elif choice == '/' :
  div = (num1) / (num2)
  print ("Division of num1 and num2 is: ", div)

else:
  print ("Input is invalid")


