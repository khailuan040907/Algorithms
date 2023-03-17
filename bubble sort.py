# thuật toán sắp xếp nổi bọt (bubble sort)

def bubble_sort(array, start, end):
    for i in range(start, end) :
        for j in range (start, end - i) :
            if array[j] > array[j+1] :
                array[j], array[j+1] = array[j+1], array[j]
    return array     
       
# Chương trình chính
array = [1,3,4,5,2,10,7,9,8,6]

# Gọi hàm
result = bubble_sort(array, 0, len(array) - 1)
print(result)