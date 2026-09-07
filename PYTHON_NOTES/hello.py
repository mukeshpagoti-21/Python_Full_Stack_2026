'''
------------------------------------------------------------------------------------------------------------------------18/08
concatination
-------------
--> the  +  will behave two ways for numaric it works normally
    and for other datatypes like string,list,tuple it conactinate

operators
---------
--> the operators 
1.arthmatic operators
---------------------
+ ---> to add the values
num =12
num_2 =32
print(num + num_2)




2.assignment operators
----------------------
= , += , -= , *= , %= , /=

+= -->is increment operartor
a =0
print(a)

3.comparison operators
4.logical operators
5.identity operators
6.membershhip operators
7.bit wise operators
--------------------
& --> Bit wise and
print (5 & 3)


| --> Bit wise OR
print (5 | 3)

^ --> Bit wise XOR
print (5 ^ 6)

>> --> right shift
print (10 >> 2)
10 - 1010
2  - 0010

<< --> left shift
3 - 0011
2  - 0010
---------------------------------------------------------------------------------------------------------------19/08
INPUT FORMATING
---------------
interger --> int(input())
num = int(input("enter the num :- "))
print(num)

float --> float(input())
num = float(input("enter the number decimal  :- "))
print(num)

string -->input("enter your name :- ")
num = input("enter your name :- ")
print(type(num))

list --> 1 2 3 ---> [1, 2, 3]
num = list(map(int,input().split()))
print(num)

tuple ---> 1 2 3 ---> (1,2,3)
num = tuple(map(int,input("enter :- ").split()))
print(num)

set   ---> 1 2 3 ---> {1,2,3}
num = set(map(int,input("enter :- ").split()))
print(num)

OUTPUT FORMATING
----------------

word = eval(input("enter the word : "))
print(type(word))

name = "munna"
age = 22
print("my name is :-",name,"&","my age is :-",age)

name = "Munna"
age = 22
print(f"my name is:- {name} .my age is :-{age} , so i am eligible for this")

name = "Munna"
age = 22
print("my name is %s and my age is %d years old" %(name,age))
--------------------------------------------------------------------------------------------------------------20/08
INDEXING
--------
1.positive indexing
-------------------
positive indexing starts with "0"
num = [1,2,3,4]
print(num[2])

2.negative indexing
-------------------
negative indexing starts with "-1"
num = [1,2,3,4]
print(num[-4])

len()
----
---> it will find the length of inside the variable
txt = "my name munna"
print(len(txt))

slicing
-------
txt = "my name munna"
print(txt[3:8])
print(txt[3:])
print(txt[:8])

txt = "my name munna"
print(txt[::-1])


upper()
------
--->used to convert small characters to capital characters
txt = "my name munna"
print(txt.upper())

lower()
------
--->used to convert capital to lower 
txt = "MY name munna"
print(txt.lower())

index()
-------
--->used to know the index position of an character
txt = "MY name munna"
print(txt.index("a"))

replace()
--------
--->it will replace the old sub-string to new sub string
txt = "MY name munna"
print(txt.replace("munna","nani"))

split()
-------
--->this is method used to separate the string  based on giving sub strings
txt = "MY name munna"
print(txt.split("m"))

count()
------
--->this method is used for to count specific words


---------------------------------------------------------------------------------------------------------------------21/08
indexing
--------

all = [12,[1,32,"nani",2],[32,"munna"],[21,2004,7,(4,[2004,4])]]
print(all[2][2][])



data = ["python",[1,2,(90,"details",[67,0]),(78,"student")]]
print(data[1][2][1][2])


slicing
-------
data = [1,2,3,4,5]
print(data[2:4])


data = [1,2,3,4,5,100]
print(data[0:4])

methods :-
-------
append()
--------
---> append() method is used to add new items at the end of the the index

eg:-
a = [21]
print(a)
a.append(7)
print(a)
a.append(2004)
print(a)

extend()
-------

a = [21,7]
a.extend("nani")
print(a)

pop()
----
-->pop() is used to remove items from the list and it
   will delete based on the index position

a = [21,7,"nani"]
a.pop(1)
print(a)


remove()
-------
--->but in this remove we can directly remove the value or object see the example
    and it remove only one at all.

a = [21,7,"nani",321432]
a.remove("nani")
print(a)


#input() → reads a whole line of text from the user (like "101 101 202 2022")

#.split() → splits that line into a list of strings: ["101", "101", "202", "2022"].

#map(int, ...) → converts each string into an integer: [101, 101, 202, 2022]

#tuple(...) → stores them as an immutable tuple: (101, 101, 202, 2022)
------------------------------------------------------------------------------------------------------------------------24/08
operartions :-
-----------


union()
-------
--> the union() will combine two sets into a single set

data = {1,2,3,4}
data_2 = {2,4,5}

print(data.union(data_2))
print(data | data_2)


intersection()
--------------
-->it will gives us only common element from both sets

data = {1,2,3,4}
data_2 = {2,4,5}

print(data.intersection(data_2))
print(data & data_2)


difference()
-----------
-->it will display the different elements from set_1 ,but not the set_2 elements

data = {1,2,3,4}
data_2 = {2,4,5}

print(data.difference(data_2))
print(data - data_2)


symmetric_difference()
----------------------
-->different elements from the both

data = {1,2,3,4}
data_2 = {2,4,5}

print(data.symmetric_difference(data_2))
print(data ^ data_2)


methods:-
---------

add()
----
-->add() method only one element at a time

data = {1,2,3,4}
print(data)
data.add(10)
print(data)


update()
--------
-->we can add more one eleement by using update method

data = {1,2,3}
num = {40,50,60}
print(data)
data.update([4,5,6])
print(data)
data.update(num)
print(data)

remove()
--------
--->remove() method will delete the given elememt from the set
--->if the element is not there it will raise the error

data = {1,2,3,3,4,5}
data.remove(3) #in this remove we will give definetly given value in the set either it willll throw the error
print(data)
data.remove(2)
print(data)
o/p : {1, 2, 4, 5}
      {1, 4, 5}

discard()
---------
--->if the element is not there it will not raise the error
--->discard() will use to delete the value , if the give element is not in set it will give the original data

data = {1,2,3,3,4,5}
data.discard(10)
print(data)
data.discard(2)
print(data)

o/p :
{1, 2, 3, 4, 5}
{1, 3, 4, 5}

clear()
-------
--->method is used to delete the all elements from the set and will return empty set 

data = {1,2,3,3,4,5}
data.clear()
print(data)

o/p:
set()
---------------------------------------------------------------------------------------------------------------------25/08
accessing
--------
--> dict can access by calling key ,we will get value from that key
syntax --> dict["key"]

data ={"name" : "nani",
       "balance" : 3000,
       "adhr" : 8106155301,
       "pan" : "JXPMB2OKM",
       3:[21,4]}

print(data["pan"])
o/p: JXPMB2OKM

--> get() method is also used to get the value from that key
syntax-->dict.get("key")
data ={"name" : "nani",
       "balance" : 3000,
       "adhr" : 8106155301,
       "pan" : "JXPMB2OKM",
       3:[21,4]}
       print(data.get("adhr"))
    o/p: 8106155301

update()
-------
-->Method is update a key, incase if the key is not present inside dict
   then it add that key : value
synatx-->dict.update({key : value})
data ={"name" : "nani",
       "balance" : 3000,
       "adhr" : 8106155301,
       "pan" : "JXPMB2OKM",}
data.update({"name" : "munna"})
print(data)
o/p:{'name': 'munna', 'balance': 3000, 'adhr': 639668255534, 'pan': 'JXPMB2OKM'}

-->there is another way to update a key
syntax-->dict.["key"]
data ={"name" : "nani",
       "balance" : 3000,
       "adhr" : 8106155301,
       "pan" : "JXPMB2OKM",}
data["mobile_no"] = 9676630139
print(data)
o/p : {'name': 'nani', 'balance': 3000, 'adhr': 639668255534, 'pan': 'JXPMB2OKM', 'mobile_no': 9676630139}

values()
-------
-->values() method is used to print the all values what we given in dict
data ={"name" : "nani",
       "balance" : 3000,
       "adhr" : 8106155301,
       "pan" : "JXPMB2OKM"}

print(data.values())
o/p: dict_values(['nani', 3000, 8106155301, 'JXPMB2OKM'])

keys()
-----
-->keys() method is used to print all  keys in dict
data ={"name" : "nani",
       "balance" : 3000,
       "adhr" : 8106155301,
       "pan" : "JXPMB2OKM"}

print(data.keys())
o/p : dict_keys(['name', 'balance', 'adhr', 'pan'])

items()
------
-->this method will get the key : value seperated from the dict
syntax --> dict.items()
data ={"name" : "nani",
       "balance" : 3000,
       "adhr" : 8106155301,
       "pan" : "JXPMB2OKM"}

print(data.items())
o/p: dict_items([('name', 'nani'), ('balance', 3000), ('adhr', 8106155301), ('pan', 'JXPMB2OKM')])

del
---
data ={"name" : "nani",
       "balance" : 3000,
       "adhr" : 8106155301,
       "pan" : "JXPMB2OKM"}

del data["name"]
print(data)
o/p : {'balance': 3000, 'adhr': 8106155301, 'pan': 'JXPMB2OKM'}

clear()
-------
--> method is used to clear all data from the dict
syntax --> dict.clear()
data ={"name" : "nani",
       "balance" : 3000,
       "adhr" : 8106155301,
       "pan" : "JXPMB2OKM"}
print(data.clear())
print(data)
o/p : {}

----------------------------------------------------------------------------------------------------------------------------26/08
IF STATEMENT
------------
--> if condition become true ,then it will execute inside block of code.
--> incase it become false ,then it will never entrry inside the block.

score = 69
if score >= 70:
 print("your current score is 69")
print(f"score is : {score}")

o/p : score is : 69

IF-ELSE
-------
--> if statement is false directly print the else


percentage = 77
if percentage <=76:
    print(f"you are not eligible to the drive due to , percentage is {percentage}")
else:
    print(f"you are eligible to drive due to ,percentage is {percentage}")

o/p : you are eligible to drive due to ,percentage is 77

ELIF
----
-->elif statement is used to check more possible 

a = 100
b = 200
c = 300

if a > b and a > c:
    print(a)
elif b > c and b > a:
    print(b)
else:
    print(c)
o/p : 300

NESTED IF
---------
--> if inside an if statement is called nested if


ex
--
app_details = {'pin' : 2004}

import random

user_login = int(input("enter the app login pin :- "))
otp = random.randint(1000,9999)

if user_login == app_details['pin']:
    print("pin is correct")
    print(f"your otp is : {otp}")
    user_otp = int(input("enter the otp :- "))
    if user_otp == otp:
                print("welcome to the app")
    else:
               print("access deined to the app")
else:
    print("pin is incorrect")

o/p : enter the app login pin :- 2004
      pin is correct
      your otp is : 2978
      enter the otp :- 2978
      welcome to the app
ex
--
marks = int(input("enter your marks :- "))

if marks >= 90 :
    print("+A")
elif marks >= 80 :
    print("A")
elif marks >= 70 :
    print(" +B ")
elif marks >= 60 :
    print(" B ")
else:
    print("you are fail in this semester " )
    
o/p: enter your marks :- 59
      you are fail in this semester 

ex
--
a = 100
b = 200
user_input = int(input("enter \n1.add \n2.sub \n3.mul \n4.pow \n "))

if user_input == 1:
    print(a + b )
elif user_input == 2:
    print(a - b)
elif user_input == 3:
    print(a * b)
elif user_input == 4:
    print(a ** b)
else:
    print("invalid input")

o/p: enter 
     1.add 
     2.sub 
     3.mul 
     4.pow 
       5
     invalid input

----------------------------------------------------------------------------------------------------------------------------------27/08
for statement
-------------
-->for loop is used to iterate over a sequence or iterable
   data types

nums = "python"

for num in nums:
    print(nums)



else in for
----------
-->The else block runs only if the loop finishes without a break.
    If the loop is stopped early using break, the else part is skipped.
nums = "python"

for num in nums:
    print(nums)
else:
    print("ended")


BREAK
 
-----
nums = [1,2,3,4,5]

for num in nums:
    if num == 4:
        print("founded")
        
        break
    
    else:
       print("not founded")

CONTINUE
--------
--> skip the value what we give in the if statement , and print the balance nums

nums = [1,2,3,4,5]

for num in nums:
    if num == 4:
        continue
    print(num)
    
o/p:1,2,3,5

PASS
----
--> a pass is called as space holder ,that is used after
    statement like (if ,for ,else) not to raise ANY error

nums = [1,2,3,4,5]
for num in nums:
    if num == 4:
      pass
      
o/p : 

ASSERT
------
-->in Python, assert is a keyword used for debugging.
   It helps you test whether a condition is true while your program is running.
   if condition is false rise the error

num = 20

assert num >=21, "bad error"
print("good")

o/p :  assert num >=21, "bad error" 
       AssertionError: bad error


----------------------------------------------------------------------------------------------------------------------------------28/08

nums = int(input("enter the number:- "))

for i in range (2,nums+1):
    count = 0
    for j in range (1,i+1):
        if i % j == 0:
          count += 1
    if count == 2:
        print(f"{i} is prime")
star 
----
num = int(input("enter the no.of stars : "))
for i in range (1,num+1):
    for j in range (1,i+1):
          print("?",end = " ")
    print()
o/p: enter the no.of stars : 5
     ? 
     ? ? 
     ? ? ? 
     ? ? ? ? 
     ? ? ? ? ? 
ex
--
num = int(input("enter the no.of stars : "))
count = 1
for i in range (1,num+1):
    for j in range (1,i+1):
        print(count,end = " ")
        count += 1
    print()
    
o/p:enter the no.of stars : 5
    1 
    2 3 
    4 5 6 
    7 8 9 10 
    11 12 13 14 15 

--------------------------------------------------------------------------------------------------------------------------------------------29/08
ex
--
ran = [20,21,22,23,30]

for j in ran:
    if j % 2 == 0:
        print(f"{j} is even")
    else:
        print(f"{j} is odd")
        
o/p: 20 is even
     21 is odd
     22 is even
     23 is odd
     30 is even

ex
--
word = input("enter the word : ").lower()
vowels = "aeiou"
count = 0
for i in word:
    if i in vowels:
        count += 1
        print(f"{i} is vowel")
    else:
        print(f"{i} is consonant")
  
print(count)
o/p : enter the word : mukesh
      m is consonant
      u is vowel
      k is consonant
      e is vowel
      s is consonant
      h is consonant
      2 


ex
--
nums = [1,2,2,3,4,5,6,6]
empty = []

for i in nums:
    if i not in empty:
        empty.append(i)
print(empty)
o/p : [1, 2, 3, 4, 5, 6]


ex
--
digits = (1,2,3,1,5,3)        #digits 1,2,3,1,5,3   ----> 1,3
duplicate = []                #we use only list function in the another variABLE

for i in digits:         
   if digits.count(i) > 1 and i not in duplicate: # 1,1 --> 1 3,3 -->3
        duplicate.append(i)   # 1,3
print(duplicate)              #[1,3]

o/p : [1,3]

----------------------------------------------------------------------------------------------------------------------------31/08
perfect number
--------------

num =28
sum_ =0

for i in range(1,num):
    if num % i == 0:
        sum_ += i
if sum_ == num:
    print(f"{num} perfect number")
else:
    print(f"{num} not perfect number")

o/p: 28 perfect number

fibonacci
---------
num_ = 0
num_2 = 1
print(num_,num_2,end = " ")

for i in range(0,11):
  num_3 = num_ + num_2
  num_ = num_2
  num_2 = num_3
  print(num_3,end = " ")

o/p : 0 1 1 2 3 5 8 13 21 34 55 89 144

-----------------------------------------------------------------------------------------------------------------------------01/09
FUNCTION
--------
--> A function is a block of code that can be excuted only when is called..
--> A function start with def keyword and  the line called ass defination line ,where we can define a function name
--> And if we want to excute the program in the function,need to call with the function name define at def line

eg
--
def add(a,b)
    print(a+b)
add(5,6)
 
ARGUMENTS
---------
postional arguments
-------------------
--> the arguments should be same at def 
def feb(num_1,num_2):
    print(num_1,num_2,end = " ")

    for i in range(0,11):
          num_3 = num_1 + num_2
          num_1 = num_2
          num_2 = num_3
          print(num_3,end = " ")
feb(0,1)
0/p:

default arguments
-----------------
-->the default arguments where the function will only consider the data
   at calling,even though data present at def line

def num_(num,num_1):
    print(num + num_1)
num_(87,78)


keyword argument
----------------
-->

eg
--
def data_(name,age,location):
    print(age)
    print(name)
    print(location)
data_(location = "srikakulam" ,name = "mukesh" ,age =22)

eg
--
def greet(name, message="Hello"):
    print(f"{message}, {name}!")

# Using positional arguments
greet("Mukesh", "Good morning")

# Using keyword arguments
greet(name="Mukesh", message="Good morning")
greet(message="Hi", name="Mukesh")  # order doesn’t matter
o/p:
Good morning, Mukesh!
Good morning, Mukesh!
Hi, Mukesh!


variable length argument
------------------------
--> adding a ( * call it as args) before a variable at parameter
    we can pass tuple of arguments and can be access with indexing

def all_(*tv):
    print(tv)
all_("sony","nani","munna")

o/p:('sony', 'nani', 'munna')

keyword length arguments
------------------------
-->

def details(**data_):
    print(data_.keys())
details(name = "munna" ,age = 22 ,location = "srikakulam")

o/p : dict_keys(['name', 'age', 'location'])

RETURN
------
--> return keyword used inside the function ,once the return is excuted
    means it will get back to calling with return values


def all_(a,b):
    return a - b
print(all_(10,50))

o/p: -40
-----------------------------------------------------------------------------2/09
scope varibles
--------------
1.local variable
----------------
-->declareed inside the function

def greet():
    msg = "Hello from inside the function!"
    print(msg)
greet()
o/p: Hello from inside the function!


2.global variable
-----------------
-->declared outside all functions 
msg = "Python is awesome!"

def display():
    print("Inside function:", msg)

display()
print("Outside function:", msg)

O/P:Inside function: Python is awesome!
    Outside function: Python is awesome!

recursive function
------------------
-->A recursive function is a function that calls itself directly or indirectly to solve a problem.
   It breaks a big problem into smaller subproblems of the same type until it reaches a base case
   (a condition where recursion stops).

def factorial(n):
    if n == 0 or n == 1:   # Base case
        return 1
    else:
        return n * factorial(n - 1)  # Recursive case  # 5 * 4 * 3 * 2 * 1

print(factorial(5))  # Output: 120 

o/p : 120

---------------------------------------------------------------------------------------------------3/09
lambda funcction
----------------
-->lambda function is small anonymous function
-->lambda can take n numbers arguments ,but only with one expression
-->the function is defined 
ex
--
add_ = lambda a,b,c : a+b+c
print(add_(10,20,30))
o/p:60
ex
--
greater = lambda a,b:a if a > b else b
print(greater(100,200))
o/p:200

filter()
--------
-->filter() function will perform only on selected


nums = [1,2,3,4,5]
data_ = filter(lambda a : a % 2 == 0,nums)
print(tuple(data_))
o/p : 2,4


map()
-----
-->map() function will perform on all elements of a iterable
syntax --> map(lambda arguments : expression, iterable)

num_ = [1,2,3,4,5]
res_ = map(lambda a: a % 2 == 0,num_)
print(list(res_))
o/p : [False, True, False, True, False]

num_ = [1,2,3,4,5]
res_ = map(lambda a: a + 5,num_)
print(list(res_))
o/p : [6, 7, 8, 9, 10]


reduce()
--------
from functools import reduce
nums = [1,2,3,4,5]
data_ = reduce(lambda a,b: a % b,nums)
print(data_)
o/p:55

------------------------------------------------------------4/09
list comprehension
------------------
--> list comprehension is the shortest form of syntax to create a new list 

old_ =(1,2,3,45)
new_ = [ i for i in old_]
print(new_)
o/p :  [1, 2, 3, 45]

old_ =[21,22,33,44,66,88]
new_ = [ i for i in old_ if i % 2 == 0]
print(new_)
o/p:[22, 44, 66, 88]

NESTED COMPREHANSION
--------------------
--> using list comprehension generating list inside list

data_ = [[10,20,30],
        [40,50,60],
        [70,80,90]]

fan = [num for i in data_  for num in i]
print(fan)

o/p : [10, 20, 30, 40, 50, 60, 70, 80, 90]

GENERATOR
---------
--> a generator is a special function which generates one
   value at a time
   

-----------------------------------------------------------------











































