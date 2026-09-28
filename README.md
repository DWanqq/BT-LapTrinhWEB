# BÁO CÁO BÀI TẬP MÔN LẬP TRÌNH WEB

## TỔNG QUAN BÁO CÁO (OVERVIEW)
* **Môn học:** Lập trình Web
* **Giảng viên hướng dẫn:** Đỗ Duy Cốp
* **Sinh viên thực hiện:** Trần Đình Quang
* **Mã sinh viên (MSSV):** K235480106057
* **Lớp:** K59KMT

---

## BÀI 1: THIẾT LẬP MÔI TRƯỜNG PHÁT TRIỂN WEB DEV & GIT
* **Mục tiêu:** Cấu hình môi trường Linux (WSL2), cài đặt Docker và kết nối SSH an toàn với GitHub.
* **Nội dung thực hiện:**
1. Khởi tạo môi trường **WSL2 (Ubuntu)** trên hệ điều hành Windows.
2. Cấu hình thông tin cá nhân Git (`user.name`, `user.email`).
3. Tạo mã xác thực SSH Key (`ed25519`) để kết nối an toàn với GitHub.
4. Khởi tạo repository công khai `BT-LapTrinhWEB` trên GitHub.

---

## BÀI 2: XÂY DỰNG WEB LOGIN, DOCKER & CẤU HÌNH TÊN MIỀN FREE
* **Mục tiêu:** Lập trình ứng dụng Web Login bằng **Python (Flask)**, đóng gói bằng **Docker** và cấu hình tên miền truy cập miễn phí.
* **Thành phần mã nguồn:**
* `app.py`: Giao diện HTML/CSS và logic xác thực đăng nhập.
* `requirements.txt`: Khai báo thư viện Flask.
* `Dockerfile`: Kịch bản đóng gói ứng dụng trên nền Python 3.10-slim.

---

## CẤU HÌNH TÊN MIỀN (DOMAIN CONFIGURATION)

### 1. Tên miền Nội bộ (Local Domain)
Cấu hình ánh xạ địa chỉ `127.0.0.1` tới tên miền ảo `web-login.local` trong tệp `/etc/hosts`:
```bash
echo "127.0.0.1 web-login.local" | sudo tee -a /etc/hosts

