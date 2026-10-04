a, b = map(int, input().split())

# Please write your code here.
def if_prime(n):
    for i in range(2, n//2+1):
        if n%i == 0: return False
    return True

def get_answer(n):
    if if_prime(n):
        if sum(list(map(int, str(n)))) %2 == 0:
            return True
    return False

answer = 0
for i in range(a, b+1):
    if get_answer(i): answer += 1

print(answer)