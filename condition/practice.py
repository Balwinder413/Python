   #largest no
a = int(input("enter first largest no")) 
b = int(input("enter second largest no"))
c = int(input("enter third largest no"))

if(a > b and b > c):
    print("first no largest")
elif(b > c ):
    print("second is largest")  
else:
    print("c is largest")
