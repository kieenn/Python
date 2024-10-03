# A.
# 1. Định nghĩa class có tên là HinhChuNhat bao gồm chiều dài và chiều rộng. Class HinhChuNhat có phương
# thức để tính diện tích. (Dùng __init__ để khởi tạo)
# 2. Định nghĩa một class có tên là Shape và class con là Square. Square có thuộc tính là length. Cả 2 lớp đều
# có hàm getarea() để in diện tích của hình, diện tích mặc định của Shape là 0.
# (Dùng pass để qua body trong phương thức lớp Shape)
class HinhChuNhat:
    def __init__(self, chieu_dai, chieu_rong):
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong

    def tinh_dien_tich(self):
        return self.chieu_dai * self.chieu_rong

class Shape:
    def __init__(self):
        self.area = 0

    def getarea(self):
        print("Diện tích của hình:", self.area)
        pass

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length
        self.area = length * length

    def getarea(self):
        print("Diện tích của hình vuông:", self.area)