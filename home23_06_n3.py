#is_sorted tarberak 1
"""
def is_sorted(arr : list) -> list:
    sort_arr = arr[:]
    for i in range(len(arr)):
        for j in range(i + 1 , len(arr)):
            if sort_arr[i] > sort_arr[j]:
                sort_arr[i] , sort_arr[j] = sort_arr[j] , sort_arr[i]
            if arr == sort_arr:
                return 1
            else:
                return 0
lst = [ 5 , 4 , 3, 2 , 1]
i = is_sorted(lst)
if i == 1:
    print("The list was sorted. ")
else:
    print("List wasn't sorted. ")
"""
#tarberak 2
def is_sorted(arr : list) -> list:
    try:
        for i in range(len(arr)):
            for j in range(i + 1 , len(arr)):
                if arr[i] > arr[j]:
                    print("List is not sorted. ")
                    return False
        print("List is sorted. ")
        return True   
    except TypeError:
        raise TypeError("You should enter only numbers. ")     
lst = [1 , 2 , 3, 4 ,5]
try:
    is_sorted(lst)
except TypeError as te:
    print(str(te))
            
    