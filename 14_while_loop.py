print("Enter a no. to check if that is Even or not")
num = ""
while num!='q':
    num = input("Enter your no else q - ")
    if num.isdigit():
        if int(num )% 2==0:
            print('yes no. is even')
        else:
            print('No. is Odd')