# Compress the string

s = input("Enter a string : ")
count=1
ch=s[0]
for i in range(1, len(s)):
    if ch!=s[i]:
        print('(',count, ',',ch, ')',end=' ')
        c=1
        ch=s[i]
    else:
        c+=1
if c:
    print('(',count, ',',ch, ')')
