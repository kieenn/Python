def xoa_trung_lap(A):
    """Xóa các phần tử trùng nhau trong list."""
    B = []
    for x in A:
        if x not in B:
            B.append(x)
    return B

def xoa_trung_lap_khong_rang_buoc(A):
  """Xóa các phần tử trùng nhau trong list (không ràng buộc)."""
  B = list(set(A))
  return B

A = [1, 2, 3, 1, 2, 5, 6, 7, 8]

print(xoa_trung_lap(A))
print(xoa_trung_lap_khong_rang_buoc(A))