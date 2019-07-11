test1 = [1,1,2]
test2 = [17, 17, 3, 17, 17, 17, 17,4]
def findTheStrayNumber(arr):
    res = []
    arr.sort()
    print(arr)
    if len(arr) >= 3:
        for i in range(len(arr)):
            if arr.count(arr[i]) == 1:
                res.append(arr[i])
        return res
    else:
        return 'len(arr) < 3'

print(findTheStrayNumber(test1))
print(findTheStrayNumber(test2))