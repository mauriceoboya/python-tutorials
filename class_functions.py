class Person:
    def __init__(self,first_name,second_name):
        self.first_name=first_name
        self.second_name=second_name

first_name=input('Enter first name:')
second_name=input('Enter second name:')
person=Person(first_name,second_name)

print (f"hello {person.first_name} {person.second_name}, welcome to the site.")

