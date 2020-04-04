n = int(input())
a = list(map(int, input().split()))

def next_permutation(a):
    #배열은 0부터시작하므로 길이 맞춤 
    n=len(a)-1
    i = n
    while i>0 and a[i-1]>=a[i]:
        i-=1
       
    #만약 i가 0이라면 리스트는 내림차순이란뜻이므로 False리턴
    if i==0:
        return False
        
    #인덱스를 교환함 
    j = n
    while a[i-1]>=a[j]:
        j-=1
    a[i-1],a[j]=a[j],a[i-1]
    
    #i이후 값들의 정렬(=끝에서부터 앞의 수와 차례로 swap)
    j=n
    while i<j:
        a[i],a[j]=a[j],a[i]
        i+=1
        j-=1
    return True

if next_permutation(a) is True:
    for i in a:
        print(i, end=' ')
    print()
else:
    print(-1)