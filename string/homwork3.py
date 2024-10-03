# 1. Giả sử chuỗi s = “pythonfile.py”. Kiểm tra kết quả các lệnh sau:
#a. s[2]
# b. s[-1]
# c. len(s)
# d. s[0:7]
# e. Viết lệnh trích chuỗi con “file” từ s
# f. Viết lệnh trích trích chuỗi con “.py” từ s
# g. Viết vòng lặp in chuỗi theo thứ tự ngược lại
def lay_ky_tu_thu_3(s):
    print('s[2]:', s[2])

def lay_ky_tu_cuoi_cung(s):
    print('s[-1]:', s[-1])

def tinh_do_dai_chuoi(s):
    print('len(s):', len(s))

def lay_chuoi_con_tu_0_den_7(s):
    print('s[0:7]:', s[0:7])

def lay_chuoi_con_file(s):
    print('s[8:12]:', s[8:12])

def lay_chuoi_con_py(s):
    print('s[-3:]:', s[-3:])

def in_chuoi_nguoc(s):
    for i in range(len(s) - 1, -1, -1):
        print(s[i], end="")


# 2. Viết lệnh chuyển đổi các yêu cầu sau đây
# a. Chuyển 11001 ở hệ nhị phân sang decimal
# b. Chuyển 47 ở hệ decimal sang binary
# c. Chuyển AF1 hệ hexadecimal sang decimal
# d. Chuyển 127 ở hệ octal sang binary

def nhi_phan_sang_thap_phan(binary_number):
    decimal_number = int(binary_number, 2)
    print("Số thập phân:", decimal_number)

def thap_phan_sang_nhi_phan(decimal_number):
    binary_number = bin(decimal_number)[2:]
    print("Số nhị phân:", binary_number)

def hexa_sang_thap_phan(hexadecimal_number):
    decimal_number = int(hexadecimal_number, 16)
    print("Số thập phân:", decimal_number)

def bat_phan_sang_nhi_phan(octal_number):
    decimal_number = int(octal_number, 8)
    binary_number = bin(decimal_number)[2:]
    print("Số nhị phân:", binary_number)

# B.1: Sắp xếp từ theo thứ tự từ điển
def sap_xep_tu(s):
    """Tách chuỗi thành các từ và in ra theo thứ tự từ điển."""
    words = s.split()
    words.sort()
    for word in words:
        print(word)

# B.2: Chuyển đổi nhị phân sang thập phân
def nhi_phan_sang_thap_phan(s):
    """Chuyển đổi chuỗi các số nhị phân sang thập phân."""
    numbers = s.split(',')
    for number in numbers:
        decimal = int(number, 2)
        print(decimal, end=", ")

# B.3: Đếm số lần xuất hiện của các ký tự
def dem_ky_tu(s):
    """Đếm số lần xuất hiện của các ký tự trong chuỗi."""
    counts = {}
    for char in s:
        if char.isalpha():  # Kiểm tra xem ký tự có phải chữ cái không
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
    for char, count in counts.items():
        print(f"{char}: {count}")

# B.4: Chuyển ký tự đầu tiên của mỗi từ sang chữ hoa
def hoa_ky_tu_dau(s):
    """Chuyển ký tự đầu tiên của mỗi từ sang chữ hoa."""
    words = s.split()
    result = ' '.join([word.capitalize() for word in words])
    print(result)

# B.5: Đếm số lượng chữ cái in hoa, in thường
def dem_chu_cai(s):
    """Đếm số lượng chữ cái in hoa, in thường."""
    upper_count = 0
    lower_count = 0
    for char in s:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    print("Chữ cái in hoa:", upper_count)
    print("Chữ cái in thường:", lower_count)

# B.6: In ra các số nguyên tố
def in_so_nguyen_to(s):
    """In ra các số nguyên tố trong chuỗi."""
    numbers = [int(num) for num in s.split(',')]
    for number in numbers:
        if is_prime(number):
            print(number, end=", ")

def is_prime(n):
    """Kiểm tra xem một số có phải là số nguyên tố hay không."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# B.7: Đếm số lần xuất hiện của mỗi từ
def dem_tu(s):
    """Đếm số lần xuất hiện của mỗi từ trong chuỗi."""
    words = s.split()
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    for word, count in word_counts.items():
        print(f"{word}: {count}")