y = int(input())

# Please write your code here.
def if_year(n):
    if n%4 == 0:
        if n%100 == 0 and n%400 != 0: 
            print('false')
            return 
        print('true')
        return 
    print('false')
    return False

if_year(y)