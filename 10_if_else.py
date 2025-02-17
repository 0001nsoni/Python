'''
    if age>=18:
        print("you can vote!')
    else: 
        print("you can't vote!")
'''


if True:
    print("Hey it is true")
    print("this is second line in if else")
else:
    print('it is false')



print('Enter a no. to check if that is EVEN or not')
num=int(input('Enter a no - '))
if num%2==0:
    print('Yes no. is EVEN')
else:
    print('No. is ODD')

users=['neeraj','soni','paul']
if 'neeraj' in users:
    print('User exist')


marks=int(input('Enter your marks - '))
if marks>=80:
    print('1st Divison')
elif marks>= 60:
    print('2nd Divison')
else:
    print("Failed!")

# Nested if 
age=20
voter_id=True
if age>=18:
    if voter_id:
        print("yes you can vote")
    else:
        print("Please apply for Voter ID first")
else:
    print('You cannot vote!')  
