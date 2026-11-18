#function return multiple value
def square_cube(n):
    square=n*n
    cube=square*n
    return square,cube
s,c=square_cube(5)
print("square of 5 =",s)
print("cube of 5=",c)

#another example
def square_cube(n):
    square=n*n
    cube=square*n
    return square,cube
ans=square_cube(4)
s=ans[0]  
c=ans[1]
print("Square of 4=",s,"and cube of 4=",c)