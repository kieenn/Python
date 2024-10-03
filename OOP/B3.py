# 3. Xây dựng lớp PHANSO bao gồm các thuộc tính và phương thức sau:
# + Thuộc tính: mãu số, tử số
# + Viết phương thức __init__ khởi tạo phân số
# + Viêt phương thức sau
# - Nhập phân số input()
# - Phương thức __str__ trả về phân số dạng a/b (dạng tối giản) và in ra màn hình thông qua gọi hàm
# print()
# - Rút gọn phân số.
# - Nghịch đảo phân số
#
# - Viết các phương thức my_addition(), my_subtract(), my_multi(), my_division()cộng, trừ, nhân,
# chia hai phân số.
# - Viết các phương thức nạp chồng toán tử cho các phép toán +, -, *, /
class PHANSO:
    def __init__(self, tu_so=0, mau_so=1):
        if mau_so == 0:
            raise ZeroDivisionError("Mẫu số không được bằng 0")
        self.tu_so = tu_so
        self.mau_so = mau_so

    def input(self):
        self.tu_so = int(input("Nhập tử số: "))
        self.mau_so = int(input("Nhập mẫu số: "))
        while self.mau_so == 0:
            print("Mẫu số không được bằng 0. Vui lòng nhập lại.")
            self.mau_so = int(input("Nhập mẫu số: "))

    def __str__(self):
        gcd = self.gcd(abs(self.tu_so), abs(self.mau_so))
        return f"{self.tu_so // gcd}/{self.mau_so // gcd}"

    def gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def rut_gon(self):
        gcd = self.gcd(abs(self.tu_so), abs(self.mau_so))
        self.tu_so //= gcd
        self.mau_so //= gcd

    def nghich_dao(self):
        if self.tu_so == 0:
            raise ZeroDivisionError("Phân số không có nghịch đảo")
        return PHANSO(self.mau_so, self.tu_so)

    def my_addition(self, other):
        return PHANSO(self.tu_so * other.mau_so + self.mau_so * other.tu_so,
                       self.mau_so * other.mau_so)

    def my_subtract(self, other):
        return PHANSO(self.tu_so * other.mau_so - self.mau_so * other.tu_so,
                       self.mau_so * other.mau_so)

    def my_multi(self, other):
        return PHANSO(self.tu_so * other.tu_so,
                       self.mau_so * other.mau_so)

    def my_division(self, other):
        if other.tu_so == 0:
            raise ZeroDivisionError("Không thể chia cho 0")
        return PHANSO(self.tu_so * other.mau_so,
                       self.mau_so * other.tu_so)

    def __add__(self, other):
        return self.my_addition(other)

    def __sub__(self, other):
        return self.my_subtract(other)

    def __mul__(self, other):
        return self.my_multi(other)

    def __truediv__(self, other):
        return self.my_division(other)

# Ví dụ sử dụng
p1 = PHANSO(2, 3)
p2 = PHANSO(4, 5)
print(p1)
print(p1 + p2)
print(p1 - p2)
print(p1 * p2)
print(p1 / p2)