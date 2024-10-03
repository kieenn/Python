# 5. Phần mềm quản lý nhân viên của công ty được mô tả nghiệp vụ như sau:
# Mỗi nhân viên (Employee) được công ty chia thành 3 loại sau: Nhân viên có kinh nghiệm lâu năm
# (Experience), nhân viên mới ra trường (Fresher) , Nhân viên thực tập (Intern)
# Tất cả các Employee đều có các thuộc tính
# là: ID, FullName, BirthDay,Phone, Email, Employee_type,Employee_count và phương thức
#
# là ShowInfo để hiển thị thông tin của nhân viên đó (hiển thị thông tin nhân viên ra màn hình
# console).
# Trong đó :
# Employee_type có giá trị tương ứng là 0: Experience, 1: Fresher , 2: Intern (tùy vào người dùng
# nhập vào ứng viên loại nào)
# Employee_count dùng để người dùng đếm số lượng nhân viên trong một đợt người dùng nhập
# nhân viên mới vào cơ sở dữ liệu. (mỗi lần người dùng nhập thêm mới nhân viên thì thuộc tính
# Employee_count của class Employee sẽ tăng lên 1)
# Ngoài ra :
# Đối với nhân viên Experience có thêm thuộc tính: Số năm kinh nghiệm (ExpInYear), Kỹ
# năng chuyên môn (ProSkill)
# Đối với nhân viên Fresher có thêm thuộc tính: Thời gian tốt nghiệp(Graduation_date),
# Xếp loại tốt nghiệp (Graduation_rank) , Trường tốt nghiệp (Education)
# Đối với nhân viên Intern có thêm thuộc tính: Chuyên ngành đang học (Majors), Học kì
# đang học (Semester), Tên trường đang học (University_name)
# Lưu ý: Tùy mỗi loại nhân viên, phương thức showMe sẽ được bổ sung thêm các thuộc tính của
# riêng loại nhân viên đó.
# Thực hiện các yêu cầu sau đây:
# a) Hãy thiết kế class và các phương thwucs theo đúng mô hình OOP đã học, áp dụng đầy đủ các tính chất
# : bao đóng (encapsulation) , kế thừa (inheritance) , đa hình (polymorphism).
# b) Xác định và viết hàm __init__ cho các lớp
# c) Viết các hàm kiểm tra tính hợp lệ của ngày sinh, email, tên và số điện thoại của nhân viên.
# d) Viết phương thức cho phép thêm các loại nhân viên trên.
# d) Xử lý ngoại lệ trong trường hợp birthday, email, và phone người dùng nhập vào không hợp lệ.
# e) Viết chương trình tìm tất cả các nhân viên intern.
# f) Viết chương trình tìm tất cả các nhân viên experience
# g) Viết chương trình tìm tất cả các nhân viên fresher.
import datetime

