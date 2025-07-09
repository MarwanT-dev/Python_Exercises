str = input("enter the string :")
subsequence = input("enter the subsequence :")

pointer = 0
for i in range(len(str)):
    if(str[i]==subsequence[pointer]):
        pointer+=1
    
    if pointer==len(subsequence):
        print("YES")
        break
else:
    print("NO")
