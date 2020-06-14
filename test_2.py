n = int(input())
i = 0
k = 0
counter = 0
list_items = [[0 for q in range(n)] for q in range(n)]
if n == 1:
    print(1)
    quit()
while 1:
    save_j = 0

    for j in range(k, n - k):
        counter += 1
        list_items[i][j] = counter
        save_j = j
    for i in range(k + 1, n - k):
        counter += 1
        list_items[i][save_j] = counter
    for j in range(n - k - 2, k - 1, -1):
        counter += 1
        list_items[save_j][j] = counter
    for i in range(n - k - 2, k, -1):
        counter += 1
        list_items[i][k] = counter
    k += 1
    if counter == n * n:
        break
for i in list_items:
    for j in i:
        print(j, end=' ')
    print()
