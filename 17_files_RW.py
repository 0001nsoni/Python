with open("user.txt",'w') as file:
    file.write('This is my first text file using python')
with open("user.txt",'a') as file:
    file.write('\nappending a line in text file')
with open("user.txt",'r') as file:
    content=file.read()
print(content)