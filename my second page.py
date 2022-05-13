import numbers
from pickle import TRUE
 
# EXERCISE
def who_do_know():
  people=input('Name people you know: ')
  people_list=people.strip()
  return (people_list)
    
def ask_user():
    your_name=input('What is your name ?')
    List= who_do_know()
    new_name=your_name.strip()
    if new_name in List:
     print('You know this person called', new_name)
    else:
     print('You are not registered')
ask_user()
