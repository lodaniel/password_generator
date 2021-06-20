# Python code to create secure password

import random
n="0123456789"
l="abcdefghijklmnopqrstuvxwyz"
u="ABCDEFGHIJKLMNOPQRSTUVXWYZ"
s="!@#$%&*(){}[]<>.,;^~-_"

x=n+l+u+s
lenght=18
pwd="".join(random.sample(x,lenght))

print("My new password is: ",pwd)