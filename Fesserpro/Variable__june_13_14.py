# June 13 - Variables

stock_price=float(input("Stock Price"))
stop_perc=5
stop_loss=round(stock_price*((100-stop_perc)/100),2)
print(stop_loss)

# June 14 - String

i1="10"
i2="20"
# we can add 2 strings
print(i1+i2) 

# we can multiply string
print(i1*10)

# no other mathematical operations will not work

# Tycasting- converting one type of value to another value
# int,float,str
name="john"
age=32
intro= "my name is "+name+" and my age is "+str(age)
print(intro)

# type function will help us to know the type of the variable.

# fstring- automatically do the typecasting.
name="john"
age=32
intro1= "my name is "+name+" and my age is "+str(age)
intro2=f"my name is {name} and my age is {age}"
print(intro1)
print(intro2)

# Escape sequence
print("hello \n world")
      
# question1
num=44.589
numprint=int(num*100)/100
print(numprint)

# question 2
num1=10
num2=20
temp=num1
num1=num2
num2=temp
print(num1,num2)


     
      