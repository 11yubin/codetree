A = input()

# Please write your code here.
def palindrome(a):
    a = list(a)
    rev_a = list(reversed(a))
    for i in range(len(a)//2):
        if rev_a[i] != a[i]: return False
    return True

if palindrome(A): print('Yes')
else: print('No')
