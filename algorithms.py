# ==========================================
# FILE: algorithms.py
# CHỨC NĂNG: Chứa 4 thuật toán giải Knapsack
# ==========================================

# ---------------------------------------------------------
# 1. THUẬT TOÁN VÉT CẠN (BRUTE FORCE) - Giải 0/1 Knapsack
# ---------------------------------------------------------
def brute_force_knapsack(W, wt, val, n):
    # Điều kiện dừng: Nếu balo hết chỗ chứa (W=0) hoặc không còn đồ (n=0)
    if n == 0 or W == 0:
        return 0

    # Nếu món đồ thứ n nặng hơn phần sức chứa còn lại của balo -> Bắt buộc BỎ QUA
    if wt[n-1] > W:
        return brute_force_knapsack(W, wt, val, n-1)

    # Nếu nhét vừa, ta thử cả 2 cách và chọn cách mang lại giá trị lớn nhất (max):
    # Cách 1: LẤY món đồ này (cộng giá trị của nó, trừ đi sức chứa balo tương ứng)
    take = val[n-1] + brute_force_knapsack(W - wt[n-1], wt, val, n-1)
    
    # Cách 2: KHÔNG LẤY món đồ này (sức chứa balo giữ nguyên, xét đồ tiếp theo)
    leave = brute_force_knapsack(W, wt, val, n-1)

    return max(take, leave)


# ---------------------------------------------------------
# 2. THUẬT TOÁN QUAY LUI (BACKTRACKING) - Giải 0/1 Knapsack
# ---------------------------------------------------------
def backtracking_knapsack(W, wt, val, n):
    max_value = [0] # Dùng list có 1 phần tử để lưu biến toàn cục tham chiếu

    # Hàm đệ quy nội bộ để duyệt và cắt tỉa
    def backtrack(index, current_weight, current_value):
        # Cập nhật giá trị lớn nhất tìm được
        if current_value > max_value[0]:
            max_value[0] = current_value

        # Thử nhét các món đồ từ vị trí index hiện tại trở đi
        for i in range(index, n):
            # CẮT TỈA (Pruning): Chỉ đi tiếp nhánh này nếu balo còn nhét vừa
            if current_weight + wt[i] <= W:
                # Rẽ nhánh: Quyết định chọn món đồ thứ i
                backtrack(i + 1, current_weight + wt[i], current_value + val[i])
                # Khi hàm đệ quy rẽ nhánh xong, nó tự lùi lại (backtrack) để thử món khác

    # Bắt đầu chạy từ món đồ số 0, trọng lượng 0, giá trị 0
    backtrack(0, 0, 0)
    return max_value[0]


# ---------------------------------------------------------
# 3. QUY HOẠCH ĐỘNG (DYNAMIC PROGRAMMING) - Giải 0/1 Knapsack
# ---------------------------------------------------------
def dp_knapsack(W, wt, val, n):
    # Tạo một ma trận K kích thước (n+1) hàng và (W+1) cột, điền sẵn toàn số 0
    K = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    # Duyệt qua từng món đồ (hàng) và từng mức sức chứa của balo (cột)
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0 # Hàng 0 và cột 0 luôn bằng 0
            elif wt[i-1] <= w:
                # Nếu nhét vừa: Lấy max giữa việc CHỌN và KHÔNG CHỌN
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]], K[i-1][w])
            else:
                # Nếu quá nặng: Bắt buộc KHÔNG CHỌN (lấy kết quả từ hàng trên)
                K[i][w] = K[i-1][w]

    # Ô dưới cùng bên phải của ma trận chính là kết quả tối ưu nhất
    return K[n][W]


# ---------------------------------------------------------
# 4. THAM LAM (GREEDY) - Giải Fractional Knapsack (Cắt nhỏ đồ)
# ---------------------------------------------------------
def greedy_fractional_knapsack(W, wt, val, n):
    # Bước 1: Tính Tỉ suất sinh lời = (Giá trị / Trọng lượng) của từng món đồ
    items = []
    for i in range(n):
        ratio = val[i] / wt[i]
        items.append({'value': val[i], 'weight': wt[i], 'ratio': ratio})

    # Bước 2: Sắp xếp các món đồ theo tỉ suất sinh lời GIẢM DẦN (Món ngon nhất lên đầu)
    items.sort(key=lambda x: x['ratio'], reverse=True)

    total_value = 0.0

    # Bước 3: Lần lượt nhét đồ vào balo
    for item in items:
        if W >= item['weight']:
            # Nếu balo còn đủ chỗ chứa nguyên món đồ này -> Lấy trọn vẹn
            W -= item['weight']
            total_value += item['value']
        else:
            # Nếu balo sắp đầy, chỉ lấy một phần (fraction) của món đồ này cho đầy balo
            fraction = W / item['weight']
            total_value += item['value'] * fraction
            break # Balo đã đầy phè, dừng ngay lập tức

    return total_value

# ---------------------------------------------------------
# 5. THAM LAM (GREEDY) - Giải 0/1 Knapsack (Nguyên khối)
# ---------------------------------------------------------
def greedy_01_knapsack(W, wt, val, n):
    # Bước 1: Tính Tỉ suất sinh lời = (Giá trị / Trọng lượng) của từng món đồ
    items = []
    for i in range(n):
        ratio = val[i] / wt[i]
        items.append({'value': val[i], 'weight': wt[i], 'ratio': ratio})

    # Bước 2: Sắp xếp các món đồ theo tỉ suất sinh lời GIẢM DẦN (Món ngon nhất lên đầu)
    items.sort(key=lambda x: x['ratio'], reverse=True)

    total_value = 0

    # Bước 3: Lần lượt nhét đồ vào balo (Chỉ lấy nguyên khối)
    for item in items:
        if W >= item['weight']:
            # Nếu balo còn đủ chỗ chứa nguyên món đồ này -> Lấy trọn vẹn
            W -= item['weight']
            total_value += item['value']
        # Điểm khác biệt: Nếu không vừa, MẶC KỆ luôn (không có lệnh else để cắt nhỏ)

    return total_value
# ---------- PHẦN TEST THỬ ----------
# Đoạn này dùng để bạn tự kiểm tra xem code có chạy đúng logic không
if __name__ == "__main__":
    print("--- KIỂM TRA 4 THUẬT TOÁN ---")
    # Bộ test cố định giả lập: 4 món đồ, Balo chứa được 10kg
    val_test = [15, 20, 30, 5]
    wt_test = [1, 3, 5, 10]
    W_test = 10
    n_test = len(val_test)

    print(f"Balo = {W_test}kg | Trọng lượng = {wt_test} | Giá trị = {val_test}\n")
    
    print("1. Brute Force (0/1):", brute_force_knapsack(W_test, wt_test, val_test, n_test))
    print("2. Backtracking (0/1):", backtracking_knapsack(W_test, wt_test, val_test, n_test))
    print("3. Dynamic Programming (0/1):", dp_knapsack(W_test, wt_test, val_test, n_test))
    print("4. Greedy (Fractional):", greedy_fractional_knapsack(W_test, wt_test, val_test, n_test))
    
    # Kết quả mong đợi: 
    # Cả 3 thuật toán đầu (0/1) đều ra 65 (Lấy món 1+2+3)
    # Thuật toán Greedy Fractional có thể ra lớn hơn hoặc bằng tùy tỉ lệ cắt nhỏ.