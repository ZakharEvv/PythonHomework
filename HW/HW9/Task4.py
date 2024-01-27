first = "0 0 0 0 0 0 0"
second = "1 1 1 0 0 0 0"
third = "1 1 1 1 1 1 1"


def tasks(arr):
    res = []
    for i in arr.split():
        res.append(int(i))
    print(res[0] + res[1] + res[2] - res[3] - res[4] - res[5] + res[6])

tasks(second)
