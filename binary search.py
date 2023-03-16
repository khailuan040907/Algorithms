# thuật toán tìm kiếm nhị phân (tìm phần tử x có trong danh sách không, chỉ tìm index)

# điều kiện : danh sách đã được sắp xếp từ nhỏ đến lớn

def binary_search(array, left, right, x) :

    if left <= right : # Nếu phần tử nằm trong mảng

        mid = (left + right) // 2

        if array[mid] == x : #Nếu phần tử nằm ở giữa mảng

            return mid 
        
        elif array[mid] > x : #Nếu phần tử nhỏ hơn mid, nó sẽ nằm ở phía bên trái của mảng (từ left cho đến mid - 1)

            return binary_search(array, left , mid - 1 , x)
        
        else :  #Nếu phần tử lớn hơn mid, nó sẽ nằm ở phía bên phải của mảng (từ mid + 1 cho đến right)

            return binary_search(array, mid + 1, right , x)
    else : # Phần tử không nằm trong tập hợp
        return -1
# Khởi tạo danh sách và tham số x
array = [0,1,2,3,4,5,6,7,8,9]
x = int(input("Nhập số bạn muốn tìm trong dãy 0 -> 9 : "))

# Gọi hàm
result = binary_search(array, 0 , len(array) - 1 , x)
if result != -1 :
    print("Phần tử bạn cần tìm ở vị trí :",result)
else :
    print("Phần tử bạn cần tìm không có trong danh sách")