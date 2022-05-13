import numbers
from pickle import TRUE


print("Hello World")
a= 5
b=10
my_name="Juliet Nakibuuka"
the_sex='Am a female by nature'

print(a,b,my_name,the_sex)
print(123, "it works")

     # EXERCISE 1
var1= 'start'
var2='start'
num1= 4
num2= 4
total=num1*num2
print('The total is', total)

    # USING METHODS
def method_one(my_argument):
    print(my_argument)
method_one("ookkay")

def method_2(number_1, number_2):
    total= number_1 + number_2
    print(total)
method_2(4,6)

# EXERCISE 2
def return_42():
    return 42

def my_method(num_1,num_2):
    print( num_1*num_2)
my_method(100,100)

# EXERCISE 3
my_list=[1, 2, 97]
my_tuple=(10, )

set1={14, 5, 9, 31, 12, 77, 67, 8}
set2={5}
set2.add(77, )
print(set2)
jj=set1.intersection(set2)
print("The intersection is" ,jj)
hh=set1.union(set2)
# print("The union is" ,hh)

# LOOPS
variable_name='Juliet'
for letter in variable_name:
    print(letter)

# set_of_numbers=True 
# while set_of_numbers==True:
    # print('That is right')

people_known= ['Jack', 'Peter', 'John']
person=input('Enter the name of the person:')

if person in people_known:
    print('You may know', person)
else : 
    print('You do not know', person)

while people_known[0]=='Jack':
    people_known.append('Juliet')
    print(people_known)
    break
else : print ('it is over')

# EXERCISE
Numbers=[1,2,3,4,5,6,7,8,9]
def return_evens():
 for number in Numbers:
        if number %2==0:
            evens=[]
            evens.append(number)
        return evens

def user_choice(choice):
    if choice== 'a':
        return 'Add'
    elif choice == 'q':
        return 'quit'

