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

print(array)