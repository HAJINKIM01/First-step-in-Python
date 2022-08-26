#Fix the code below 👇

print("Day 1 - String Manipulation")
print("String Concatenation is done with the "+" sign.")
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")
# I learned how to use print function and ++, \n, and debugging. 
# For now, I will be studying about input function.
input ("what is your name") # it will allow user to type the answer. 
print ("hello " + input("what is your name?")+ " it is very nice to meet you")

# if I want to count the name.
print(len(input("what is your name?")))

# I learned saving the variable from the input by using =. 
#if I want to rewrite print(len(input("what is your name?"))).
name = input ("what is your name"?)
lenth = len(name)
print(lenth)
          
# first Project "BAND NAME GENERATOR!"

print("welcome to band name generator!")
name_city= input("what's name of the city you grew up in?\n")
name_pet = input("what is the name of your pet?\n")
print(name_city +" "+ name_pet + " is your decent band name!")


#day2 , making tip calculator,
# Integer, if I want to do the mathmatical calculation, I need to use Integer.
# if I use print("123"+"123"), it will accept number as letter not the number.
# so, when I need to calculator some number wihtout decimal, I need to use Integer. 
#float= it is some number with the decimal points.
#Boolean, only two possible value, True or false. 

print("you name has" + integer + "characters") it will end up with the error because it has string and error in the ().
if I want to convert integer into string, I nedd to use "str" and if I want to check the type of data, I need to use print(type(x))

#BMI calculator
# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
new_height=int(height)
new_weight=int(weight)

BMI=((new_weight/100)/(new_height*new_height))
New_BMI=str(BMI)

print("Your Official BMI IS "+New_BMI)

#To manage the decimal
Print(round(8/3,2))

# life calculator
# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

year_left =90-int(age)
print(str(year_left)+"years has left to death")
week_left=year_left*52
day_left=week_left*7
print(f"you have {year_left} years, {week_left} weeks,and {day_left} days.")

#tip : when I want to make some diagram, use Draw.io! 

Print("wellcome to the rollercoaster)
height=input(int("what is your height?")
if height>120:
              Print("you can ride this rollarcoaster!")
Else: 
              Print("you have to be taller to ride this rollarcoaster!")
 # Comparison Operators
   >,<,>=,<=, important(==equal to, and != not equal to)
 # finding odd or even number by using if else function and %= it means dividing by x number.
# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if number % 2==0:
  print("even")
else:
  print("odd")
             
# combination of if,elif, and else. 
height = int(input("what is your height? "))
 
if height >= 120:
  age=int(input("how old are you?"))
  if age< 10:
    print("price is $10")
  elif age<20:
    print("price is $20")
  else:
    print("price is $100")
else:
  print("we can't enter")
#leap year 찾는건데 나는 여기서 좀 해까려서, year%4!=0,year and %100==0 or %400!=0 print(not leap year) else: print("leap year).
#근데 정답에서는 좀 달랐음.(이렇게 이거아니면 이거고 이거아니면 이거다** 이게중요!. 하면서 몰아가면서 찾는거 자주보기!!)
year=int(input("what year?") )

if year%4==0:
  if year%100==0:
    if year%400==0:
      print("leap year")
    else:
      print("not leap year")
  else:
    print("leap year")  
else:
  print("not leap year")
 # comparing between if/elif/else and multiple if.
 # when I use if/elif/else에서는 3개중에 조건에 적합한 하나에 들어가는거임. 하지먄 multiple if문에서는 조건에 적합한 모든것들이 들어가는것!
#띄어쓰기 조심            
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print("Child tickets are $5.")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7.")
  else:
    bill = 12
    print("Adult tickets are $12.")
  
  wants_photo = input("Do you want a photo taken? Y or N. ")
  if wants_photo == "Y":
    bill += 3
  
  print(f"Your final bill is ${bill}")

else:
  print("Sorry, you have to grow taller before you can ride.")
  #연습 롯데월드
print("롯데월드에 오신걸 환영합니다")
티켓종류=str(input("어떤종류의 티켓을 구매하시겠습니까?자유이용권 or 빅4\n"))
bill=0

if 티켓종류=="자유이용권":
  print("자유이용권 가격은 5만원입니다.")
  bill=50000
  주차권=input("주차권(10,000원) 구매하시겠습니까?네 OR 아니요\n")
  if 주차권=="네":
    bill+=10000
    print(f"최종금액은 {bill}원 입니다") 
  else:
    print(f"최종가격은{bill}원 입니다")
elif 티켓종류=="빅4":
  print("빅4 가격은3만원입니다.")
  bill=30000
  주차권=input("주차권(10000원) 구매하시겠습니까?네 OR 아니요\n")
  if 주차권=="네":
    bill+=10000
    print(f"최종금액은 {bill}원 입니다") 
  else:
    print(f"최종가격은 {bill}원 입니다")  
else:
  print("영업방해말고 돌아가주십시오")

#Pizza 주문계산기
             # 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆
bill = 0
#Write your code below this line 👇
if size=="S":
   bill+=15
elif size=="M":
   bill+=17
else:
   bill+=20

if add_pepperoni=="Y":
  if size=="S":
     bill+=2
  else:
     bill+=3
if extra_cheese=="Y":
  bill+=1
print(f"your final bill is ${bill}")
 
#logical operator. and or not!
