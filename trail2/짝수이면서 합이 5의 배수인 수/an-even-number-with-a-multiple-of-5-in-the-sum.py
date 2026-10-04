n = int(input())

# Please write your code here.
def get_answer(n):
    if n % 2 == 0:
        if sum(list(map(int, str(n)))) % 5 == 0:
            return True
    
    return False

answer = get_answer(n)
if answer:
    print('Yes')
else:
    print('No')