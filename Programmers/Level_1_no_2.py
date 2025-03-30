def count_ones(n, l, r):
    if n == 0:
        return 1  # n=0일 때 "1" 하나만 존재
    
    length = 5 ** (n - 1)  # n-1 단계의 비트열 길이
    total_ones = 4 ** (n - 1)  # n-1 단계에서 '1'의 개수
    
    count = 0
    for section in range(5):
        start = section * length + 1
        end = start + length - 1
        
        if r < start or l > end:  # 범위를 벗어나면 무시
            continue
        if section == 2:  # 3번째 블록(항상 00000)이면 건너뛰기
            continue
        if l <= start and end <= r:  # 블록 전체가 포함되면 빠르게 계산
            count += total_ones
        else:  # 부분적으로 포함되면 재귀 탐색
            count += count_ones(n - 1, max(l, start) - start + 1, min(r, end) - start + 1)

    return count

def solution(n, l, r):
    return count_ones(n, l, r)



# main start!

print(solution(2, 4, 17))  # 8

# main end!

