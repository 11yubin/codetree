a, b = map(int, input().split())

# Please write your code here.
def if_prime(n):
    for i in range(2, n//2+1):
        if n%i == 0: return False
    return True

answer = 0
for j in range(a, b+1):
    if if_prime(j):
        answer += j

print(answer)