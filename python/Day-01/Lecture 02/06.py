#variable length of Argument
#example of arg
def add(*num):
    sum=0
    for n in num:
        sum+=n;
    return sum
print(add())   # 0 argument
print(add(1))  #1 argument
print(add(1,2))  #2 argument
print(add(1,2,3))   #3 argument
print(add(1,2,3,4))  #4 argument

#example of kwarg
def display_emp(**data):
    for k,v in data.items():
        print("{} \t :".format(k,v))
display_emp(id=1001,name="hillary",age=20)
