a=input()
b=a

a=a.replace("<?", 'a')
a=a.replace(">?", 'b')

stack=[]

temp=''
for i in range(len(a)):
    if a[i]=='(':
        stack.append(i)
    elif a[i]==')':
        stack.append(int(temp))

    elif '+' or '-' or 'a' or 'b':
        stack.append(a[i])
    else:
        temp+=a[i]