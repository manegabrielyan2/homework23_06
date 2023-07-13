#merge 
def sortt(arr : list) -> list:
    try:
        for i in range(len(arr)):
            for j in range(i + 1 , len(arr)):
                if arr[i] > arr[j]:
                    arr[i] , arr[j] = arr[j] , arr[i]
        return arr
    except TypeError:
        raise TypeError("You should enter only numbers! ")
def merge(arr1 : list , arr2 : list) -> list:
   
    arr1 = sortt(arr1)
    arr2 = sortt(arr2)
    arr_merge = sortt(arr1 + arr2)
    return arr_merge
    
arr1 = [5 , 4 , 2 , 1]
arr2 = [10 , 9 , 8 , 7 , 6, 90]
try:
    merged = merge(arr1 , arr2)
    print(merged)
except TypeError as te:
    print(str(te))
    
