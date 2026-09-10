'''
# 01 
# Use a loop to accept three marks from the user. 
marks=[]
for mark in range(3):
    mark=int(input("enter the marks : "))
#Add each entered mark to a list using append()
    marks.append(mark)
#Insert 90 at the beginning using insert()
marks.insert(0,90)
#Add 75 and 85 together using extend().
marks.extend([75,85])
#Use a condition to check for 75, then remove it using remove(). 
if 75 in marks:
    marks.remove(75)
#Remove the final mark using pop() and display the removed value. 
print(marks.pop())
print("final list is " ,marks)
#Display the final list and its length using len(). 
print("length of the list is ",len(marks))


#02
numbers = [20, 10, 30, 20, 40, 20] 
#Sort the list in ascending order using sort(). 
numbers.sort()
#print(numbers)
#Reverse the sorted list to produce descending order using reverse(). 
numbers.reverse()
print(numbers)
#Ask the user to enter a number to search for. 
number = int(input("enter the number : "))
#Use a condition to check whether the number exists in the list. 
if number in numbers:
#If found, display its count and first index using count() and index(). 
    print("count is",numbers.count(number))
    print("first index is",numbers.index(number))
else:
    print("number is not found")
#Display the smallest value, largest value, and total using min(), max(), and sum().
print("smallest number",min(numbers))
print("largest number",max(numbers))
print("total sum",sum(numbers))

#03
numbers = [10, 15, 20, 25, 30, 35] 
#Create two empty lists named even and odd. 
even_ = []
odd_ = []
#Use a loop to examine every number in the original list. 
for num  in numbers:
#Use a condition with the remainder operator (%) to identify even and odd numbers
    if num % 2 == 0:
#Add each number to the correct list using append(). 
        even_.append(num)
    else:
        odd_.append(num)
#Use slicing to display the first three and last three values. 
print("first three",numbers[:3])
print("last three",numbers[-3:])
#Create a backup of the original list using copy(). 
f = numbers.copy()
#Empty the original list using clear(), then display both the original and backup lists. 
numbers.clear()
print("original list",numbers)
print("backup list",f)
'''
   
