#from function import even 
#num=[2,6,8,12]


def is_even(x):
    return x % 2 ==0;

numbers = [1,56,234,87,4,76,24,69,90,135]

a = (list(filter (is_even, numbers)))
print(a)
