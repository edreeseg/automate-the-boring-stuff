spam = 0
while spam < 5:
    print('Hello World')
    spam = spam + 1

#

name = ''
while name != 'your name':
    print('Please type your name.')
    name = input()
print('Thank you!')

#

# Infinite loop
while True:
    print('Hello!')

#

while True:
    print('Please type your name.')
    name = input()
    if name == 'your name':
        break
print('Thank you!')

#

spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:
        continue
    print('spam is ' + str(spam))

#

print('My name is')
for i in range(5):
    print('Jimmy Five Times ' + str(i))

#

total = 0
for num in range(101):
    total = total + num
print(total)

#

print('My name is')
i = 0
while i < 5:
    print('Jimmy Fives Times ' + str(i))
    i = i + 1

#

print('My name is')
for i in range(12, 16):
    print('Jimmy Five Times ' + str(i))

#

print('My name is')
for i in range(0, 10, 2): # step by 2 each iteration
    print('Jimmy Five Times ' + str(i))

#

print('My name is')
for i in range(5, -1, -1): # step down by 1 each iteration
    print('Jimmy Five Times ' + str(i))