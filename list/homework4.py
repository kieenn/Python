# 1. L = [2 ,4, 9, 3, 5]. Cho biết kết quả các câu lệnh sau:
# a. L[2]
# b. L[-1]
# c. len(L)
# d. L[0:2]
# e. 0 in L
# f. L + [24, 1, 4]
# g. tuple(L)
def a(L):
  print("L[2]:", L[2])

def b(L):
  print("L[-1]:", L[-1])

def c(L):
  print("len(L):", len(L))

def d(L):
  print("L[0:2]:", L[0:2])

def e(L):
  print("0 in L:", 0 in L)

def f(L):
  print("L + [24, 1, 4]:", L + [24, 1, 4])

def g(L):
  print("tuple(L):", tuple(L))

# 2. L = [2 ,4, 9, 3, 5]. Viết các câu lệnh thực hiện các yêu cầu sau đây:
# a. Thay thế phần tử đầu tiên thành số âm tương ứng.
# b. Thêm 20 vào cuối danh sách.
# c. Thêm số 0 vào vị trí thứ 3 trong danh sách.
# d. Xóa phần tử tại vị trí số 4 trong danh sách.
# e. Thêm list [0,0,0] vào sau danh sách trên.
# f. Sắp xếp danh sách giảm dần.

def thay_the_phan_tu_dau_tien(L):
  L[0] = -L[0]
  print("Danh sách sau khi thay thế:", L)

def them_phan_tu_vao_cuoi(L):
  L.append(20)
  print("Danh sách sau khi thêm:", L)

def them_phan_tu_vao_vi_tri_thu_3(L):
  L.insert(3, 0)
  print("Danh sách sau khi thêm:", L)

def xoa_phan_tu_tai_vi_tri_thu_4(L):
  del L[4]
  print("Danh sách sau khi xóa:", L)

def them_list_vao_sau(L):
  L.extend([0, 0, 0])
  print("Danh sách sau khi thêm:", L)

def sap_xep_giam_dan(L):
  L.sort(reverse=True)
  print("Danh sách sau khi sắp xếp:", L)

# B.
# 1. Cho một danh sách bao gồm các chuỗi chứa các chữ số.
# Ví dụ: A = [‘3’, ‘27’,’5’,’123’,’9’,’1’]
# Viết hàm sắp xếp chuỗi tăng dần theo hai kiểu (string compare hoặc integer compare)
# Ví dụ:
# • string compare ( so sánh theo thứ tự từ điển)
#
# Danh sách A sau khi được sắp xếp [‘1’, ‘123’,’27’,’3’,’5’,’9’]
#
# • integer compare (so sánh theo số nguyên)
#
# Danh sách A sau khi được sắp xếp [‘1’, ‘3’,’5’,’9’,’27’,’123’]
#
# ❖ Gợi ý dùng sorted() và key function
def sap_xep_chuoi(A, theo_kieu="string"):
    """Sắp xếp chuỗi tăng dần theo hai kiểu: string compare hoặc integer compare."""
    if theo_kieu == "string":
        return sorted(A)
    elif theo_kieu == "integer":
        return sorted(A, key=int)
    else:
        raise ValueError("Kiểu sắp xếp không hợp lệ")

# 2. Viết chương trình in list sau khi đã xóa số tại vị trí thứ 1, thứ 2, thứ 3, thứ 6 trong [12,24,35,70,88,120,155].
#
# * Dùng list comprehension và enumerate()
def xoa_phan_tu_tai_vi_tri(A):
    """In list sau khi đã xóa số tại vị trí thứ 1, thứ 2, thứ 3, thứ 6 trong [12,24,35,70,88,120,155]."""
    B = [x for i, x in enumerate(A) if i not in [1, 2, 3, 6]]
    print("Danh sách sau khi xóa:", B)

# 3. Xóa các phần tử trùng nhau trong list.
# a) Dùng vòng lặp, Yêu cầu không dùng hàm của kiểu dữ liệu dictionary và set
# b) Không ràng buộc
# Ví dụ:
# Input A = [1, 2, 3, 1, 2, 5, 6, 7, 8]
# Output B = [1, 2, 3, 5, 6, 7, 8]

def xoa_trung_lap(A):
    """Xóa các phần tử trùng nhau trong list."""
    B = []
    for x in A:
        if x not in B:
            B.append(x)
    return B

def xoa_trung_lap_khong_rang_buoc(A):
  """Xóa các phần tử trùng nhau trong list (không ràng buộc)."""
  B = list(dict.fromkeys(A))
  return B

# 4. Đếm số lần xuất hiện của các phần tử trong list.
# a) Dùng vòng lặp, Yêu cầu không dùng hàm của kiểu dữ liệu dictionary, set hay module collections
# b) Không ràng buộc
# Ví dụ: A = [1,1,1,1,2,2,2,2,3,3,4,5,5]
# Output: 1: 4, 2: 4, 3:2, 4:1, 5:2

def dem_phan_tu(A):
    """Đếm số lần xuất hiện của các phần tử trong list."""
    counts = {}
    for x in A:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    for x, count in counts.items():
        print(f"{x}: {count}", end=", ")
from collections import Counter
def dem_phan_tu_khong_rang_buoc(A):
    """Đếm số lần xuất hiện của các phần tử trong list (không ràng buộc)."""
    counts = Counter(A)
    for x, count in counts.items():
        print(f"{x}: {count}", end=", ")

# 5. Viết chương trình nhập một list chứa các số nguyên dương theo các yêu cầu sau:
# a) nhập trước số phần từ của list, sau đó nhập từng phần tử.
# b) không nhập trước số lượng phần tử, quá trình nhập kết thức nếu nhập vào số -1.

def nhap_list_so_nguyen_duong_truoc_so_phan_tu():
    """Nhập một list chứa các số nguyên dương theo yêu cầu: nhập trước số phần từ của list, sau đó nhập từng phần tử."""
    n = int(input("Nhập số phần tử: "))
    A = []
    for i in range(n):
        x = int(input(f"Nhập phần tử thứ {i+1}: "))
        A.append(x)
    print("Danh sách đã nhập:", A)

def nhap_list_so_nguyen_duong_khong_truoc_so_luong():
    """Nhập một list chứa các số nguyên dương theo yêu cầu: không nhập trước số lượng phần tử, quá trình nhập kết thúc nếu nhập vào số -1."""
    A = []
    x = int(input("Nhập số nguyên dương (-1 để kết thúc): "))
    while x != -1:
        A.append(x)
        x = int(input("Nhập số nguyên dương (-1 để kết thúc): "))
    print("Danh sách đã nhập:", A)

# 6. Cho 2 list như sau: ( 2 list có thể khác độ dài)
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# Viết chương trình tạo ra một list chứa các phần tử chung của 2 list ban đầu theo các yêu cầu sau:
# a) Không dùng List Comprehension
# b) Dùng List Comprehension

def tim_phan_tu_chung_khong_list_comprehension(a, b):
    """Tìm phần tử chung của 2 list (không dùng List Comprehension)."""
    c = []
    for x in a:
        if x in b and x not in c:
            c.append(x)
    return c

def tim_phan_tu_chung_list_comprehension(a, b):
    """Tìm phần tử chung của 2 list (dùng List Comprehension)."""
    c = set([x for x in a if x in b])
    return c