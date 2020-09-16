#program for max of 3 no's
a=int(input("enter 1st num: "))
b=int(input("enter 2nd num: "))
c=int(input("enter 3rd num: "))

max=a if a>b and a>c else b if b>c else c
print("max value:",max)

