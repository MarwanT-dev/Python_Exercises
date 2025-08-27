#grouping problem 

text  = '11122234555'
print(text[0],end = '')

for i in range(1,len(text)):
    if text[i] != text[i-1]:
        print(' ',end = '')
    print(text[i],end = '')