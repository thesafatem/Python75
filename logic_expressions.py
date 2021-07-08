"""
LOGICAL OPERATORS:
== -> равно ли?
!= -> не равно ли?
> -> больше
< -> меньше
>= -> больше или равно
<= -> меньше или равно
not -> не
and -> True if all True
or -> False if all False
xor -> работает только с двумя выражениями
        True if only one True
"""

x = 5
print(x == 5)
print(x > 5)
print(x <= 5)
print(not(x == 5))

a = [1, 2, 1, 1, 1, 2, 1, 2, 2]

cnt = 0
for i in range(len(a)):
    cnt += a[i] == 2
    # if a[i] == 2:
    #     cnt += 1
print(cnt)