def solution(num_list):
    rs = []
    for i in range(len(num_list) - 1, -1, -1):
        rs.append(num_list[i])
    return rs;