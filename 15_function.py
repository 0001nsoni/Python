'''
block of code which perform some task and run when it is called

can be reuse many times in our program which lessen our lines of code

we can pass arguments to the method
'''
def myfun():
    print("my name is neeraj")
myfun()
myfun()
def greeting(username,*hobbie):
    print("*"*20)
    print(f"hello {username} ")
    print(f"your hobbie is {hobbie}")
    print("*"*20)
greeting('Neeraj',"programming","watching movies","chilling")
greeting('Raju',"party","circket")
greeting("sham","football")


# dynamic argument functions

def user_details(name,**user_info):
    print(f"Name- {name}")
    for key,value in user_info.items():
        print(f"- {key}: {value}")


user_details('Raju',age=18)
user_details('Neeraj',age=20,skill='DEVOPS',tech='Mern')

def addition(num1,num2):
    return num1+num2
print(addition(10,20))
