def solution(array):
    answer = 0
    dp = [0] * 1000
    for i in range(len(array)):
        dp[array[i]] += 1
    answer = dp.index(max(dp))
    tmp = max(dp)
    dp[answer] = 0
    
    if max(dp) == tmp:
        answer = -1
    
    return answer