a, b, c = map(int, input().split())

# Please write your code here.
def get_answer(a, b, c):  
    answer = min(a, b)
    answer = min(answer, c)
    
    return answer

print(get_answer(a, b, c))