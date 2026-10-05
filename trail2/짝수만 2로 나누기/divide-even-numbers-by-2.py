n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def get_answer(n):
    if n%2 == 0: return n//2
    else: return n

for i in range(n):
    arr[i] = get_answer(arr[i])

print(' '.join([str(a) for a in arr]))