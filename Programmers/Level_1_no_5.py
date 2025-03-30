import heapq

def solution(jobs):
    # 작업을 요청 시각을 기준으로 정렬
    jobs.sort(key=lambda x: x[0])
    
    current_time = 0  # 현재 시간
    idx = 0           # 작업 인덱스
    total_time = 0     # 총 소요 시간의 합
    job_count = len(jobs)
    
    # 우선순위 큐
    pq = []
    
    while idx < job_count or pq:
        # 대기 중인 작업 중 시작 시각이 현재 시간보다 작거나 같은 작업을 큐에 삽입
        while idx < job_count and jobs[idx][0] <= current_time:
            heapq.heappush(pq, (jobs[idx][1], jobs[idx][0]))  # (소요시간, 요청시각)
            idx += 1
        
        if pq:
            # 우선순위 큐에서 가장 소요 시간이 적은 작업을 꺼낸다
            duration, start = heapq.heappop(pq)
            current_time += duration  # 작업을 처리하는데 걸린 시간만큼 시간을 증가시킨다
            total_time += current_time - start  # 요청 시각부터 끝난 시각까지의 시간
        else:
            # 큐에 대기 중인 작업이 없으면, 작업 요청이 들어올 때까지 기다린다
            current_time = jobs[idx][0]
    
    # 평균 반환 시간의 정수 부분을 반환
    return total_time // job_count




# main start!
print(solution([[0, 3], [1, 9], [3, 5]]))  # 8
# main end!

