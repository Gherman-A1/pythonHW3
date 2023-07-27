# Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.
# list_1 = [1, 2, 3, 4, 5]
# k = 6
# # 5

list_1 = [1, 2, 3, 4, 5]
k = 6
closest_number=list_1[0]
min_difference=abs(k-list_1[0])
for i in range(len(list_1)):
    difference=abs(k-list_1[i])
    if difference<min_difference:
        min_difference=difference
        closest_number=list_1[i]
print(closest_number)