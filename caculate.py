def add(x,y):
    return x+y

def subtruct(x,y):
    return x-y
    
def multiply(x,y):
    return x*y

def devition(x,y):
    return x/y


print ("Select operation")
print ("1. add")
print ("2. subtruct")
print ("3. multiply")
print ("4. devition")

choice=input("Enter choice(1/2/3/4):")
num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))

if choice=="1":
 print(num1,"+",num,"=",add(num1,num2))
else choice =="2":
 print(num1,"-",num2,"=",subtruct(num1,num2))
else choice =="3":
 print(num1,"*",num2,"=",multiple(num2,num2))
else choice =="4":
 print(num1,"/",num2,"=",divition(num1,num2))
else:
 print("invalid input")
 
