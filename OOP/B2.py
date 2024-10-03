# 2. Tạo một class có tên MyComplexNumber bao gồm các thuộc tính và phương thức sau:
# + Thuộc tính: phần thực
#
# phần ảo
# + Viết phương thức khởi tạo __init()__
# + Viết phương thức __str__ trả về chuỗi in số phức ra màn hình thông qua gọi hàm print()
# + Viết phương thức input() nhập vào số phức
# + Viết phương thức my_addition(), my_subtract(), my_multi(), my_division() cộng, trừ, nhân, chia hai số
# phức.
# + Viết các phương thức __add__ , __sub__, __mul__, __truediv__ nạp chồng toán tử +, -, *, / cho hai số
# phức
# + Viết phương thức tính độ lớn của số phức
# + Viết phương thức compare() so sánh hai số phức
# + Viết phương thức __eq__, __lt__, __gt__ nạp chồng cho các toán tử == ; < ; > so sánh hai số phức.
# Ví dụ:
# I = MyComplexNumber(10,2)
# J = MyComplexNumber()
# J.input()
# print(I); print(J)
# print(I.addition(J))
# print(I+J)
# print(I==J)
# I.compare(J)
class MyComplexNumber:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def __str__(self):
        if self.imag >= 0:
            return f"{self.real} + {self.imag}i"
        else:
            return f"{self.real} - {-self.imag}i"

    def input(self):
        self.real = float(input("Nhập phần thực: "))
        self.imag = float(input("Nhập phần ảo: "))

    def my_addition(self, other):
        return MyComplexNumber(self.real + other.real, self.imag + other.imag)

    def my_subtract(self, other):
        return MyComplexNumber(self.real - other.real, self.imag - other.imag)

    def my_multi(self, other):
        return MyComplexNumber(self.real * other.real - self.imag * other.imag,
                                 self.real * other.imag + self.imag * other.real)

    def my_division(self, other):
        denominator = other.real ** 2 + other.imag ** 2
        return MyComplexNumber((self.real * other.real + self.imag * other.imag) / denominator,
                                 (self.imag * other.real - self.real * other.imag) / denominator)

    def __add__(self, other):
        return self.my_addition(other)

    def __sub__(self, other):
        return self.my_subtract(other)

    def __mul__(self, other):
        return self.my_multi(other)

    def __truediv__(self, other):
        return self.my_division(other)

    def modulus(self):
        return (self.real ** 2 + self.imag ** 2) ** 0.5

    def compare(self, other):
        if self.real == other.real and self.imag == other.imag:
            print("Hai số phức bằng nhau")
        else:
            print("Hai số phức không bằng nhau")

    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag

    def __lt__(self, other):
        return self.modulus() < other.modulus()

    def __gt__(self, other):
        return self.modulus() > other.modulus()

# Ví dụ sử dụng
I = MyComplexNumber(10, 2)
J = MyComplexNumber()
J.input()
print(I); print(J)
print(I.my_addition(J))
print(I + J)
print(I == J)
I.compare(J)