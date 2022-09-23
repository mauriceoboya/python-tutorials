# varible are used to temp hold values
from msilib.schema import Binary


FirstName='Maurice Oboya'
print(FirstName)

##varible assignment CamelCase,Pascal,Snakecase
firstName='oboya maurice'
FirstName='Oboya maurice'
first_name='oboya maurice'
print(firstName,FirstName,first_name)
### global variables and local variables
# ###local vriables are declared and used inside a function while global variables are declared
##outside a function and can be used inside a function
## x is a global variable and a,b  are local variables

x=34

def sum():
    global x
    a=2
    b=3
    c=a+x
    print(f'the sum of {a} and {x} is {c}')

sum()

## deleting a varible
del x
#print(x)


##### Data types ###############
a=10 + 3j
b="Hi Python"  
c = 10.5  
print(type(a))  
print(type(b))  
print(type(c)) 
##list ,#tuples(immutable)
list1=['mike','kim','jane',1,2,3,4,5,4+5j,'john']
list1.insert(0,'maurice')
list1.append('oboya')
print(list1)
print(list1[1:6])

### dictionaries-key value pair
name={1:'mike',2:'john',3:'james',3:'lenny'}
  ##getting the dictionary key value
print(name[3])


### python Literals(data given to a variable or constant)
## string literals
text1='hello \n user' 
print(text1)
