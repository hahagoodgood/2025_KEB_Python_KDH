def countdown_loop(n):
    for i in range(n, -1, -1):
        if i ==0:
            print("뱅~~~")
        else:
            print(i)

def countdown_recursion(n):
    if n < 0:
        return
    if n == 0:
        print("팽~~~")
    else:
        print(n)
    countdown_recursion(n-1)

n = int(input())
countdown_loop(n)
countdown_recursion(n)