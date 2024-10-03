# B.
# 1. Tạo một class Student bao gồm các thuộc tính và phương thức sau:
# + Thuộc tính : name (là một chuỗi lưu trữ tên sinh viên)
# number ( là số lượng môn thi, giả sử number >=5)
# score (là một list lưu trữ điểm thi của các môn thi)
# + Viết phương thức khởi tạo: __init()__ (ban đầu khởi tạo list score toàn số 0)
# + Viết phương thức getName() trả về tên sinh viên
# + Viết phương thức getScore(i) trả về điểm của môn thi thứ i ( giả sử chỉ số i đúng yêu cầu chỉ số)
# + Viết phương thức inputScore() nhập vào điểm các môn thi
# + Viết phương thức getAverage() trả về điểm trung bình.
# + Viết phương thức getHighScore() trả về điểm thi cao nhất.
# + Viết phương thức xem Student có được học bổng không? Được học bổng khi điểm trung bình lớn hơn
# 8.0 và không có môn thi nào dưới 4.
# + Viết phương thức __str__ trả về chuỗi diễn giải thông tin của sinh viên (name và score) thông qua gọi
# hàm print.
# Ví dụ :
# s = Student("An", 5)
# s.inputScore()
# print(s)
# print(s.getAverage())
# #....
class Student:
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.score = [0] * self.number

    def getName(self):
        return self.name

    def getScore(self, i):
        if 0 <= i < self.number:
            return self.score[i]
        else:
            return "Chỉ số không hợp lệ"

    def inputScore(self):
        print("Nhập điểm các môn thi:")
        for i in range(self.number):
            self.score[i] = float(input(f"Môn {i+1}: "))

    def getAverage(self):
        return sum(self.score) / self.number

    def getHighScore(self):
        return max(self.score)

    def checkScholarship(self):
        if self.getAverage() > 8.0 and all(score >= 4 for score in self.score):
            return "Học sinh đạt học bổng"
        else:
            return "Học sinh không đạt học bổng"

    def __str__(self):
        return f"Tên học sinh: {self.name}\nĐiểm các môn: {self.score}"

# Ví dụ sử dụng
s = Student("An", 5)
s.inputScore()
print(s)
print(s.getAverage())
print(s.getHighScore())
print(s.checkScholarship())