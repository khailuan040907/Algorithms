# thuật toán sắp xếp chọn trực tiếp (SelectionSort)

def selection_sort(array) :
    for i in range(len(array)):
        for j in range(i+1,len(array)) :
            if array[i] > array[j] :
                array[i] , array[j] = array[j], array[i]
    return array

# Chương trình chính
array = [64, 25, 12, 22, 11] 

# Gọi hàm
result = selection_sort(array)
print(result)