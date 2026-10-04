n = int(input())

# Please write your code here.
def get_answer(n):
    answer = n * (n+1) / 2
    answer //= 10
    return int(answer)

print(get_answer(n))