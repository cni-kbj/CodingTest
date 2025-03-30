def solution(n, a, b):
    round_num = 0
    
    while a != b:
        a = (a + 1) // 2
        b = (b + 1) // 2
        round_num += 1
    
    return round_num


# main start!

N = 8		#TC no.1
A = 4		#TC no.1
B = 7		#TC no.1
print(solution(N, A, B)) 

# main end!