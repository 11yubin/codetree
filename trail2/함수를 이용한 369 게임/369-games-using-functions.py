a, b = map(int, input().split())

# Please write your code here.
def three_six_nine(n):
    if n % 3 == 0: return True
    n_list = list(map(int, str(n)))

    if 3 in n_list or 6 in n_list or 9 in n_list:
        return True
    return False

answer = 0
for i in range(a, b+1):
    if three_six_nine(i):
        answer += 1

print(answer)