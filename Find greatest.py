n1 = int(input("Enter the first number"))
n2 = int(input("Enter the second number"))
n3 = int(input("Enter the third number"))
if (n1<n2) and (n2>n3):
    print("Greatest number is",n2)
elif (n1>n2) and (n1>n3):
    print("Greatest number is",n1)
else:
    print("Greatest is",n3)
