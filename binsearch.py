def binarySearch(lst, beg, end, x):
    while beg <= end:
        mid = (beg + end) //2;
        if lst[mid] == x:
            return mid
        elif lst[mid] < x:
            beg = mid + 1
        else:
            end = mid - 1 
    return -1
a=[]
b=int(input("enter no of elements"))
for i in range(b):
    c=int(input("enter number one by one"))
    a.append(c)
x=int(input("enter element to be searched"))
a=sorted(a)
result = binarySearch(a, 0, len(a)-1, x)
 
if result != -1:
    print ("Element is present at index %d" % result)
else:
    print ("Element is not present in list")
