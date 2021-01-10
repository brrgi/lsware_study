import heapq
a,b,n=map(int,input().split())      #상민이 a 시간, 지수 b시간, n은 손님 수

number=1
heap=[]
for i in range(n):
    temp=input().split()

    time=int(temp[0])   #주문 시간
    color=temp[1]       #포장지 색깔
    nums=int(temp[2])   #주문한 선물 개수

    if color=='B':  #상민이
        for i in range(nums):
            heapq.heappush(heap, time+(i*a))
    else:           #지수
        for i in range(nums):
            heapq.heappush(heap, time+(i*b)+0.1)
    #RED인 경우 우선순위 값으로 0.1추가

sangmin=[]
jisoo=[]
while heap:
    temp=heapq.heappop(heap)
    if int(temp)==temp:
        sangmin.append(number)
    else:
        jisoo.append(number)
    number+=1

print(len(sangmin))
for i in sangmin:
    print(i, end=' ')
print()
print(len(jisoo))
for i in jisoo:
    print(i, end=' ')