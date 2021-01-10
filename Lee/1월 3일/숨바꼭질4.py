from collections import deque
subin, goal=map(int, input().split())

queue=deque()
queue.append(subin)
trigger=1
visit=[-1 for i in range(100001)]
if subin==goal:
    trigger=0
time=-1
visit[subin]=-2

while trigger:
    time += 1
    leng=len(queue)
    for i in range(leng):
        data=queue.popleft()
        if data==goal:
            trigger=0
        else:
            if data-1>=0 and visit[data-1]==-1:
                queue.append(data-1)
                visit[data-1]=data
            if data+1<=100000 and visit[data+1]==-1:
                queue.append(data+1)
                visit[data+1]=data
            if data*2<=100000 and visit[data*2]==-1:
                queue.append(data*2)
                visit[data*2]=data

queue2=deque()
howMany=0
lists=[]
while 1:
    if visit[goal]==-2:
        lists.append(goal)
        break
    else:
        lists.append(goal)
        goal=visit[goal]
    howMany+=1
print(howMany)
for i in range(len(lists)-1,-1,-1):
    print(lists[i], end=' ')