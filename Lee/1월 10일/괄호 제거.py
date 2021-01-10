from itertools import combinations
a=input()
stack=[]
ssang=[]
all=[]
def translate(str, ss):
    for i in ss:
        str=str[0:i[0]]+" "+str[i[0]+1:i[1]]+" "+str[i[1]+1:]
    str=str.replace(" ", "")
    return str

for i in range(len(a)):
    if a[i]=='(':
        stack.append(i)
    elif a[i]==')':
        temp=stack.pop()
        ssang.append((temp,i))
print(ssang)
t=[]
for i in range(1, len(ssang)+1):
    c = combinations(ssang, i)

    for j in c:
        t.append(j)

for i in t:
    all.append(translate(a, i))
all=set(all)
all=list(all)
all.sort()
for i in all:
    print(i)