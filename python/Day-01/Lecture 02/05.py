#Default Argument
def display(fname,lname,degs='officer',age=20):
    print("{} {} is a/an {} and age is {} ".format(fname,lname,degs,age))
display("SAJID","MILAN")

# example
def display(fname,lname,degs='officer',age=18):
    print("{} {} is a/an {} and age is {} ".format(fname,lname,degs,age))
display("SAJID","MILAN",age=20)
