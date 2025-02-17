'''
the program should add number from 1 to a specified number in a list 
for multiples of 3 , it should be 'Fizz'
for multiples of 5 , it should be 'Buzz'
for numbers multiples of both 3 and 5, it should be "FizzBuzz"
Print the list
'''
till_number = int(input('Enter the specified number : '))
my_list=[]
for num in range(1,till_number+1):
    result = ""
    if num%3==0:
        result=result+'Fizz'
    elif num%5==0:
        result=result+'Buzz'
    else:
        result=num
    my_list.append(result)
print(my_list)
