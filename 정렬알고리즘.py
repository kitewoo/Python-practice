# 선택 정렬 

array = [7,5,9,0,3,1,6,2,4,8]
for i in range(len(array)):
    min_index = i  #0부터 대입하니까 처리되지 않은 것 중 가장 작은 값은 i가 된다. 
    for j in range(i+1, len(array)): #i가 0이면 처리되지 않은 값들은 1부터 끝 수인 9가 된다. 
        if array[min_index] > array[j]: #계속 한칸 씩 비교
            min_index = j #가장 작은 값을 갖는 j를 내려보냄
    array[i], array[min_index] = array[min_index], array[i]

print(array)

    #for 구문 2번을 돌린다면 N + N-1 + N-2 + .... + 2 가 된다. 이를 수식으로 풀면 시간복잡도는 O(N**2) 이 된다.
# 삽입 정렬

array = [7,5,9,0,3,1,6,2,4,8]
for i in range(len(array)):
    for j in range(i,0,-1): #인덱스 i 부터 1까지 1씩 감소하며 반복하는 문법
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break
#삽입 정렬은 이중for문이라 위와 동일하게 최대 O(N**2)이다. 만약 정렬이 잘 되어있다면 N번만 하면 되므로 최선의 경우 O(N)이다. 

print(array)

# 퀵 정렬 : 기준 데이터 값을 기준으로 큰 값과 작은 값의 위치를 바꾸는 방법. 정렬 라이브러리의 근간이 되는 알고리즘
# 시간 복잡도는 최선의 경우 O(N*log(n)), 최악의 경우 N**2
array = [5,7,9,0,3,1,6,2,4,8]
def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right=end
    while(left <= right): 
        #pivot 보다 큰 데이터를 찾을 때 까지 반복
        while(left <= end and array[left] <= array[pivot]):
            left += 1
        #pivot 보다 작은 데이터를 찾을 때 까지 반복
        while (right > start and array[right] >= array[pivot]):
            right -= 1 
        
        if(left>right): #왼쪽에서 오는 애랑 오른쪽에서 오는 애랑 엇갈렸다면
            #작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]

        else:
            array[left], array[right] = array[right], array[left]
        
    #분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행(재귀)

    quick_sort(array, start, right-1)
    quick_sort(array,right+1, end)
quick_sort(array,0,len(array)-1)
print(array)


#파이썬 장점을 살린 방식
array= [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array):
    #리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <=1:
        return array
    
    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x<=pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] #분할된 오른쪽 부분

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))

# 계수 정렬 : 특정한 조건이 부합할 때만 사용할 수 있지만 매우 빠르게 동작하는 알고리즘
# 조건 : 데이터의 크기 범위가 제한되어 '정수' 형태로 표현할 수 있을 때 사용 가능하다.
# 데이터의 개수가 N, 데이터(양수) 중 최댓값이 K일 때 최악의 경우에도  수행시간 O(N+K)를 보장.

array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

count = [0] * (max(array)+1)

for i in range(len(array)): # 각 데이터에 해당하는 인덱스의 값 증가
    count[array[i]] += 1

for i in range(len(count)): # 각 리스트에 기록된 정렬 정보 확인
    for j in range(count[i]):
        print(i, end=' ') # 띄어쓰기를 구분으로 등장한 횟수만큼 인덱스 출력

#DFS 깊이 우선 탐색

def dfs(graph, v, visited):
    #현재 노드 방문 처리
    visited[v] = True
    print(v, end=' ')
    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i ,visited)

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [7],
    [2,6,8],
    [1,7]]

visited = [False]*9
dfs(graph, 1, visited)

