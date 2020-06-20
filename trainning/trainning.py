def query1(x, y, lastAnswer):
    seq = (x ^ lastAnswer) % n
    seqlist[seq].append(y)


def query2(x, y, lastAnswer):
    seq = (x ^ lastAnswer) % n
    lastAnswer = seqlist[seq][y % len(seqlist[seq])]
    print(lastAnswer)
    return lastAnswer


line1 = input().split()
n = int(line1[0])
q = int(line1[1])
seqlist = []
lastAnswer = 0
for _ in range(n):
    seqlist.append([])

for _ in range(q):
    query = input().split()
    if (int(query[0]) == 1):
        query1(int(query[1]), int(query[2]), lastAnswer)
    else:
        lastAnswer = query2(int(query[1]), int(query[2]), lastAnswer)
