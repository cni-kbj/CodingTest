def solution(s):
    # 열린 괄호의 개수를 세는 변수
    count = 0
    
    # 문자열 s를 순차적으로 확인
    for char in s:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
        
        # 만약 닫힌 괄호가 너무 많다면 (즉, count가 음수라면)
        if count < 0:
            return False
    
    # 모든 괄호가 짝지어졌다면 count는 0이어야 한다.
    return count == 0




# main start!

print(solution("()()"))      # True
print(solution("(())()"))    # True
print(solution(")()("))      # False
print(solution("(()("))      # False
print(solution(""))          # True (빈 문자열은 올바른 괄호로 간주)

# main end!

