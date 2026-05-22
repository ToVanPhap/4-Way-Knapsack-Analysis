import random

def generate_test_case(n, max_weight=50, max_value=100):
    """
    Hàm sinh dữ liệu ngẫu nhiên cho bài toán Knapsack.
    
    Tham số đầu vào:
    - n: Số lượng món đồ vật cần tạo.
    - max_weight: Trọng lượng nặng nhất của một đồ vật (mặc định 50kg).
    - max_value: Giá trị cao nhất của một đồ vật (mặc định 100$).
    
    Trả về:
    - W: Sức chứa tối đa của balo.
    - wt: Danh sách (list) trọng lượng các món đồ.
    - val: Danh sách (list) giá trị tương ứng của các món đồ.
    """
    
    # Dùng list comprehension để tạo ngẫu nhiên mảng trọng lượng và giá trị
    wt = [random.randint(1, max_weight) for _ in range(n)]
    val = [random.randint(10, max_value) for _ in range(n)]
    
    # CÁCH TÍNH SỨC CHỨA BALO (W) HỢP LÝ:
    # Nếu W quá lớn (chứa được hết đồ) -> Bài toán mất hay.
    # Nếu W quá nhỏ -> Không chọn được đồ nào.
    # Kinh nghiệm: Set W bằng khoảng 40% - 60% tổng trọng lượng của tất cả đồ vật.
    total_weight = sum(wt)
    W = int(total_weight * 0.5) 
    
    # Trả về 3 biến để các file khác lấy ra dùng
    return W, wt, val

# ---------- PHẦN TEST THỬ ----------
# Đoạn code dưới đây chỉ chạy khi bạn bấm nút Run trực tiếp file này.
# Nếu file này được gọi từ file main_demo.py, đoạn code này sẽ không chạy.
if __name__ == "__main__":
    print("--- CHẠY THỬ MÁY SINH DỮ LIỆU ---")
    n_test = 5
    print(f"Đang tạo test case thử nghiệm với {n_test} món đồ...\n")
    
    W_test, wt_test, val_test = generate_test_case(n_test)
    
    print(f"Sức chứa của balo (W) = {W_test} kg")
    print(f"Trọng lượng các món đồ (wt)  = {wt_test}")
    print(f"Giá trị các món đồ (val)     = {val_test}")
    print("---------------------------------")