def cacluate(*args):
    avg = sum(args)/len(args)
    arr = []
    for i in args:
        if i > avg:
            arr.append(i)
    return avg, arr
print(cacluate(1,2,3,4,5,6,))
