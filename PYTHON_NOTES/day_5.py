'''
#perform operation
a =10
b = 20
print(a + b)
'''
#Tokens --> keywords,variables,operators,punctuator [],(),{}.
#variable should not start with number,space,symbols and also no space
#between words

batch = ["pfs-06" , "da-06"]
#print(batch)
#print(type(batch)) #everything is an object (pop --> oop)

#len() --> return the number of itams in a collection
#print(len(batch))
#IDLE is colourcoding editor (violet --> built - in functions)

#add 3 more students name into it 
#list --> collection --> append(),extend(),insert()

batch.append("saket")#adding in last position with only one argument
#print(batch)

batch.extend(["mukesh","yaswanth"])#adding elements in last ,but adding more than one inn the end 
#print(batch)

batch.insert(0,"munna")#adding in a specific value index 
#print(batch)

batch.insert(-1,"chinna")
print(batch)

#print(len(batch))

#indexing --> [] --> index start at 0 and ends at len(obj)-1
#also in reverse manner it is -1 to len(obj)

#print(batch[0])
#print(batch[4])
#print(batch[20]) #it will show an index error due to out of range

#slicing --> group of values [start:end]
#start is include : last is excluded
#print(batch[4:6])

#last 3 elements --> we prefer negative index values
#print(batch[-2:])

#first three elements
#print(batch[:3])

#striding --> [start:stop:step]
#in step is n-1
#print(batch[1:7:3])# start with 1 and 
#print(batch[::2])#skip only 1 element
#print(batch[::3])#skip only 2 element


#try out
'''
print(batch[:7:4])
print(batch[7::4])
print(batch[1::5])
print(batch[1:7:-2])
print(batch[-1:-4:-1])
'''

print(batch[7::4])
















