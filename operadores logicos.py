a=4
b=5
c=2
d=1
e=6
f=3
if a<b and b>c and b>d and b>e and b>f:
     print("el verdadero es b el mayor")
elif c>a and b>c and d<c and c>e and c>f:
     print("el verdadero es c el mayor")
elif d>a and d>b and d>c and d>c and b>f:
     print("el verdadero es d el mayor")
elif e<b and b>c and b>d and b>e and b>f:
     print("el verdadero es e el mayor")
else:
    print("el verdadero es f el mayor")