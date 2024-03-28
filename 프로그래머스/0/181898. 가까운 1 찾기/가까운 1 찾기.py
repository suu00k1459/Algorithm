def solution(arr, idx):
    try:
        k= arr[idx:].index(1)
    except ValueError:
        return -1 
    else:
         return k+idx