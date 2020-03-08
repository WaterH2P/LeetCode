limit = 10 ** 6
prime = [i for i in range(limit+1)]
i = 2
while i * i <= limit:
    if prime[i] == i:
        for j in range(i * i, limit + 1, i):
            if prime[j] == j:
                prime[j] = i
    i += 1

for t in range(int(input())):
    n = int(input()) - 1
    count = 0
    limit = int(n ** 0.5)
    for i in range(2, limit + 1):
        p = prime[i]
        q = prime[i // prime[i]]
        if p * q == i and q != 1 and p != q:
            count += 1
        elif prime[i] == i:
            if i ** 8 <= n:
                count += 1
    print(count)
