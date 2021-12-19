#import the necessary modules!
import random
import string

print('hello, welcome to password generator')
name = str(input("enter your name ?"))
#input the length of password
length=int(input('\nEnter the length of password:'))
# predefine data
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation
#combine the data
all = name+lower+upper+num+symbols

#use random
temp = random.sample(all,length)

#create the password
password = "".join(temp)

#print the password
print(password)