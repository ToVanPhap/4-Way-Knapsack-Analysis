import time
import tracemalloc 
from data_generator import generate_test_case
import algorithms as alg

def run_demo():
    print("\n" + "="*70)
    print("🎓 ĐỒ ÁN: SO SÁNH CÁC PHƯƠNG PHÁP GIẢI BÀI TOÁN KNAPSACK 🎓")
    print("="*70 + "\n")
    
    # =====================================================================
    # PHẦN 1: CHỨNG MINH SỰ KHÁC BIỆT GIỮA OPTIMAL VÀ APPROXIMATE 
    # =====================================================================
    print(">>> PHẦN 1: TEST CASE ĐẶC BIỆT (Minh chứng Optimal vs Approximate)")
    time.sleep(1)
    
    W_fixed = 50
    wt_fixed = [10, 20, 30]
    val_fixed = [60, 100, 120]
    n_fixed = 3
    
    print("[+] DỮ LIỆU ĐẦU VÀO :")
    print(f"    - Balo (W): {W_fixed} kg")
    print(f"    - Món A: Nặng {wt_fixed[0]}kg, Giá trị {val_fixed[0]}, Tỷ lệ: {val_fixed[0]/wt_fixed[0]:.1f}")
    print(f"    - Món B: Nặng {wt_fixed[1]}kg, Giá trị {val_fixed[1]}, Tỷ lệ: {val_fixed[1]/wt_fixed[1]:.1f}")
    print(f"    - Món C: Nặng {wt_fixed[2]}kg, Giá trị {val_fixed[2]}, Tỷ lệ: {val_fixed[2]/wt_fixed[2]:.1f}\n")
    time.sleep(1)

    print("  ⏳ Đang chạy Tham lam (Greedy 0/1 - Approximate)...")
    res_gr_fixed = alg.greedy_01_knapsack(W_fixed, wt_fixed, val_fixed, n_fixed)
    print(f"  ❌ Kết quả Greedy: {res_gr_fixed} (Bị lừa lấy món A+B, thừa 20kg khoảng trống chết)\n")
    time.sleep(1)

    print("  ⏳ Đang chạy Quy hoạch động (DP - Optimal)...")
    res_dp_fixed = alg.dp_knapsack(W_fixed, wt_fixed, val_fixed, n_fixed)
    print(f"  ✅ Kết quả DP    : {res_dp_fixed} (Tối ưu tuyệt đối: Lấy món B+C)\n")
    time.sleep(1.5)

    # =====================================================================
    # PHẦN 2: CHẠY THỰC NGHIỆM VỚI DỮ LIỆU NGẪU NHIÊN (ĐO THỜI GIAN & RAM)
    # =====================================================================
    print("-" * 70)
    print(">>> PHẦN 2: CHẠY KIỂM THỬ VỚI DỮ LIỆU NGẪU NHIÊN (N LỚN HƠN)")
    
    n_random = 20
    print(f"🔄 Đang sinh ngẫu nhiên bộ dữ liệu với N = {n_random} đồ vật...\n")
    time.sleep(1)
    
    W, wt, val = generate_test_case(n_random)
    
    print("[+] THÔNG TIN DỮ LIỆU ĐẦU VÀO NGẪU NHIÊN:")
    print(f"    - Sức chứa Balo (W): {W} kg")
    print(f"    - Trọng lượng (wt) : {wt}")
    print(f"    - Giá trị (val)    : {val}\n")
    time.sleep(1)
    
    # 1. Brute Force
    print("  ⏳ Đang chạy Vét cạn (Brute Force) - Vui lòng đợi...")
    tracemalloc.start() # Bật máy quét RAM
    start = time.time()
    res_bf = alg.brute_force_knapsack(W, wt, val, n_random)
    t_bf = time.time() - start
    _, peak_bf = tracemalloc.get_traced_memory() # Lấy lượng RAM đỉnh điểm (Bytes)
    tracemalloc.stop() # Tắt máy quét
    # In thêm thông số RAM, đổi từ Bytes sang MB chia cho (1024*1024)
    print(f"  ✅ Kết quả: {res_bf:<8.2f} | ⏱️ Thời gian: {t_bf:.5f} giây | 💾 RAM: {peak_bf / (1024*1024):.6f} MB\n")
    
    # 2. Backtracking
    print("  ⏳ Đang chạy Quay lui (Backtracking)...")
    tracemalloc.start()
    start = time.time()
    res_bt = alg.backtracking_knapsack(W, wt, val, n_random)
    t_bt = time.time() - start
    _, peak_bt = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"  ✅ Kết quả: {res_bt:<8.2f} | ⏱️ Thời gian: {t_bt:.5f} giây | 💾 RAM: {peak_bt / (1024*1024):.6f} MB\n")
    
    # 3. Dynamic Programming
    print("  ⏳ Đang chạy Quy hoạch động (Dynamic Programming)...")
    tracemalloc.start()
    start = time.time()
    res_dp = alg.dp_knapsack(W, wt, val, n_random)
    t_dp = time.time() - start
    _, peak_dp = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"  ✅ Kết quả: {res_dp:<8.2f} | ⏱️ Thời gian: {t_dp:.5f} giây | 💾 RAM: {peak_dp / (1024*1024):.6f} MB\n")
    
    # 4. Greedy
    print("  ⏳ Đang chạy Tham lam (Greedy - Fractional)...")
    tracemalloc.start()
    start = time.time()
    res_gr = alg.greedy_fractional_knapsack(W, wt, val, n_random)
    t_gr = time.time() - start
    _, peak_gr = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"  ✅ Kết quả: {res_gr:<8.2f} | ⏱️ Thời gian: {t_gr:.5f} giây | 💾 RAM: {peak_gr / (1024*1024):.6f} MB\n")
    
    print("="*70)
    print("📌 TỔNG KẾT ĐÁNH GIÁ:")
    print(" - Với bài toán 0/1 Knapsack, DP luôn đảm bảo tính chính xác tuyệt đối.")
    print(" - Greedy chạy nhanh nhất nhưng chỉ nên dùng nếu bài toán cho phép cắt nhỏ")
    print("   đồ vật (Fractional), hoặc khi hệ thống chấp nhận sai số (Approximate).")
    print(" - QUAN TRỌNG: DP tiêu tốn nhiều RAM nhất do phải cấp phát ma trận lưu trữ.")
    print("="*70 + "\n")

if __name__ == "__main__":
    run_demo()