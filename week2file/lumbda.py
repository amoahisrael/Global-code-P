def is_even(x):
    if x % 2==0:
        return x

numbers = [1,56,234,87,4,76,24,69,90,135]
filter(is_even, numbers)

print(list(filter(is_number)))
a=list(filter(lambda x: x% 2==0, numbers))
print(a)

