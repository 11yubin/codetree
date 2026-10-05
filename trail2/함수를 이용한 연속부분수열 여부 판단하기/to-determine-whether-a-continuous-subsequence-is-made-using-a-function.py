n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Please write your code here.
def get_answer(a, b):
    answer = False
    cur = 0
    i = 0
    for i in range(n1):
        if a[i] == b[0]:
            for j in range(n2):
                if 0<=i+j<n1:
                    if a[i+j] != b[j]:
                        break
                    else:
                        if j == n2-1:
                            answer = True


    return answer

if get_answer(a, b): print('Yes')
else: print('No')