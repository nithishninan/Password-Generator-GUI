import random
lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
number = '0123456789'
symbol = '!@#$%^&*()_+<>/'
length = int(input('Required String length: '))
string = lower + upper + number + symbol
password = "".join(random.sample(string,length))
print("Suggested Password:--> "+password)