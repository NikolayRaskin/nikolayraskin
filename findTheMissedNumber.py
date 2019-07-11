string = "578910"
def find_number(start,end,string):
    res = []
    for i in range(start,end+1):
        i = str(i)
        if string.find(i) == -1:
            res.append(i)
    return res
print(find_number(5, 10, string))