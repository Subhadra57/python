# num1 = 10
# num2 =15

# if num1 >= num2:
#     print(True)
# else:
#     print(False)

num1 = int(input("enter your  first number: "))
num2 = int(input("enter your  second number: "))
num3 = int(input("enter your  third number: "))

if num1 > num2 and num1> num3:
    print("greater number is: ",num1)
elif num2 > num1 and num2> num3:
    print("greater number is",num2)
else:

    print("greater number is",num3)
