#same as list , however you can't modify the items of Tuple
#Immutable,Ordered


days=('mon','tue','wes')
print(type(days))
print(days)
print(days[1])
# days[1]='fri' can't change it because of immutability
print(days.count('mon'))
# days=(1,2,3) we can do this ,this is allowed in python
print(days.index('tue'))