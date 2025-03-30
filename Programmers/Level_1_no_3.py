def solution(n, s):
    # s가 n보다 작은 경우에는 집합을 만들 수 없으므로 -1을 반환
    if s < n:
        return [-1]
    
    # 각 원소의 기본 값 q와 나머지 r을 계산
    q = s // n  # 각 원소가 가질 값
    r = s % n   # 나머지

    # 결과 집합을 생성
    answer = [q] * (n - r) + [q + 1] * r

    return answer



# main start!

print(solution(2, 9))  # [4, 5]
print(solution(2, 1))  # [-1]
print(solution(2, 8))  # [4, 4]
print(solution(3, 10)) # [3, 3, 4]
print(solution(5, 15)) # [3, 3, 3, 3, 3]

# main end!

