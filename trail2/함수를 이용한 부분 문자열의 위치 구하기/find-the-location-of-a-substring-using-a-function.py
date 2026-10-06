text = input()
pattern = input()

# Please write your code here.
answer = -1

def get_pattern(ti, pi):
    global answer
    if 0<=ti<len(text) and 0<=pi<len(pattern):
        if text[ti] == pattern[pi]:
            if pi == len(pattern) -1:
                answer = ti - len(pattern) + 1
                return
            return get_pattern(ti+1, pi+1)

for i in range(len(text)):
    if text[i] == pattern[0]:
        if answer == -1:
            get_pattern(i, 0)
    
print(answer)