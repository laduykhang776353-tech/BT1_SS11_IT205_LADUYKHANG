# # Thông tin sản phẩm ban đầu
# product_info = ("SP001", "Áo polo nam", "Size L", 299000)

# # Lấy mã sản phẩm
# product_code = product_info[1]

# # Lấy tên sản phẩm
# product_name = product_info[2]

# # Đếm số lượng thông tin sản phẩm
# product_length = product_info.length()

# # Cập nhật giá bán
# product_info[3] = 279000

# print("Mã sản phẩm:", product_code)
# print("Tên sản phẩm:", product_name)
# print("Số lượng thông tin sản phẩm:", product_length)
# print("Thông tin sản phẩm sau cập nhật:", product_info)

# Tuple product_info ban đầu có bao nhiêu phần tử: 4 phần tử
# Phần tử "SP001" đang nằm ở index[0]
# Vì sao dòng product_code = product_info[1] lỗi:
# Do "SP001" đang nằm ở vị trí index[0] mà đoạn code nó lại gán index[1] 
# Nên khi lấy ra mã sản phẩm thì nó sẽ lấy giá trị ở index[1] là "Áo polo nam" ==> Sai

# Phần tử "Áo polo nam" đang nằm ở index[1]
# lấy sai tên sản phẩm là do "Áo polo nam" đang là index[1] mà đoạn code lại gán index[2] ==> sai yêu cầu

# Vì sao dòng sau gây lỗi?
# product_length = product_info.length()
# Tuple trong Python không có method .length()

# Muốn đếm số phần tử trong tuple, cần dùng hàm nào: hàm len()

# Vì sao dòng sau không hợp lệ?
# product_info[3] = 279000
# Vì:

#Tuple là kiểu dữ liệu immutable (không thể thay đổi)
#Không cho phép sửa trực tiếp phần tử bằng index

#Tuple có cho phép sửa trực tiếp phần tử không: không

# code chuẩn
# Thông tin sản phẩm ban đầu
product_info = ("SP001", "Áo polo nam", "Size L", 299000)

# Lấy mã sản phẩm
product_code = product_info[0]

# Lấy tên sản phẩm
product_name = product_info[1]

# Đếm số lượng thông tin sản phẩm
product_length = len(product_info)

# Cập nhật giá bán
product_info = product_info[:3] + (279000,)

print("Mã sản phẩm:", product_code)
print("Tên sản phẩm:", product_name)
print("Số lượng thông tin sản phẩm:", product_length)
print("Thông tin sản phẩm sau cập nhật:", product_info)