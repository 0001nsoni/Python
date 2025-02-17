'''
For Loop
Execute a block of code for each item in the sequence
(such as a list ,tuple , string or range)
'''
# for i in 1,2,3,7,5:
#     print(i)

user_list=['Alex','Raju','Sham','Baburao']
for user in user_list:
    print(user)

marks={'Hindi':80,'English':90,'Science':100}

for key,vlaue in marks.items():
    print(f'Subject is: {key}')
    print(f'Marks is: {vlaue}')

for key in marks.keys():
    print(f'subject name is : {key}')
for num in range(1,20):
    print(num)