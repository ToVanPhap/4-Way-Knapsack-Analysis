import time
import matplotlib.pyplot as plt
from data_generator import generate_test_case
import algorithms as alg

def run_experiment():
    # Các mốc dữ liệu chiến thuật, cắt Brute Force ở N=23, kết thúc ở N=500
    N_values = [10, 15, 20, 22, 23, 50, 100, 200, 500]
    
    time_bf, time_bt, time_dp, time_greedy = [], [], [], []

    print("--- BẮT ĐẦU CHẠY THỰC NGHIỆM ĐO THỜI GIAN ---")
    print("Lưu ý: Máy sẽ khựng lại vài giây ở N=22 và 23 do Brute Force hoạt động. Đừng tắt!\n")
    
    for n in N_values:
        print(f"Đang xử lý test case với N = {n} ...")
        W, wt, val = generate_test_case(n)
        
        # 1. BRUTE FORCE
        if n <= 23:
            start = time.time()
            alg.brute_force_knapsack(W, wt, val, n)
            time_bf.append(time.time() - start)
        else:
            time_bf.append(None)

        # 2. BACKTRACKING
        if n <= 23:
            start = time.time()
            alg.backtracking_knapsack(W, wt, val, n)
            time_bt.append(time.time() - start)
        else:
            time_bt.append(None)

        # 3. DYNAMIC PROGRAMMING
        start = time.time()
        alg.dp_knapsack(W, wt, val, n)
        time_dp.append(time.time() - start)

        # 4. GREEDY
        start = time.time()
        alg.greedy_fractional_knapsack(W, wt, val, n)
        time_greedy.append(time.time() - start)

    print("\n--- HOÀN THÀNH THỰC NGHIỆM! ĐANG VẼ BIỂU ĐỒ... ---")
    
    # VẼ BIỂU ĐỒ
    plt.figure(figsize=(10, 6))
    
    n_bf = [N_values[i] for i in range(len(N_values)) if time_bf[i] is not None]
    t_bf = [x for x in time_bf if x is not None]
    
    n_bt = [N_values[i] for i in range(len(N_values)) if time_bt[i] is not None]
    t_bt = [x for x in time_bt if x is not None]

    plt.plot(n_bf, t_bf, label='Brute Force', color='red', marker='o', linewidth=2.5)
    plt.plot(n_bt, t_bt, label='Backtracking', color='orange', marker='s', linewidth=2.5)
    plt.plot(N_values, time_dp, label='Dynamic Programming', color='blue', marker='^', linewidth=2)
    plt.plot(N_values, time_greedy, label='Greedy (Fractional)', color='green', marker='x', linewidth=2)

    # Căn chỉnh không gian trục Y và X
    plt.ylim(-0.1, max(t_bf) + 0.5) 
    plt.xlim(-15, max(N_values) + 20) 

    plt.title('Đánh giá Runtime 4 thuật toán Knapsack', fontsize=14, fontweight='bold')
    plt.xlabel('Số lượng đồ vật (N)', fontsize=12)
    plt.ylabel('Thời gian thực thi (Giây)', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.5)
    
    # Dời bảng chú thích (Legend) sang góc TRÊN BÊN PHẢI
    plt.legend(loc='upper right', fontsize=11)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    run_experiment()