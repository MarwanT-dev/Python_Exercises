#is substring problem 



str = input("enter the string :")
sub = input("enter the substring:")

for i in range(len(str)):
    match  = True
    if match:
        for j in range(len(sub)):
            if(str[i+j]!=sub[j]):
                match = False
                break
    if match :
        print("Yes")
        break
else:
    print("No")

