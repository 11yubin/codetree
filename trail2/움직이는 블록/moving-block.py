n = int(input())
blocks = [int(input()) for _ in range(n)]

# Please write your code here.
sum_of_blocks = sum(blocks)

avg = sum_of_blocks // n
ans = 0
for b in blocks:
    if b > avg:
        ans += b - avg

print(ans)