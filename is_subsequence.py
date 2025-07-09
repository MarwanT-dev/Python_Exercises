while(True):
    str = input("enter the string :")
    subsequence = input("enter the sub :")

    for i in range(len(str)):
        if(str[i]==subsequence[0]):
            for j in range(len(subsequence)):
                if(subsequence[j]!=str[i]):
                    print("No")
                    break
                i +=1
            else:
                print("YES")
                break