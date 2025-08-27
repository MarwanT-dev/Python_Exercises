#compressing problem 

text  = 'aaaaaddcefff'
cnt = 1

for i in range(1,len(text)):
    if text[i] != text[i-1]:
        print(text[i-1],cnt,sep = '',end = "")
        print("_",end = "")
        cnt = 1
    else:
        cnt+=1

print(text[-1],cnt,sep = "",end="")