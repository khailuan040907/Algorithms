# thuật toán tìm kiếm tuần tự / tuyến tính

# điều kiện : danh sách đã được sắp xếp 
def linear_search(array, start, end, x):

    if start <= end : # Nếu phần tử nằm trong mảng

        if array[start] == x :

            return start
        
        else :

            return linear_search(array, start + 1, end, x)
        
    else : # Nếu phần tử không nằm trong mảng

        return -1

# Chương trình chính
array = [1,2,3,4,5,6,7,8,9,10]
x = int(input("Nhập phần tử bạn muốn tìm trong danh sách : "))

# Gọi hàm
result = linear_search(array, 0, len(array) - 1,x)
if result != -1 :
    print("Vị trí của phần tử bạn muốn tìm là :",result)
else :
    print("Phần tử bạn muốn tìm không có trong danh sách")