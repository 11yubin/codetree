a, b = map(int, input().split())

# Please write your code here.

def get_answer(a, b):
    min, max = 0, 0
    if a > b: 
        a += 25
        b *= 2
    else:
        a *= 2
        b += 25

    return a, b

res1, res2 = get_answer(a, b)
print(res1, res2)