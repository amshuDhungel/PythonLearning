
#Sonali Shrivastav
#3 days ago (edited)
#6:45:12   Sum of n natural numbers using recursive

def sum_recursive(n):

    if n<1:
        return 0
    return n + sum_recursive(n-1)
f = sum_recursive(2)
print(f)
