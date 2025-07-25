cnt = int(input())
# lns = [[0] * 3] * cnt
lns = []

for i in range(cnt):
    lns += input().split()

# print(lns)
# for 
# for i in range(12):
#     for j in range(6):

# for i in range(int(lns[3*i+2])):
#     print(i)


for i in range(cnt):
    w = str(int(lns[3*i-1])%int(lns[3*i]))
    h = str((int(lns[3*i-1])//int(lns[3*i]))+1)
    if int(h) < 10:
        print(int(w + '0' + h))
    else:
        print(w+h)



#  101
#  201
#  301
#  .
#  .
#  H01
#  .
#  .
#  102
#  .
#  /.
#  .
#  1W
#  .
#  .
#  H+W