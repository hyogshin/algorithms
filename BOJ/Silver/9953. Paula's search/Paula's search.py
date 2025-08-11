while True:
    n = int(input())
    if n == 0:
        break

    left = 1
    right = 100
    cnt = 1
    if n % 2 != 0:
        left, right, mid = 1, 99, 49

        cnt += 1
    else:
        left, right, mid = 2, 100, 50

    while left <= right:
        if (n % 2 == 0 and mid % 2 !=0) or (n % 2 != 0 and mid % 2 == 0):
            mid -= 1

        if n == mid:
            break
        cnt += 1
        if n > mid:
            left = mid + 2
        else:
            right = mid - 2

        mid = (left + right) // 2

    print(cnt)