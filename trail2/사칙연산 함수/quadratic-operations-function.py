a, o, c = input().split()
a = int(a)
c = int(c)

# Please write your code here.
def calculate(a, o, c):
    if o == '+':
        print(f'{a} + {c} = {a+c}'); return
    elif o == '-':
        print(f'{a} - {c} = {a-c}'); return
    elif o == '/':
        print(f'{a} / {c} = {int(a/c)}'); return
    elif o == '*':
        print(f'{a} * {c} = {int(a*c)}'); return
    else: print(False); return

calculate(a, o, c)