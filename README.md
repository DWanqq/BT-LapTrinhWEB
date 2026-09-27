
# BÁO CÁO BÀI TẬP MÔN LẬP TRÌNH WEB

* **Giảng viên hướng dẫn:** Đỗ Duy Cốp
* **Sinh viên thực hiện:** Trần Đình Quang 
* **Mssv**  : K235480106057
* **Lớp**   : K59KMT
---

##  BÀI 1: THIẾT LẬP MÔI TRƯỜNG PHÁT TRIỂN WEB DEV & GIT
* **Mục tiêu:** Cấu hình môi trường Linux (WSL2), cài đặt Docker và kết nối SSH an toàn với GitHub.
* **Nội dung thực hiện:**
  1. Khởi tạo môi trường **WSL2 (Ubuntu)** trên hệ điều hành Windows.
  2. Cấu hình thông tin cá nhân Git (`user.name`, `user.email`).
  3. Tạo mã xác thực SSH Key (`ed25519`) để kết nối an toàn với GitHub.
  4. Tạo repository công khai `BT-LapTrinhWEB` trên GitHub.

---

##  BÀI 2: XÂY DỰNG & ĐÓNG GÓI ỨNG DỤNG WEB LOGIN BẰNG DOCKER
* **Mục tiêu:** Lập trình ứng dụng Web Login bằng **Python (Flask)** và đóng gói vận hành bằng **Docker Container**.
* **Thành phần mã nguồn:**
  * `app.py`: Xử lý giao diện HTML/CSS và logic xác thực đăng nhập.
  * `requirements.txt`: Khai báo thư viện Flask.
  * `Dockerfile`: Kịch bản đóng gói ứng dụng trên nền Python 3.10-slim.

### Hướng dẫn chạy ứng dụng (CLI):
```bash
# 1. Build Docker Image
docker build -t web-login-app .

# 2. Khởi chạy Docker Container
docker run -d -p 5000:5000 --name running-web-login web-login-app
