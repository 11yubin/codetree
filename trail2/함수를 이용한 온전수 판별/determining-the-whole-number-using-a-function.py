a, b = map(int, input().split())

# Please write your code here.
def get_answer(n):
    if n%2 == 0: return False
    elif list(map(int, str(n)))[-1] == 5: return False
    elif n%3 == 0 and n%9 != 0: return False
    return True

answer = 0
for i in range(a, b+1):
    if get_answer(i): answer += 1

print(answer)