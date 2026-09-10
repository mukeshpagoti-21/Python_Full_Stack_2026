'''
EXCEPTION HANDLING
------------------
In Python, exception handling lets you deal with runtime errors gracefully using try, except, else, and finally blocks, so your program doesn’t crash unexpectedly.
It separates risky code from error-handling logic, making applications more reliable and easier to debug.

#things we use in only exception handling
-----------------------------------------
try → Code that may raise an error.

except → Handles specific errors. Multiple except blocks can catch different exceptions.

else → Runs only if no exception occurs.

finally → Always runs (cleanup tasks like closing files).


NameError -->print(x)   # x is not defined
NameError: name 'x' is not defined

ValueError -->num = int("abc")   # "abc" is a string, but not a valid integer
ValueError: invalid literal for int() with base 10: 'abc'


try:
    x = 10/0
except ZeroDivisionError:
    print("zero division error")
except ValueError:
    print("Value error")
except NameError:
    print("Name Error")
else:
    print("divisible by that number")
finally:
    print("program excuted succesfully")


FILE HANDLING
-------------
Modes in Detail:-
---------------
"r"	Read --> Error if file doesn’t exist
"w"	Write --> Creates new file or overwrites existing
"a"	Append -->Adds content at the end
"x"	Create -->Error if file already exists
"rb" / "wb"	Binary read/write -->Used for images, videos, etc.


1. Read Mode ("r")
------------------
Opens a file for reading.

with open("example.txt", "r") as f:
    data = f.read()
    print(data)
👉 Error if the file doesn’t exist.

2. Write Mode ("w")
------------------
Opens a file for writing. Creates a new file or overwrites existing content.

with open("example.txt", "w") as f:
    f.write("This will overwrite the file.")
👉 Old content is erased.

3. Append Mode ("a")
--------------------
Opens a file for appending. Adds new content at the end.

with open("example.txt", "a") as f:
    f.write("\nThis line is added at the end.")
👉 Old content remains, new content is added.

4. Create Mode ("x")
-------------------
Creates a new file. Error if the file already exists.

python
with open("newfile.txt", "x") as f:
    f.write("This file is newly created.")
    

'''









































