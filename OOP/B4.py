# 4. Xây dựng lớp Shape có các thuộc tính và phương thức sau:
# + Thuộc tính : color (chuỗi), name (chuỗi)
# + Viết phương thức __init__ khởi tạo shape
# + Viết phương thức findarea() (tính diện tích của hình) dùng lệnh pass để bỏ qua body
# + Viết phương thức findperimeter () (tính chu vi của hình) dùng lệnh pass để bỏ qua body
# + Viết phương thức __str__ trả về tên (name) của shape
#
# Xây dựng hai lớp Circle và Rectangle kế thừa lớp shape
# Lớp Circle có các thuộc tính và phương thức thêm sau:
# + Thuộc tính: radius (số thực)
# + Viết phương thức __init__ khởi tạo Circle (ghi đè từ lớp shape)
# + Viết phương thức findarea() và findperimeter () cụ thể cho lớp Circle
# Lớp Rectangle có các thuộc tính và phương thức thêm sau:
# + Thuộc tính: width và heigth (số thực)
# + Viết phương thức __init__ khởi tạo Rectangle (ghi đè từ lớp shape)
# + Viết phương thức findarea() và findperimeter () cụ thể cho lớp Rectangle
#
# Xây dựng hai lớp Square kế thừa từ lớp Rectangle
# Lớp Square có các thuộc tính và phương thức thêm sau:
# + Viết phương thức __init__ khởi tạo Square
# + Viết phương thức findarea() và findperimeter () cụ thể cho lớp Square
class Shape:
    def __init__(self, color, name):
        self.color = color
        self.name = name

    def findarea(self):
        pass

    def findperimeter(self):
        pass

    def __str__(self):
        return f"Tên hình: {self.name}"

class Circle(Shape):
    def __init__(self, color, name, radius):
        super().__init__(color, name)
        self.radius = radius

    def findarea(self):
        return 3.14 * self.radius ** 2

    def findperimeter(self):
        return 2 * 3.14 * self.radius

class Rectangle(Shape):
    def __init__(self, color, name, width, height):
        super().__init__(color, name)
        self.width = width
        self.height = height

    def findarea(self):
        return self.width * self.height

    def findperimeter(self):
        return 2 * (self.width + self.height)

class Square(Rectangle):
    def __init__(self, color, name, side):
        super().__init__(color, name, side, side)

# Ví dụ sử dụng
c = Circle("red", "Circle", 5)
print(c.findarea())
print(c.findperimeter())
r = Rectangle("blue", "Rectangle", 4, 6)
print(r.findarea())
print(r.findperimeter())
s = Square("green", "Square", 3)
print(s.findarea())
print(s.findperimeter())