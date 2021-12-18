

def search(list, n):
    l = 0
    u = len(list)- 1

    while l <= u:
        mid = (l+n) // 2
        if list(mid) == n:
            globals()['pos']= mid
            return True
        else:
            if list(mid)<n:
                l = mid
            else:
                u = mid
list = [1,3,23,34,5,6]
list.sort()
n = 23
result = search(list,  n)

if result != -1:
    print("your number is found at", str(result))
else:
    print("Not found")
