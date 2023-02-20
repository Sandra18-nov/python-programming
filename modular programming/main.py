# import functions
# x=functions.add(34,12)
# print(x)

# y=functions.subtract(34,12)
# print(y)


# from functions import subtract
# y=subtract(34,12)
# print(y)

#import operators module
import operators
import others
import trig


#build a better calculator
x=others.cube(3)
y=operators.add(7,8)

print(y)

#get numbers
operator=input("enter operator:")
if operator=="cube":
    num=eval(input("enter number:"))
    x=others.cube(num)
    print(x)

elif operator=="sin":
  angle=eval(input("enter angle in degrees:"))
  sin_of_angle=trig.get_sine(angle)
  print(sin_of_angle)

elif operator=="tan":
  angle=eval(input("enter angle in degrees:"))
  tan_of_angle=trig.get_tan(angle)
  print(tan_of_angle)


else:
      num1=eval(input("enter number 1:"))
      num2=eval(input("enter number 2:"))


      if operator=="+":
        x=operators.add(num1,num2)
        print(x)


      elif operator=="-":
        x=operators.subtract(num1,num2)
        print(x)

      elif operator=="/":
        x=operators.divide(num1,num2)
        print(x)
 
      elif operator=="*" or"x" or"X":
        x=operators.multiply(num1,num2)
        print(x)

