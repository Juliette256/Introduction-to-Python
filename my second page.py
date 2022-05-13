import numbers
from pickle import TRUE
from re import M

from pkg_resources import invalid_marker
 
# EXERCISE
def who_do_know():
  people=input('Name people you know: ')
  people_list=people.strip().lower()
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

# LISTS
array_of_nu=[0,1,2,3,4]
producted =[x+10 for x in range(5)]
print(producted)

# DICTIONARIES
student ={
  'name':'Jose',
  'school':'computing',
  'sgrades':(66,77,88)
}

def average_grade(data):
  grades=data['sgrades']
  return sum(grades) / len(grades)

def average_grade(studentlist):
  Total=0
  Count=0
  
  for student in studentlist:
    Total += sum(student['sgrades'])
    Count +=len(student['sgrades'])
    return Total / Count
    

class Store:
  def __init__(self, name):
    self.name=name
    self.items=[]
  
  def add_item(self, itemname, itemprice):
    self.iname=itemname
    self.iprice=itemprice
    items={
       'name':itemname,
       'price':itemprice
          }
    self.items.append(items)
  
  def stock_price(self):
     total=sum([items['price'] for items in self.items])
     return total