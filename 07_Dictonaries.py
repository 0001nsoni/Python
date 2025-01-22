# a type of data structure that store value in a formet of key pair
marks={'Hindi':80,'English':90}
print(marks)
print(type(marks) )
print(marks['English'])
print(marks.get('English'))
#adding a value in dictonary
marks['Math']=100
print(marks.get('Math'))
#to delete a value from dictonary
del marks['Hindi']
print(len(marks))