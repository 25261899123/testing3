"""Создайте лист из чисел и определите количество четных и не четных."""
numbers = [1, 2, 3, 4, 5, 6]
even = []
odd = []
for num in numbers:
    if num%2 ==0:
        even.append(num)
    else:
        odd.append(num)
        print(even)
        print(odd)





