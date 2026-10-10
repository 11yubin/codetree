n, m = map(int, input().split())
A = list(map(int, input().split()))
answer = 0

# Please write your code here.
def get_answer(m):
    global answer
    answer += A[m-1]
    if m == 1: 
        return 
    elif m%2 == 0: 
        m //= 2
    else:
        m -= 1
    return get_answer(m)

get_answer(m)
print(answer)