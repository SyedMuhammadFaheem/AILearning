#Task 5
arr=[1,2,3,4,6,7]
def findDup(arrParam):
    n=arr[0]
    for i in range(len(arr)):
        if i>0:
            if n==arr[i]:
                return True
            else:
                n=arr[i]
    return False

print(findDup(arr))