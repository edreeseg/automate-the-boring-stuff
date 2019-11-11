spam = 42 # global variable
def eggs():
    spam = 42 # local variable

print('Some code here.')
print('Some more code.')

# Accessing global variables within a function's scope:

eggs = 100

def change_eggs():
    global eggs
    eggs = 0

print(eggs) # 100
change_eggs()
print(eggs) # 0