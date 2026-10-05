n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def get_answer(arr):
    for i in range(n):
        arr[i] = abs(arr[i])
    print(' '.join([str(a) for a in arr]))

get_answer(arr)