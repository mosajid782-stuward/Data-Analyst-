#REquired Argument
def display(id,name):
    print("{} :{} ".format(id,name))
print(18,"SAJID")

#Keyword Argument
def display(id,name):
    id+=10
    print("{} : {}".format(id,name))
display(name="SAJID",id=10)

#Default argument
def display(name,age=20):
    print("{} : {}".format(name,age))
print("MO SAJID")