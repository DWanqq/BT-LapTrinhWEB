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
  4. Khởi tạo repository công khai `BT-LapTrinhWEB` trên GitHub.

---

##  BÀI 2: XÂY DỰNG WEB LOGIN, DOCKER & CẤU HÌNH TÊN MIỀN FREE
* **Mục tiêu:** Lập trình ứng dụng Web Login bằng **Python (Flask)**, đóng gói bằng **Docker** và cấu hình tên miền truy cập miễn phí.
* **Thành phần mã nguồn:**
  * `app.py`: Giao diện HTML/CSS và logic xác thực đăng nhập.
  * `requirements.txt`: Khai báo thư viện Flask.
  * `Dockerfile`: Kịch bản đóng gói ứng dụng trên nền Python 3.10-slim.

---

## 🌐 CẤU HÌNH TÊN MIỀN (DOMAIN CONFIGURATION)

### 1. Tên miền Nội bộ (Local Domain)
Cấu hình ánh xạ địa chỉ `127.0.0.1` tới tên miền ảo `web-login.local` trong tệp `/etc/hosts`:
```bash
echo "127.0.0.1 web-login.local" | sudo tee -a /etc/hosts
```
* **Đường dẫn truy cập nội bộ:** `http://web-login.local:5000`

### 2. Tên miền Công cộng Miễn phí (Free Public Domain)
Sử dụng công cụ SSH Tunneling để tạo tên miền HTTPS miễn phí ra ngoài Internet:
```bash
ssh -R 80:localhost:5000 nokey@localhost.run
```
* **Đường dẫn truy cập công cộng:** `https://<random_subdomain>.lhr.life`

---

##  HƯỚNG DẪN KHỞI CHẠY ỨNG DỤNG (CLI)

```bash
# 1. Đóng gói Docker Image
docker build -t web-login-app .

# 2. Khởi chạy Docker Container
docker run -d -p 5000:5000 --name running-web-login web-login-app
```
* **Tài khoản thử nghiệm:** `admin` / **Mật khẩu:** `123456`

---

## 🛠️ CÁC LỆNH QUẢN LÝ DOCKER CONTAINER
* Xem danh sách container: `docker ps`
* Dừng ứng dụng: `docker stop running-web-login`
* Xóa container: `docker rm running-web-login`
EOF

git add README.md
git commit -m "Cap nhat toan bo bao cao README hoan chinh va trinh bay chuan"
git push
