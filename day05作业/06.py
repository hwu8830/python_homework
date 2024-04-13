# 给定一个10个元素的列表，请完成排序（注意，不要使用系统api）
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# 示例列表
my_list = [64, 34, 25, 12, 22, 11, 90, 45, 87, 1]

# 使用冒泡排序对列表进行排序
bubble_sort(my_list)

# 打印排序后的列表
print("排序后的列表:", my_list)
