"""a = 8
b = 6.23
c = 'строка'

print(a, b, c)
print(f"{a} - {b} - {c}")
print("{} | {} | {}".format(a, b, c))"""


n = 4423
sum = 0
while n > 0:
    m = n % 10
    sum += m
    n //= 10
print(sum)