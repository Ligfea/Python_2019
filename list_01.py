A = [1, 2, 3]
B = A  # создание синонимичного имени
B[0] = 10
print(A)  # [10, 2, 3], потому что В и А ссылаются на один и тот же список
