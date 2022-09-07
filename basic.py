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
#love game
print("welcome to LoveGame!\n")
Name_1=input("what is your name?")
Name_2=input("what is his name?")
combname=(Name_1+Name_2).lower()

n1=combname.count("t")
n2=combname.count("r")
n3=combname.count("u")
n4=combname.count("e")

sumoftrue=str(n1+n2+n3+n4)

n5=combname.count("l")
n6=combname.count("o")
n7=combname.count("v")
n8=combname.count("e")

sumoflove=str(n5+n6+n7+n8)
total=int(sumoftrue+sumoflove)


print(f"your love score is {total}")

if total>10 and total>90:
  print("Best")
elif total<=90 or total>=10:
  print("Good")
else:
  print("bad")
#list. listofstates=["a","b"."C"]. print(listofstates[1]), listofstate.append("ar") (한개의 데이타추가), listofstate.expend("x","y")더 많은 리스트를 추가. 
             
#random. 1st, Import random. random,randint(0,1). 
# split function.
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
#who will be paying?
listofpeople=[1,2,3,4,5,6]
import random
print(listofpeople[random.ramdint(0,5)]
      both are same
import random
listofpeople=[1,2,3,4,5,6]
print(random.choice(listofpeople))
      
 roop: for fruit in fruits:
      print(fruits)
      
 #Practice for Roop, round!
#finding average number, and max
      
#Write your code below this row 👇
student_heights=[143,255,332,334,222,443]
total_numberofstudent=0
for student in student_heights:
  total_numberofstudent+=1
print(total_numberofstudent)

total_height=0
for student in student_heights:
  total_height+=student

print(total_height)

print(round(total_height/total_numberofstudent,2))

 

highest=0
for student in student_heights:
  if (student)>(highest):
    highest=student
print(highest)
      
#sum of even number
total_number=0

for number in range(2,101,2):
  total_number+=number
  
print(total_number)
or
total_number=0
for number in range(1,101):
      if number % 2==0:
          total_number+=number
print(total_number)
      
#가위바위보
 import random

me=int(input("what do you choose?"))

computer=random.randint(0+1,me+1)
print(f"computer choose {computer}")
if me==2 and computer==0:
  print("you won")
elif me<computer:
  print("you lost")
elif computer==me:
  print("draw")
else:
  print("you type invalid number, you lost")
      
  #defining Functions:
  def my_function():
          print("hello")
          print("bye")
      #it means that! do hits then do this finall do this.
      in this defining, indentation is very important.
  def my function():
      if a>3:
          print ("wow") 이런식으로 4 spaces! 
      
  #Reeborg's world.
      def right():
    turn_left()
    turn_left()
    turn_left()
def tmove():
    move()
    move()
def solution():
    move()
    turn_left()
    move()
    right()
    move()
    right()
    move()
    turn_left()

for jump in range(0,6):
    solution()
# by using while, 
number_huddle=6
while number_huddle >0"
      jump()
      number_huddle-=-1
#for 에서 차이점
list_of_states=["a","b","c","d","e",
"f"]

for i in list_of_states:
  print("its your",i)

for number in range(0,6):
  print(f"its your {list_of_states}")
 이차이를 알아야됨 !      
      
# while something_is_ture, 
   #do this 
    #do this
     #then do this untile the comdition become false. 
      
#def math, def, naming, parameter.
#Write your code below this line 👇
import math
def paint_calc(height,width,cover):
  area= height*width
  number= math.ceil(area/cover)
  print(f"you need {number}")
  


#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

#defining and using if function by making turn false. 
#Write your code below this line 👇

def prime_checker(number):
  is_prime=True
  for i in range(2,number):
    if number % i ==0:
      is_prime = False
  if is_prime:
    print("its prime number")
  else:
    print("its not prime number")
    


#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)

#dictionary
      {key:value}
ex: key:bug value: an error in a program that prevents the program from running as expected. 
      programming_dictionary={"bug":"an error in a program that prevents the program from running as expected."}
          if I want to make more dictionary {"1":"~~","2":"~~~", 콤마로 이어가면서 추가하면됨 그리고 마지막에 }
print(programming_dictionary["key"])
    #empty.
      Prombramming_dictionary={}
    #adding
      programming_dictionary["add"]="valude"
    #editing
      programming_dictionary["bug"]="new value"
       
   #loop through a dictionary
      for key in program_dictionary:
          print(key)
          pritn(programing_dictionary[key])
  
      
      
    #grading program with for, dictionary
      student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grade={}

#TODO-2: Write your code below to add the grades to student_grades.👇
for student in student_scores:
  score= student_scores[student]
  if score>90:
    student_grade[student]="outstanding"#adding to dictionary
  if score>80:
    student_grade[student]="Exceeding expectation"#adding to dictionary
  if score>70:
     student_grade[student]="average"#adding to dictionary
  else:
     student_grade[student]="failed"#adding to dictionary
    
  
    

# 🚨 Don't change the code below 👇
print(student_grade)


#네스팅 nesting
travel_log ={"Franch":["paris", "Lille", "Dijon"]} dictionary with listing
      listing in listing
      ["A","B",["C","D"]]
#EX) 

 travel_log={
   "France":{"cities_visited":["paris","Lille","Dijon"], "total_visits":12},
 }
      
  이거는 지금 
 {
   key: [list],
   key2: {dict},
 }
이형식임 
 programming_dictionary={
   "bug":"wfefwefewf.",
   "function":"weflejwflk",
   ,
 } 이런 형식으로 정리. 
  
 adding new entry in dictionary
 
  programming_dictionary["loop"]="it is very useful."
 
 editing exiting dictionary
    
  Programming_dictionary["bug"] = " new material." 
      
   #loop through a dictionary
   
      for key in programming_dictionary
          print(key)
          print(programming_dictionary[key]) 
      #이러면 다나옴. #for loop 에 집중 ! 

      # bidding_finished=false
      
      while not bidding_finished: 여기 뜻은 만약에 bidding_finished 가 false 이면 계속 반복해라. 
      
 #[bidding progect]
      
from replit import 
      
from art import logo
print(logo)

bids={}
finished_bidding=False


def finding_highest_bidder(bidding_record):
  highest_bid = 0
  highest_bidder = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid=bid_amount
      highest_bidder = bidder
  print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")
    
 
while not finished_bidding:
  name=input("what is your name?")
  price=int(input("what is your bidding price? $"))
  bids[name]=(price)
  should_continue=input("are there any other bidder? Type 'yes or no'.")
  if should_continue=="no":
    finished_bidding=True
    finding_highest_bidder(bids)
  elif should_continue=="yes":
    clear()      
      
  #functions with outputs
      
   def format_name(f_name,L_name):
      if f_name=="" or l_name=="":
        return " you didn't provide valid inputs."
      format_f_name=f_name.title()
      format_l_last=l_name_title()
      return f"Result:{formated_f_name} {formated_l_name}"
      
   print(format_name(input("what is your first name?"),input("what is your name?")))
      
      #blackjack
      
import random
from replit import clear
from art import logo


def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card
  

def calculate_score(cards):
  if sum (cards)==21 and lens(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21 :
    cards.remove(11)
    cards.append(1)
  return sum (cards)

def compare(user_score, computer_score):
  if user_score > 21 and computer_score > 21:
    return "you went over, you lost"
    
  if user_score == computer_score:
    return "draw"
  elif user_score == 0:
    return " you won with blackjack"
  elif computer_score== 0:
    return " you lost with blackjack"
  elif user_score > 21:
    return " you went over, lost"
  elif computer_score > 21:
    return " you won"
  elif user_score > computer_score:
    return "you won"
  else:
    return " you lost"



  
def play_game():
  print(logo)
  
  user_cards = []
  computer_cards = []
  is_game_over = False

  
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  while not is_game_over:

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f"your card is {user_cards}, and your score is {user_score}")
    print(f"computer's first card is {user_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score> 21:
      is_game_over = True
    else:
      user_should_deal =input("do you want to get one more cards? 'y'or'n'?")
      if user_should_deal == "y":
        user_cards.append(deal_card())
      else:
        is_game_over=True
  
  while computer_score!=0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"your final score is {user_score} and your cards {user_cards}")
  print(f"computer's final score is {computer_score} and computer's card {computer_cards}")
  print(compare(user_score, computer_score))

while input("do you want to play blackjack?'y'or 'n'")=='y':
 clear()
 play_game()
    
        
