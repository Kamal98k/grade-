sub1=int(input("Enter the first subject marks:\n"))
sub2=int(input("Enter the second subject marks:\n"))
sub3=int(input("Enter the third subject marks:\n"))
sub4=int(input("Enter the fourth subject marks:\n"))
sub5=int(input("Enter the fifth subject marks:\n"))

avg=(sub1+sub1+sub1+sub1+sub1)/5

print(avg)

if(avg>=90):
    print("your Grade is : A+")

elif(avg <=89 and avg >=80 ):
    print("your grade: A")

elif(avg <=79 and avg >=60 ):
    print("your grade: B")

elif(avg <=59 and avg >=45 ):
    print("your grade: C")

elif(avg <=44 and avg >=33 ):
    print("your grade: D")

else:
    print("you are fail:")



