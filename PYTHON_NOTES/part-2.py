'''
MODULES
-------
--> A MODULE IS A PYTHON FILE(.PY) THAT WRITTEN USING
    FUNCTION , VARIABLE,OPERATORS,ETC.
    
1.BUILT-IN MODULES
------------------
--> THE MODULES ARE DEVELOPED BY PROGRAMMER AND THOSE COMES WITH INSTALLATION
EG
--
* MATH
-------
import math
print(math.pow(2,3))
o/p : 8.0

* OS
----
import os
print(os.getcwd())
o/p : 

* SYS
-----
import sys
print(sys.path)
print(sys.version)
print(sys.path)

* RANDOM
--------
import random
print(random.randint(1000,9999))
o/p : 8465

import random
print(random.randint(1000,9999))
print(random.randrange(1,100))
o/p:3242
    7863

colour = ["red","blue","black","yellow"]
print(random.choice(colour))
o/p:yellow

random.shuffle(colour)
print(colour)
o/p:

import random
attep_ = 3
num = random.randint(1,100)
print(num)


while attep_ > 0:
    game_ = int(input("enter the  number between 1 and 100 : "))
    if game_ == num:
        print("your guess is correct")
        break
    else:
        attep_ -=1
if attep_ == 3:
    print("u won 500")
elif attep_ == 2:
    print("u won 300")
elif attep_ == 1:
    print("u won 100")
else:
    print("better luck time")
o/p:
98
enter the  number between 1 and 100 : 98
your guess is correct
u won 500


* math
------
import math
print(math.pi)
print(math.ceil(2.3))
print(math.floor(4.6))
print(math.sqrt(25))
print(math.sin(2))
print(math.pow(3,2))
print(math.cos(5))

*platform
---------

import platform
print(platform.python_version())
print(platform.system())
print(platform.platform())
print(platform.processor())

o/p:
3.14.6
Windows
Windows-11-10.0.26200-SP0
ARMv8 (64-bit) Family 8 Model 1 Revision 201, Qualcomm Technologies Inc
* collections
-------------
import collections
data_= ["jackfruit","pineapple","banana","mango","apple"]
print(collections.Counter(data_))
o/p:Counter({'jackfruit': 1, 'pineapple': 1, 'banana': 1, 'mango': 1, 'apple': 1})

all_ = collections.Counter(data_)
print(all_.most_common())
o/p :[('jackfruit', 1), ('pineapple', 1), ('banana', 1), ('mango', 1), ('apple', 1)]

*datetime
---------

from datetime import datetime
today = datetime.today()
print(today.month)
print(today.day)
print(today.year)
print(today.hour)
print(today.minute)

o/p:
9
7
2026
14
39

from datetime import datetime
now = datetime.now()
print(now.strftime("%d-%m-%y"))
print(now.strftime("%H:%M:%S"))
print(now.strftime("%a"))
o/p:
07-09-26
14:47:40
Mon






2.USER-DEFINED MODULES
----------------------
-->user-defined modules are simply files that you create yourself to organize and reuse code.

from examples import add,sub
print(add(10,20))
print(sub(30,10))
o/p : 30
      20


import examples as exm
print(exm.add(100,20))
o/p : 120

'''

import itertools

n = itertools.chain([1,23,3],[4,5,6])
print(n)
































