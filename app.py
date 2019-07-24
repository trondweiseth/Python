import time
name = input('Name: ')
age = input('Age: ')
year = (time.strftime('%Y'))
birth = (int(year) - int(age))
print()
print('=======================================================')
print("The Pation's name is: ' + name + ' and is ' + age + ' years old.")
print('Year of birth:')
print(int(birth))
print('=======================================================')

Test