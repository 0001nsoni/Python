#lists
#orderd sequence of different types of values
#we can use multipel data type in a list 
#mix_list=["Neeraj",19,19.11,True]
#how to define a list?
# user=['raju','sham','paul']
#how to get value from a list? 

"""
users[0]
users[1] 
users[-1]
"""
user_list=['Alex','Raju','Sham','baburao']
print(user_list)
print(user_list[0])
#adding item to list
user_list.append('Neeraj')
print(user_list)
#to delete an item form list
user_list.remove('Raju') #put exact value
print(user_list)
#to modify values from a list

user_list[1]='Soni' 
print(user_list)

#adding item to a given postition
user_list.insert(1,'Sham')
print(user_list)
#to remove on the basis of index
del user_list[3]
print(user_list)

#length of list
print(len(user_list))
#we can do sorting of lists by inbuild functions of py
user_list.sort()
print(user_list)
user_list.sort(reverse=True)
print(user_list)
user_list.reverse()
print(user_list)
#for termprory sorting we can use
#print(user_lists.sorted())
#to remove last value
#user_list.pop() we can use it also in print or store removed value in  variable


# Slicing of Lists 
#Getting first two items
print(user_list[:2])
#getting middel 3 items
print(user_list[1:4])
#getting last 2 items
print(user_list[-2:])


#some operations of numerical lists
marks=[89,90,100,45,33,56]
print(marks)
print(min(marks))
print(max(marks))
print(sum(marks))