class Employee:
    Employee_count = 0

    def __init__(self, ID, FullName, BirthDay, Phone, Email, Employee_type):
        self.ID = ID
        self.FullName = FullName
        self.BirthDay = BirthDay
        self.Phone = Phone
        self.Email = Email
        self.Employee_type = Employee_type
        Employee.Employee_count += 1

    def validate_birthday(self, birthdate):
        try:
            datetime.datetime.strptime(birthdate, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    def validate_phone(self, phone):
        return phone.isdigit() and len(phone) == 10

    def validate_email(self, email):
        return "@" in email and "." in email

    def validate_name(self, name):
        return name.isalpha()

    def showInfo(self):
        print(f"ID: {self.ID}")
        print(f"Họ và tên: {self.FullName}")
        print(f"Ngày sinh: {self.BirthDay}")
        print(f"Số điện thoại: {self.Phone}")
        print(f"Email: {self.Email}")
        print(f"Loại nhân viên: {self.Employee_type}")

class Experience(Employee):
    def __init__(self, ID, FullName, BirthDay, Phone, Email, Employee_type, ExpInYear, ProSkill):
        super().__init__(ID, FullName, BirthDay, Phone, Email, Employee_type)
        self.ExpInYear = ExpInYear
        self.ProSkill = ProSkill

    def showInfo(self):
        super().showInfo()
        print(f"Số năm kinh nghiệm: {self.ExpInYear}")
        print(f"Kỹ năng chuyên môn: {self.ProSkill}")

class Fresher(Employee):
    def __init__(self, ID, FullName, BirthDay, Phone, Email, Employee_type, Graduation_date, Graduation_rank, Education):
        super().__init__(ID, FullName, BirthDay, Phone, Email, Employee_type)
        self.Graduation_date = Graduation_date
        self.Graduation_rank = Graduation_rank
        self.Education = Education

    def showInfo(self):
        super().showInfo()
        print(f"Thời gian tốt nghiệp: {self.Graduation_date}")
        print(f"Xếp loại tốt nghiệp: {self.Graduation_rank}")
        print(f"Trường tốt nghiệp: {self.Education}")

class Intern(Employee):
    def __init__(self, ID, FullName, BirthDay, Phone, Email, Employee_type, Majors, Semester, University_name):
        super().__init__(ID, FullName, BirthDay, Phone, Email, Employee_type)
        self.Majors = Majors
        self.Semester = Semester
        self.University_name = University_name

    def showInfo(self):
        super().showInfo()
        print(f"Chuyên ngành đang học: {self.Majors}")
        print(f"Học kì đang học: {self.Semester}")
        print(f"Tên trường đang học: {self.University_name}")

def add_employee():
    ID = input("Nhập ID: ")
    FullName = input("Nhập họ và tên: ")
    BirthDay = input("Nhập ngày sinh (YYYY-MM-DD): ")
    Phone = input("Nhập số điện thoại: ")
    Email = input("Nhập email: ")
    Employee_type = int(input("Nhập loại nhân viên (0: Experience, 1: Fresher, 2: Intern): "))

    if not validate_data(BirthDay, Phone, Email, FullName):
        return

    if Employee_type == 0:
        ExpInYear = int(input("Nhập số năm kinh nghiệm: "))
        ProSkill = input("Nhập kỹ năng chuyên môn: ")
        e = Experience(ID, FullName, BirthDay, Phone, Email, Employee_type, ExpInYear, ProSkill)
    elif Employee_type == 1:
        Graduation_date = input("Nhập thời gian tốt nghiệp (YYYY-MM-DD): ")
        Graduation_rank = input("Nhập xếp loại tốt nghiệp: ")
        Education = input("Nhập trường tốt nghiệp: ")
        e = Fresher(ID, FullName, BirthDay, Phone, Email, Employee_type, Graduation_date, Graduation_rank, Education)
    elif Employee_type == 2:
        Majors = input("Nhập chuyên ngành đang học: ")
        Semester = input("Nhập học kì đang học: ")
        University_name = input("Nhập tên trường đang học: ")
        e = Intern(ID, FullName, BirthDay, Phone, Email, Employee_type, Majors, Semester, University_name)
    else:
        print("Loại nhân viên không hợp lệ")
        return

    e.showInfo()

def validate_data(BirthDay, Phone, Email, FullName):
    if not Employee.validate_birthday(Employee, BirthDay):
        print("Ngày sinh không hợp lệ!")
        return False
    if not Employee.validate_phone(Employee, Phone):
        print("Số điện thoại không hợp lệ!")
        return False
    if not Employee.validate_email(Employee, Email):
        print("Email không hợp lệ!")
        return False
    if not Employee.validate_name(Employee, FullName):
        print("Tên không hợp lệ!")
        return False
    return True

def find_intern():
    for i in range(Employee.Employee_count):
        if employees[i].Employee_type == 2:
            employees[i].showInfo()

def find_experience():
    for i in range(Employee.Employee_count):
        if employees[i].Employee_type == 0:
            employees[i].showInfo()

def find_fresher():
    for i in range(Employee.Employee_count):
        if employees[i].Employee_type == 1:
            employees[i].showInfo()

# Ví dụ sử dụng
employees = []
add_employee()
add_employee()
add_employee()
print("Danh sách nhân viên thực tập:")
find_intern()
print("Danh sách nhân viên kinh nghiệm:")
find_experience()
print("Danh sách nhân viên mới ra trường:")
find_fresher()