#is suffix


str = input()
suffix = input()

""" easiest solutions

print(str.endswith(suffix))
print(suffix in str)

"""
for i in range(1,len(suffix)+1):
    if suffix[-i] != str[-i] :
        print("NO")
        break
else:
    print("YES")