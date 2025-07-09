#is prefix
str = input()
prefix = input()

""" easiest solution
if prefix in str:
    print("YES")
else:
    print("NO")
"""

for i in range (len(prefix)):
    if str[i] != prefix[i]:
        print("NO")
        break
else:
    print("YES")