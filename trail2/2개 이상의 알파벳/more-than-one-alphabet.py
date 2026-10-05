A = input()

# Please write your code here.
def get_answer(A):
    set_a = set(A)

    if len(set_a) > 1: return True
    else: return False

if get_answer(A): print("Yes")
else: print("No")